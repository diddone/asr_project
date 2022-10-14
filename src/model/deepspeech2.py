import torch.nn as nn

from torch.nn import Sequential
from src.base import BaseModel


class DeepSpeech(BaseModel):

    def __init__(
        self, n_feats, n_class,
        num_conv_layers=2, num_rnn_layers=4, rnn_size=512, use_lstm=True, use_biderect=True,
        use_layer_norm=True, **batch):
        super().__init__(n_feats, n_class, **batch)

        self.use_layer_norm = use_layer_norm
        self.num_conv_layers = num_conv_layers

        self.convs = []
        self.fc = []

        if num_conv_layers not in [1, 2, 3]:
            raise ValueError(f"Only [1, 2, 3] number of conv layers is supported, given{num_conv_layers}")

        self.conv_args_list = [
                (32, (11, 41), (2, 2)),
                (32, (11, 21), (1, 2)),
                (96, (11, 21), (1, 2)),
        ]

        conv_output_size = n_feats
        for i in range(num_conv_layers):
            in_channels = self.conv_args_list[i - 1][0] if i != 0 else 1
            out_channels = self.conv_args_list[i][0]
            kernel_size = self.conv_args_list[i][1]
            stride = self.conv_args_list[i][2]

            self.convs.append(nn.Conv2d(in_channels, out_channels, kernel_size, stride=stride))
            self.convs.append(nn.ReLU())

            conv_output_size = (conv_output_size - kernel_size[1]) // stride[1] + 1
        conv_output_size *= self.conv_args_list[num_conv_layers - 1][0]
        self.convs = Sequential(*self.convs)

        self.rnns = nn.ModuleList([])
        rnn_block = nn.LSTM if use_lstm else nn.GRU
        rnn_output_size = 2 * rnn_size if use_biderect else rnn_size
        for i in range(num_rnn_layers):
            input_size = rnn_output_size if i != 0 else conv_output_size
            self.rnns.append(rnn_block(input_size, rnn_size, batch_first=True, bidirectional=use_biderect))
            if use_layer_norm:
                self.rnns.append(nn.LayerNorm(rnn_output_size))

        self.fc = nn.Linear(rnn_output_size, n_class)


    def forward(self, spectrogram, **batch):
        # b, f, t
        x = spectrogram.transpose(1, 2).unsqueeze(dim=1)
        # b, c, t, f
        x = self.convs(x)

        # b, c, t, f
        b_size, c_size, t_size, f_size = x.size()
        x = x.permute(0, 2, 1, 3).reshape([b_size, t_size, c_size * f_size])

        step = 2 if self.use_layer_norm else 1
        for i in range(0, len(self.rnns), step):
            # rnn layer
            x, _ = self.rnns[i](x)

            # layernorm
            if self.use_layer_norm:
                x = self.rnns[i + 1](x)

        logits = self.fc(x)
        return {"logits": logits}


    def transform_input_lengths(self, input_lengths):
        """
        Input length transformation function.
        For example: if your NN transforms spectrogram of time-length `N` into an
            output with time-length `N / 2`, then this function should return `input_lengths // 2`
        """

        for i in range(self.num_conv_layers):
            kernel_size = self.conv_args_list[i][1]
            stride = self.conv_args_list[i][2]

            input_lengths = (input_lengths - kernel_size[0]) // stride[0] + 1

        return input_lengths

