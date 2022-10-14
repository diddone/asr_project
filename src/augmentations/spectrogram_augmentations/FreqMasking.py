from torchaudio.transforms import FrequencyMasking
from src.augmentations.base import AugmentationBase
from torch import Tensor

class FreqMask(AugmentationBase):
    def __init__(self, freq_mask_param=15):
        self._aug = FrequencyMasking(freq_mask_param)

    def __call__(self, spec: Tensor):
        return self._aug(spec)