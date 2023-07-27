import sklearn.preprocessing as preprocessing
import numpy as np
import pandas as pd

class Predict():

    def Encoding(targets, new_targes):

        labelEnc = preprocessing.LabelEncoder()
        new_target = labelEnc.fit_transform(targets)
        onehotEnc = preprocessing.OneHotEncoder()
        onehotEnc.fit(new_target.reshape(-1, 1))
        targets_trans = onehotEnc.transform(new_target.reshape(-1, 1))


        new_targes

        return targets_trans