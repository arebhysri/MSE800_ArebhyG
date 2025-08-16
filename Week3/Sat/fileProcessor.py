import pandas as pd
import numpy as np

class fileProcessor:
    def __init__(self, csv_path, parquet_path):
        self.csv_file = csv_path
        self.parquet_file = parquet_path
        self.df = None

    def load_csv(self):
        #Load CSV into a pandas DataFrame
        print("Loading CSV from: " ,self.csv_file)
        self.df = pd.read_csv(self.csv_file)
        print("Loaded ", len(self.df) , " rows and ",len(self.df.columns)," columns.")

    def save_parquet(self):
        if self.df is None:
            raise ValueError("Data not loaded or enter correct csv file's path")
        print("Saving as Parquet to: ",self.parquet_file)
        self.df.to_parquet(self.parquet_file, engine="pyarrow" ,index=False)
        print("Parquet file saved as " , self.parquet_file)

    def analyze(self):
        print("\n Column Statistics:")
        numeric_df = self.df.select_dtypes(include=[np.number])
        for col in numeric_df.columns:
            max_val = numeric_df[col].max()
            min_val = numeric_df[col].min()
            mean_val = numeric_df[col].mean()
            abs_vals = numeric_df[col].abs().head(5).tolist()
            print(f"\n {col}")
            print(f"   Max: {max_val}")
            print(f"   Min: {min_val}")
            print(f"   Mean: {mean_val:.2f}")
            print(f"   Sample Abs Values: {abs_vals}")

def main():
    csv_path = r"C:\Users\Administrator\Documents\GitHub\MSE800_ArebhyG\Week3\Sat\DARWIN.csv"
         # Replace with your CSV file path
    parquet_path = r"C:\Users\Administrator\Documents\GitHub\MSE800_ArebhyG\Week3\Sat\output.parquet"

    processor = fileProcessor(csv_path, parquet_path)
    processor.load_csv()
    processor.save_parquet()
    processor.analyze()

if __name__ == "__main__":
    main()
