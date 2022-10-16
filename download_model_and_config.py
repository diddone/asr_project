import gdown

model_url = 'https://drive.google.com/uc?export=download&id=1VNTFKR3pydGduRYU-9zFqkjizCDp9EjL'
config_url = 'https://drive.google.com/uc?export=download&id=14eaEuUaA2-xiMypkBxJtdM3X7Ly33BNb'
output = 'defaul_test_model/'

gdown.download(model_url, output=output)
gdown.download(config_url, output=output)
