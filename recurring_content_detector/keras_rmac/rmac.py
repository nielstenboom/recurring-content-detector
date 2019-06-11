from __future__ import division
from __future__ import print_function

from keras.layers import Lambda, Dense, TimeDistributed, Input
from keras.models import Model
from keras.preprocessing import image
import keras.backend as K

import PIL

from keras.applications.vgg16 import VGG16
# from .vgg16 import VGG16
from .RoiPooling import RoiPooling
from .get_regions import rmac_regions, get_size_vgg_feat_map
from .utils import *

import scipy.io
import numpy as np
import cv2 

import matplotlib.pyplot as plt

K.set_image_dim_ordering('th')

INPUT_DIMENSION = (224,224)
vector_size = 512

def addition(x):
    sum = K.sum(x, axis=1)
    return sum


def weighting(input):
    x = input[0]
    w = input[1]
    w = K.repeat_elements(w, vector_size, axis=-1)
    out = x * w
    return out



def rmac(input_shape, num_rois):

    # Load VGG16
    # vgg16_model = VGG16(DATA_DIR + WEIGHTS_FILE, input_shape)
    vgg16_model = VGG16(input_shape = input_shape, weights='imagenet', include_top=False)
    print(vgg16_model.summary())

    # Regions as input
    in_roi = Input(shape=(num_rois, 4), name='input_roi')

    # ROI pooling
    x = RoiPooling([1], num_rois)([vgg16_model.layers[-5].output, in_roi])

    # Normalization
    x = Lambda(lambda x: K.l2_normalize(x, axis=2), name='norm1')(x)

    # PCA
    x = TimeDistributed(Dense(vector_size, name='pca',
                              kernel_initializer='identity',
                              bias_initializer='zeros'))(x)

    # Normalization
    x = Lambda(lambda x: K.l2_normalize(x, axis=2), name='pca_norm')(x)

    # Addition
    rmac = Lambda(addition, output_shape=(vector_size,), name='rmac')(x)

    # # Normalization
    rmac_norm = Lambda(lambda x: K.l2_normalize(x, axis=1), name='rmac_norm')(rmac)

    # Define model
    model = Model([vgg16_model.input, in_roi], rmac_norm)

    # Load PCA weights
    mat = scipy.io.loadmat(DATA_DIR + PCA_FILE)
    b = np.squeeze(mat['bias'], axis=1)
    w = np.transpose(mat['weights'])
    model.layers[-4].set_weights([w, b])

    return model



# Load RMAC model
Wmap, Hmap = get_size_vgg_feat_map(INPUT_DIMENSION[0],INPUT_DIMENSION[1])
regions = rmac_regions(Wmap, Hmap, 3)
print('Loading RMAC model...')
model = rmac((3, INPUT_DIMENSION[0], INPUT_DIMENSION[1]), len(regions))
print(model.summary())

def to_feature_vector(img_array):

    img = cv2.resize(img_array, dsize=INPUT_DIMENSION, interpolation = cv2.INTER_NEAREST)
    img = img.reshape((3, INPUT_DIMENSION[0], INPUT_DIMENSION[1]))
    img = np.expand_dims(img, axis=0)

    # Compute RMAC vector
    RMAC = model.predict([img, np.expand_dims(regions, axis=0)])

    return RMAC[0,:].astype('float32')






