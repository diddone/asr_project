from torch import distributions
from torch import Tensor

from src.augmentations.base import AugmentationBase

class GaussianNoise(AugmentationBase):
    def __init__(self, scale=0.011):
        self._sampler = distributions.Normal(0, scale)

    def __call__(self, data: Tensor):
        return (data + self._sampler.sample(data.size())).clamp(-1, 1)
