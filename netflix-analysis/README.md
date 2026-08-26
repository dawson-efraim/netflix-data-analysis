# 📊 Netflix Data Analysis — Portfolio Project

Exploratory data analysis of **6,234+ titles** from the public Kaggle
`netflix_titles.csv` dataset, using **pandas** and **matplotlib**.

## Quick Start

```bash
pip install pandas matplotlib
python main.py
```

Charts are saved to `charts/` as PNGs and displayed interactively.

## Questions Answered

1. Movies vs TV Shows — what's the split?
2. How has content added to Netflix grown year over year?
3. Which countries produce the most Netflix content?
4. What are the most common genres?
5. How long is a typical Netflix movie?
6. Which ratings dominate the catalog?
7. Which months see the most new content?

## Project Structure

```
netflix-analysis/
├── netflix_titles.csv   # dataset (Kaggle: shivamb/netflix-shows)
├── data_loader.py       # load + clean + feature engineering
├── charts.py            # visualization functions (one per question)
├── main.py              # runs summary stats + all charts
└── charts/              # generated PNGs
```

## Key Techniques Demonstrated

- `pd.read_csv`, datetime parsing (`pd.to_datetime`)
- Missing-data handling (`fillna`, `errors="coerce"`)
- Regex feature extraction (`str.extract`) for durations
- `value_counts`, `groupby`, `pivot_table`
- Matplotlib styling: pie/bar/hist/line charts, annotations, dark theme

---
*Dataset: [Netflix Shows on Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)*
