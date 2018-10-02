"""
Assume single dataframe to a single cleaner
"""
class Cleaner:
    def __init__(self, df):
        print('Initializing Cleaner')
        self.df = df

    """Removes NAN values from DataFrame"""
    def remove_nan(self):
        print('Removing NaN')
        self.df.dropna(inplace=True)
    
    def get_df(self):
        return self.df