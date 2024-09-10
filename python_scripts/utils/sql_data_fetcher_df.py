from .sql_data_fetcher import SqlDataFetcher
import pandas as pd 

class SqlDataFetcherDF(SqlDataFetcher):
    def __init__(self, sql_query):
        super().__init__(sql_query)
        self.data, self.columns = self.fetch_data()
    def to_df(self):
        df = pd.DataFrame(self.data, columns= self.columns)
        return df
