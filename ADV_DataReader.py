from sqlalchemy import create_engine
import requests

# Example Usage
# CSV Reader
#csv_reader = CSVReader('your_file.csv')
#csv_reader.plot_histogram('column_name')

# API Reader
#api_reader = APIReader('https://api.example.com/data', params={'key': 'value'})
#api_reader.display_info()

# SQL Data Reader
#sql_reader = SQLDataReader('sqlite:///your_database.db', 'SELECT * FROM your_table')
#sql_reader.plot_line('x_column', 'y_column')

class CSVReader(BaseDataReader):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.read_data()

    def read_data(self):
        try:
            self.data = pd.read_csv(self.file_path)
            print("CSV data loaded successfully.")
        except Exception as e:
            print(f"Error reading CSV file: {e}")

class APIReader(BaseDataReader):
    def __init__(self, api_url, params=None, headers=None):
        super().__init__()
        self.api_url = api_url
        self.params = params
        self.headers = headers
        self.fetch_api_data()

    def fetch_api_data(self):
        try:
            response = requests.get(self.api_url, params=self.params, headers=self.headers)
            response.raise_for_status()
            self.data = pd.json_normalize(response.json())
            print("API data fetched successfully.")
        except Exception as e:
            print(f"Error fetching data from the API: {e}")

class SQLDataReader(BaseDataReader):
    def __init__(self, db_url, sql_query):
        super().__init__()
        self.db_url = db_url
        self.sql_query = sql_query
        self.fetch_sql_data()

    def fetch_sql_data(self):
        try:
            engine = create_engine(self.db_url)
            with engine.connect() as connection:
                self.data = pd.read_sql_query(self.sql_query, connection)
            print("SQL data fetched successfully.")
        except Exception as e:
            print(f"Error fetching data from the database: {e}")
