from collections import Callable
from typing import List

import src.augmentations.spectrogram_augmentations
import src.augmentations.wave_augmentations
from src.augmentations.sequential import SequentialAugmentation
from src.augmentations.random_apply import RandomApply
from src.utils.parse_config import ConfigParser

def from_configs(configs: ConfigParser):
    wave_augs = []

    proba = configs.config["augmentations"]['proba'] if 'proba' in configs.config["augmentations"] else None
    print(proba, 'Proba in init augmentations')
    if "augmentations" in configs.config and "wave" in configs.config["augmentations"]:
        for aug_dict in configs.config["augmentations"]["wave"]:
            aug_obj = configs.init_obj(aug_dict, src.augmentations.wave_augmentations)
            wave_augs.append(
                RandomApply(aug_obj, p=proba) if proba is not None else aug_obj
            )

    spec_augs = []
    if "augmentations" in configs.config and "spectrogram" in configs.config["augmentations"]:
        for aug_dict in configs.config["augmentations"]["spectrogram"]:
            aug_obj = configs.init_obj(aug_dict, src.augmentations.spectrogram_augmentations)
            spec_augs.append(
                RandomApply(aug_obj, p=proba) if proba is not None else aug_obj
            )
    return _to_function(wave_augs), _to_function(spec_augs)


def _to_function(augs_list: List[Callable]):
    if len(augs_list) == 0:
        return None
    elif len(augs_list) == 1:
        return augs_list[0]
    else:
        return SequentialAugmentation(augs_list)
