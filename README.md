# ASR project

Implemented [DeepSpeech2](https://arxiv.org/pdf/1512.02595.pdf).

Training summary:
- Optimzer: Adam
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

## Installation guide

< Write your installation guide here >

Firstly clone repo and install requirements.

```shell
git clone https://github.com/diddone/asr_project
cd asr_project
pip install -r requirements.txt
```


## Wandb Report Link
[Link](https://wandb.ai/diddone/asr_project/reports/Report--VmlldzoyODAyMzc2) to wandb report with plots and metrics
