# ASR project

Implemented [DeepSpeech2](https://arxiv.org/pdf/1512.02595.pdf).

## Installation guide

Firstly clone repo and install requirements.

```shell
git clone https://github.com/diddone/asr_project
cd asr_project
pip install -r requirements.txt
pip install gdown
python3 download_model_and_config.py
```

Download model and lm

```shell
mkdir lm
mkdir defaul_test_model
wget http://www.openslr.org/resources/11/3-gram.arpa.gz -P lm/
python3 download_model_and_config.py
python3 download_lm.py
```


Training summary:
- Optimizer: Adam
- Scheduler: OneCycleLR
- Model: DeepSpeech2 (1 conv and 6 lstms with layernorms)
- Dataset: full [LibriSpeech](https://www.openslr.org/12)
- Evaluation: LM with beamsearch

All training details can be found in [report](https://wandb.ai/diddone/asr_project/reports/Report--VmlldzoyODAyMzc2).

## Results

Provided results for other part.

- WER Argmax 0.25192699801889545
- CER Argmax 0.09848671659088183
- WER shallow LM 0.18023283293222706
- CER shallow LM 0.08360096510883173




## Wandb Report Link
[Link](https://wandb.ai/diddone/asr_project/reports/Report--VmlldzoyODAyMzc2) to wandb report with plots and metrics

## UPD
If linear grading will be aplied. Due to datasphere bugs one model was training a lot on train-clean-360 and train-other-500 with augmentations. After little tuning without them I get results:

- WER 0.24104289971977025
- CER 0.0937899395060756
- WER 0.16657656234520304
- CER 0.0780798601124191


Links to [model](https://drive.google.com/uc?export=download&id=1saBj6YJCSqVqifq645rvsy-LXBYZsN9n) and [config](https://drive.google.com/uc?export=download&id=1S7GMc26aloq-lgSwCuky42mxeWMib0Jv). They can be downloaded using download_model_and_config.py file.
