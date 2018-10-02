import pandas as pd

class Workbench:
    """
    Parameter Variables
    dataset_path: Path to the dataset on the disk
    """
    def __init__(self, dataset_path, columns):
        print('Initializing Workbench')
        self.source_dataset = self.load_dataset(dataset_path)
        self.df = self.source_dataset[columns]

    """
    Returns a Dataframe 
    """
    def load_dataset(self, path):
        return pd.read_csv(path)
    
    """
    Replaces self.df
    """
    def save_df(self, df):
        self.df = df

    def get_df(self):
        return self.df
        
    def report(self):
        print(self.df)
        