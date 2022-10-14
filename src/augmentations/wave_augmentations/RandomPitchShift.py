from torch import distributions, from_numpy
from torch import Tensor
from librosa.effects import pitch_shift
import numpy as np

from src.augmentations.base import AugmentationBase

class RandomPitchShift(AugmentationBase):
    def __init__(self, max_n_steps=3, beta_param=0.9):
        self.max_n_steps = max_n_steps
        self.beta_param = beta_param

    def __call__(self, data: Tensor):
        n_steps = (np.random.beta(self.beta_param, self.beta_param, 1) - 0.5) * 2 * self.max_n_steps
        return from_numpy(pitch_shift(data.numpy(), 16000, n_steps))
