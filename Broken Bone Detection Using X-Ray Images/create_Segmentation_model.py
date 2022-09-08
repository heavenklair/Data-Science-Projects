import keras.models as models
from utils import jacard_loss

def my_Unet(model_path):
    model = models.load_model(model_path, custom_objects = {'jacard': jacard_loss})
    return model

def my_simple_encoder_decoder(model_path):
    model = models.load_model(model_path)
    return model
