import pandas as pd
from src.db_connection import get_mysql_engine

def load_csv_to_mysql(csv_path: str):
    engine = get_mysql_engine()
    print(f"Reading {csv_path}...")
    
    df = pd.read_csv(csv_path)
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
        
    print(f"Loading {len(df)} rows into MySQL table 'raw_rentals'...")
    df.to_sql("raw_rentals", con=engine, if_exists="replace", index=False)
    print("Data ingestion complete!")

if __name__ == "__main__":
    load_csv_to_mysql("data/raw/houserentdhaka.csv")