"""Charts for the Netflix catalog analysis. Each saves a PNG into charts/."""
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use("dark_background")
NETFLIX_RED = "#E50914"
GOLD = "#f5c518"


def _save(fig, name: str):
    fig.tight_layout()
    fig.savefig(f"charts/{name}.png", dpi=150, bbox_inches="tight")
    plt.show()


def chart_movies_vs_shows(df: pd.DataFrame):
    counts = df["type"].value_counts()
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.pie(counts, labels=counts.index, autopct="%1.1f%%",
           colors=[NETFLIX_RED, GOLD], startangle=90,
           wedgeprops={"edgecolor": "black"})
    ax.set_title(f"Movies vs TV Shows ({len(df):,} titles)", fontsize=14)
    _save(fig, "movies_vs_shows")


def chart_content_by_year(df: pd.DataFrame):
    recent = df[df["year_added"].notna() & (df["year_added"] >= 2015)]
    pivot = recent.pivot_table(index="year_added", columns="type",
                               values="show_id", aggfunc="count")
    fig, ax = plt.subplots(figsize=(10, 5))
    pivot.plot(kind="bar", ax=ax, color=[NETFLIX_RED, GOLD])
    ax.set_title("Content Added to Netflix by Year", fontsize=14)
    ax.set_xlabel("Year Added")
    ax.set_ylabel("Titles")
    ax.legend(title=None)
    plt.xticks(rotation=0)
    _save(fig, "content_by_year")


def chart_top_countries(df: pd.DataFrame, n: int = 10):
    top = df[df["main_country"] != "Unknown"]["main_country"].value_counts().head(n)
    fig, ax = plt.subplots(figsize=(10, 5))
    top[::-1].plot(kind="barh", ax=ax, color=NETFLIX_RED)
    ax.set_title(f"Top {n} Countries Producing Netflix Content", fontsize=14)
    ax.set_xlabel("Titles")
    _save(fig, "top_countries")


def chart_top_genres(df: pd.DataFrame, n: int = 10):
    top = df["main_genre"].value_counts().head(n)
    fig, ax = plt.subplots(figsize=(10, 5))
    top[::-1].plot(kind="barh", ax=ax, color=GOLD)
    ax.set_title(f"Top {n} Genres on Netflix", fontsize=14)
    ax.set_xlabel("Titles")
    _save(fig, "top_genres")


def chart_movie_durations(df: pd.DataFrame):
    movies = df[(df["type"] == "Movie") & df["duration_num"].notna()]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(movies["duration_num"], bins=40, color=NETFLIX_RED, edgecolor="black")
    mean_min = movies["duration_num"].mean()
    ax.axvline(mean_min, color=GOLD, linestyle="--", linewidth=2,
               label=f"Average: {mean_min:.0f} min")
    ax.set_title("Movie Duration Distribution", fontsize=14)
    ax.set_xlabel("Minutes")
    ax.set_ylabel("Number of Movies")
    ax.legend()
    _save(fig, "movie_durations")


def chart_ratings(df: pd.DataFrame):
    counts = df["rating"].value_counts().head(8)
    fig, ax = plt.subplots(figsize=(10, 5))
    counts.plot(kind="bar", ax=ax, color=NETFLIX_RED)
    ax.set_title("Most Common Content Ratings", fontsize=14)
    ax.set_xlabel("Rating")
    ax.set_ylabel("Titles")
    plt.xticks(rotation=45)
    _save(fig, "ratings")


def chart_monthly_additions(df: pd.DataFrame):
    order = ["January", "February", "March", "April", "May", "June", "July",
             "August", "September", "October", "November", "December"]
    per_month = df["month_added"].value_counts().reindex(order)
    fig, ax = plt.subplots(figsize=(10, 5))
    per_month.plot(ax=ax, marker="o", color=NETFLIX_RED, linewidth=2)
    best = per_month.idxmax()
    ax.annotate(f"Peak: {best}", xy=(order.index(best), per_month.max()),
                xytext=(0.15, 0.9), textcoords="axes fraction", color=GOLD)
    ax.set_title("When Does Netflix Add the Most Content?", fontsize=14)
    ax.set_ylabel("Titles Added")
    plt.xticks(rotation=45)
    _save(fig, "monthly_additions")
