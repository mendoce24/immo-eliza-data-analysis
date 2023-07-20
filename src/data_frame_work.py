import pandas as pd

class DataFrameWork():

    def get_data_frame():
        """Geting data to model from a csv file

        Returns:
            dataFrame: DataFrame with the information of the csv file
        """        
        path = "../data/_data_clean_to_model.csv"
        immo = pd.read_csv(path, index_col='id')
        return immo

    def save_data_frame_clean(df):
        """Saving data clean in csv file

        Args:
            df (DataFrame): DataFrame to save
        """        
        df.to_csv('../data/_data_clean.csv')

    def get_data_frame_clean():
        """Geting data clean from a csv file

        Returns:
            dataFrame: DataFrame with the information of the csv file
        """        
        path = "../data/_data_clean.csv"
        immo = pd.read_csv(path, index_col='id')
        return immo
    
    def save_data_frame_clean_to_model(df):
        """Saving data cleaning to use in a model in csv file

        Args:
            df (DataFrame): DataFrame to save
        """        
        df.to_csv('../data/_data_clean_to_model.csv')

    def get_data_frame_properties():
        """Geting initial data of properties from a csv file

        Returns:
            dataFrame: DataFrame with the information of the csv file
        """        
        path = "../data/_properties_data.csv"
        immo = pd.read_csv(path, index_col='id')
        return immo