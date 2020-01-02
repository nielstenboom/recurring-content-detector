import pickle
import os

realpath = os.path.dirname(os.path.realpath(__file__))

DATA_DIR = realpath +'/data/'
PCA_FILE = 'PCAmatrices.mat'
IMG_SIZE = 1024


def save_obj(obj, filename):
    f = open(filename, 'wb')
    pickle.dump(obj, f)
    f.close()
    print("Object saved to %s." % filename)


def load_obj(filename):
    f = open(filename, 'rb')
    obj = pickle.load(f)
    f.close()
    print("Object loaded from %s." % filename)
    return obj


def preprocess_image(x):

    # Substract Mean
    x[:, 0, :, :] -= 103
    x[:, 1, :, :] -= 116
    x[:, 2, :, :] -= 123

    # 'RGB'->'BGR'
    x = x[:, ::-1, :, :]

    return x