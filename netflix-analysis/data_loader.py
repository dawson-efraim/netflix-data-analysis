"""Data loading & cleaning for the Netflix catalog analysis."""
import pandas as pd

CSV_PATH = "netflix_titles.csv"


def load_data(path: str = CSV_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)

    # Parse dates and extract useful columns
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
    df["year_added"] = df["date_added"].dt.year
    df["month_added"] = df["date_added"].dt.month_name()

    # Split duration into value + unit ("90 min" / "2 Seasons")
    duration = df["duration"].str.extract(r"(?P<num>\d+)\s*(?P<unit>min|Season|Seasons)")
    df["duration_num"] = pd.to_numeric(duration["num"], errors="coerce")

    # Primary country / genre (first listed)
    df["main_country"] = df["country"].fillna("Unknown").str.split(",").str[0].str.strip()
    df["main_genre"] = df["listed_in"].str.split(",").str[0].str.strip()

    return df


if __name__ == "__main__":
    df = load_data()
    print(df.shape)
    print(df.isna().sum().sort_values(ascending=False).head())
    print(df.head())
