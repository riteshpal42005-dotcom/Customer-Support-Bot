import pandas as pd

from database.database import engine


def load_data(csv_file: str, table_name: str):
    df = pd.read_csv(csv_file)


    # Basic Cleaning
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    # Remove extra spaces from string columns
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].str.strip()

    df.to_sql(
        table_name,
        con=engine,
        if_exists="append",
        index=False
    )


if __name__ == "__main__":
    load_data("data/registered_users.csv", "registered_users")
    load_data("data/user_policy_details.csv", "policy_details")