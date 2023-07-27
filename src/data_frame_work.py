import pandas as pd
from pathlib import Path

class DataFrameWork():

    def __init__(self) -> None:
        self.current_dir = Path.cwd()
        self.project_dir = [p for p in self.current_dir.parents if p.parts[-1]=='immo-eliza-data-analysis'][0]


    def get_data_frame(self):
        """Geting data to model from a csv file

        Returns:
            dataFrame: DataFrame with the information of the csv file
        """  
        path_to_open = self.project_dir / "data" / "_data_clean_to_model.csv"
        immo = pd.read_csv(path_to_open, index_col='id')
        return immo

    def save_data_frame_clean(self, df):
        """Saving data clean in csv file

        Args:
            df (DataFrame): DataFrame to save
        """   
        path_to_save = self.project_dir / "data" / "_data_clean.csv"     
        df.to_csv(path_to_save)

    def get_data_frame_clean(self):
        """Geting data clean from a csv file

        Returns:
            dataFrame: DataFrame with the information of the csv file
        """        
        path_to_open = self.project_dir / "data" / "_data_clean.csv"
        immo = pd.read_csv(path_to_open, index_col='id')
        return immo
    
    def save_data_frame_clean_to_model(self, df):
        """Saving data cleaning to use in a model in csv file

        Args:
            df (DataFrame): DataFrame to save
        """ 
        path_to_save = self.project_dir / "data" / "_data_clean_to_model.csv"       
        df.to_csv(path_to_save)

    def get_data_frame_properties(self):
        """Geting initial data of properties from a csv file

        Returns:
            dataFrame: DataFrame with the information of the csv file
        """
        path_to_open = self.project_dir / "data" / "_properties_data.csv"
        immo = pd.read_csv(path_to_open, index_col='id')
        return immo