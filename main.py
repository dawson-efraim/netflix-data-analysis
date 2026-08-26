import pandas as pd

import charts
from data_loader import load_data


def print_summary(df: pd.DataFrame):
    print("=" * 55)
    print("NETFLIX CATALOG ANALYSIS")
    print("=" * 55)

    total = len(df)
    movies = (df["type"] == "Movie").sum()
    shows = total - movies
    print(f"\nTotal titles        : {total:,}")
    print(f"Movies              : {movies:,} ({movies / total:.0%})")
    print(f"TV Shows            : {shows:,} ({shows / total:.0%})")

    years = df["release_year"]
    print(f"\nRelease year range  : {int(years.min())} - {int(years.max())}")

    busiest_year = df["year_added"].value_counts().idxmax()
    print(f"Busiest year added  : {int(busiest_year)} "
          f"({df['year_added'].value_counts().max():,} titles)")

    top_country = df[df['main_country'] != 'Unknown']['main_country'].value_counts()
    print(f"Top country         : {top_country.index[0]} ({top_country.iloc[0]:,} titles)")

    avg_movie_len = df.loc[df["type"] == "Movie", "duration_num"].mean()
    print(f"Avg movie length    : {avg_movie_len:.0f} minutes")

    print("\nTop 5 genres:")
    for genre, count in df["main_genre"].value_counts().head(5).items():
        print(f"  {genre:<30} {count:,}")


if __name__ == "__main__":
    df = load_data()

    print_summary(df)

    charts.chart_movies_vs_shows(df)
    charts.chart_content_by_year(df)
    charts.chart_top_countries(df)
    charts.chart_top_genres(df)
    charts.chart_movie_durations(df)
    charts.chart_ratings(df)
    charts.chart_monthly_additions(df)

    print("\nAll charts saved to charts/ ✔")
