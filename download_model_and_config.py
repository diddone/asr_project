import gdown

model_url = 'https://drive.google.com/uc?export=download&id=1saBj6YJCSqVqifq645rvsy-LXBYZsN9n'
config_url = 'https://drive.google.com/uc?export=download&id=1S7GMc26aloq-lgSwCuky42mxeWMib0Jv'
output = 'defaul_test_model/'

gdown.download(model_url, output=output)
gdown.download(config_url, output=output)
