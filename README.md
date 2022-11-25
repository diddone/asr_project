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

Argmax WER 0.2651159555363254
Argmax CER 0.10502687285110361
LM WER 0.18848792641611095
LM CER 0.08801816818572956


## Wandb Report Link
[Link](https://wandb.ai/diddone/asr_project/reports/Report--VmlldzoyODAyMzc2) to wandb report with plots and metrics
