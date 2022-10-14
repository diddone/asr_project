import logging
from typing import List
import torch
import torchaudio

logger = logging.getLogger(__name__)


def collate_fn(dataset_items: List[dict]):
    """
    Collate and pad fields in dataset items
    """

    result_batch = {}
    spec_lengths = []
    text_lengths = []

    text = []
    for item in dataset_items:
        spec_lengths.append(item['spectrogram'].shape[-1])
        text_lengths.append(item['text_encoded'].shape[-1])
        text.append(item['text'])
    batch_size = len(spec_lengths)
    max_specs_length = max(spec_lengths)
    max_text_length = max(text_lengths)

    spec_batch = torch.zeros(batch_size, item['spectrogram'].shape[1], max_specs_length)
    text_encoded_batch = torch.zeros(batch_size, max_text_length)

    for i, item in enumerate(dataset_items):
        spec_batch[i, :, :spec_lengths[i]] = item['spectrogram']
        text_encoded_batch[i, :text_lengths[i]] = item['text_encoded']

    return {
        'spectrogram': spec_batch,
        'spectrogram_length': torch.tensor(spec_lengths).long(),
        'text_encoded': text_encoded_batch,
        'text_encoded_length': torch.tensor(text_lengths).long(),
        'text': text,
        'audio_path': dataset_items[0]['audio_path'],
        'audio_sample': dataset_items[0]['audio'],
        'text_sample': dataset_items[0]['text']
    }