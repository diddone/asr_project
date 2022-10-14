from torchaudio.transforms import TimeMasking
from src.augmentations.base import AugmentationBase
from torch import Tensor

class TimeMask(AugmentationBase):
    def __init__(self, time_mask_param=40, proportion=1):
        self._aug = TimeMasking(time_mask_param, p=proportion)

    def __call__(self, spec: Tensor):
        return self._aug(spec)