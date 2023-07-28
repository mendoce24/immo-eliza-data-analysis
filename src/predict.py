import numpy as np
import pandas as pd
import pickle
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from read_write_files import ReadWriteFiles


class Predict():

    def __init__(self) -> None:
        pass


    def get_price_api(self, immo):
        immoData = ReadWriteFiles().get_data_frame()
        X, y = self.get_X_y(immoData)
        X_train, X_test, y_train, y_test = self.get_train_test(X, y)
        X_train, immo = self.encode_data(X_train, immo)
        
        filename = "models/immo_model.pickle"

        # load model
        loaded_model = pickle.load(open(filename, "rb"))

        # predition with training data 
        pred_train= loaded_model.predict(immo)
        print (pred_train)    

        value_to_return = '{ "prediction": '+ str(round(pred_train[0], 2)) +', "status_code": 200 }'

        return value_to_return


    def encode_data(self, targets, new_targets):
        
        transformer = ColumnTransformer(transformers=[(
            'cat', OneHotEncoder(sparse_output=False, handle_unknown='ignore'),[0,1, 2, 3, 4, 10, 12, 24]
        )], remainder='passthrough').fit(targets)

        targets = transformer.transform(targets)
        new_targets = transformer.transform(new_targets)

        return targets, new_targets
    

    def get_X_y(self, df):
        """Get the target (y) and features (X)
        Args:
            df (DataFrame): Framework with data from immo Eliza
        Returns:
            NumpyArray: Target, Features
        """
        # Drop clumns with not impat in the prediction
        X = pd.DataFrame(df.drop(columns=['price', 'gardenSurface', 'terraceSurface', 'floor']))#features
        y = np.array(df.price).reshape(-1, 1)#target

        return X, y
    
    
    def get_train_test(self, X, y, normalize = False):
        """Split the target and features in training and test data
        Args:
            X (NumpyArray): Feature
            y (NumpyArray): Target
            normalize (bool, optional): Normalize the Features to train and test. Defaults to False.
        Returns:
            NumpyArray: X_train, X_test, y_train, y_test
        """        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=40)

        # validation to normalize or not the Xtrain and Xtest
        if normalize:
            scalar = StandardScaler()

            X_train = np.array(pd.DataFrame(
                scalar.fit_transform(X_train),
                columns = X_train.columns
            ))

            X_test = np.array(pd.DataFrame(
                scalar.transform(X_test),
                columns = X_test.columns
            ))
        
        return X_train, X_test, y_train, y_test
    

    def get_performance(self, y, pred):
        """Get the performace of a model prediction
        Args:
            y (NumpyArray): Target
            pred (NumpyArray): Prediction
        Returns:
            Floats: score, mse, rmse, mae
        """        
        score = r2_score(y, pred) # Score
        mse = mean_squared_error(y, pred) # Mean Squared Error
        rmse = mse**0.5 # Root Mean Squared Error
        mae = mean_absolute_error(y, pred) # Mean Absolute Error

        return score, mse, rmse, mae
    
