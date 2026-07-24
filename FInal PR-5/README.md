<div align="center">

# -- ! Stock Market Analysis ! --
### *An Exploratory Data Analysis & Visualization Project Uncovering Trends in Historical Stock Prices*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Array%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

<br/>

> *"A closing price is just one number — a moving average is the story of where it's been."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧱 Notebook Design — Analysis Steps](#-notebook-design--analysis-steps)
- [🖥️ Example Output](#️-example-output)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Stock Market Analysis** is a Jupyter Notebook project that explores historical daily price data for several major stock market indices using **Pandas** and **NumPy** for data manipulation, and **Matplotlib**/**Seaborn** for visualization. It focuses on a single index — the NYSE Composite (NYA) — cleans and sorts its history, then visualizes moving averages, trading volume, volatility, and yearly trends to understand how the index has performed over time.

This project is designed to:
- Demonstrate how Pandas can be used to filter, sort, and clean a large multi-index time-series dataset
- Practice rolling-window calculations such as moving averages and rolling volatility
- Apply Python's `match`/`case` structural pattern matching to label daily price movement
- Build a clear, step-by-step visual narrative using Matplotlib and Seaborn

---

## 🎯 Problem Statement

> **Objective:** Analyze historical stock market data to identify trends and patterns in stock prices over time. Visualize stock performance against various indicators such as moving averages and trading volume.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Loading & Exploration | Core | Load the CSV dataset and inspect shape, dtypes, and which indices are present |
| Index Filtering | Core | Isolate a single index (NYSE Composite) for focused analysis |
| Data Cleaning | Core | Parse dates, sort chronologically, drop missing values and duplicates |
| Daily Return Labeling | Core | Bucket each trading day into Gain / Loss / Flat using `match`/`case` |
| Moving Averages | Core | Compute 50-day and 200-day moving averages of the closing price |
| Volatility Analysis | Core | Compute a 30-day rolling standard deviation of daily returns |
| Yearly Trend Analysis | Core | Compare average closing price across years |
| Correlation Analysis | Core | Measure how price and volume relate to one another |
| Data Visualization | Core | Line plots, histogram, and a correlation heatmap |

The goal is to demonstrate a **clean, structured approach to time-series exploratory data analysis** using real-world market index data.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📥 **CSV Dataset Loading** | Loads the multi-index historical stock market dataset with Pandas |
| 🔍 **Data Exploration** | Shape, dtypes, and index value counts across all included markets |
| 🎯 **Single-Index Focus** | Filters down to the NYSE Composite (NYA) for a clean, consistent time series |
| 🧹 **Chronological Cleaning** | Dates parsed and sorted, missing values and duplicates removed |
| 🐍 **`match`/`case` Day Labeling** | Each trading day labeled Gain / Loss / Flat based on its daily return |
| 📈 **Moving Averages** | 50-day and 200-day moving averages plotted against the closing price |
| 📊 **Volume Trend** | Trading volume plotted across the full history |
| 🔔 **Return Distribution** | Histogram of daily percentage returns |
| 🌪️ **Rolling Volatility** | 30-day rolling standard deviation of daily returns |
| 📅 **Yearly Trend** | Average closing price tracked year over year |
| 🔗 **Correlation Heatmap** | Relates Open, High, Low, Close, Volume, and Daily Return to one another |
| 📝 **Narrative Markdown Cells** | Every section explained in plain language alongside the code |

---

## 🏗️ Project Structure

```
📦 stock-market-analysis/
│
├── 📓 Final_PR-5.ipynb        ← Jupyter Notebook with full EDA and visualizations
├── 📄 Market.csv              ← Historical daily price dataset for multiple indices
│
└── 📄 README.md               ← Project documentation
```

---

## 🔄 Project Workflow

```
Notebook Start
      │
      ▼
┌───────────────────────────────┐
│ Load Market.csv                │
└────────────┬──────────────────┘
             │
             ▼
┌───────────────────────────────┐
│ Explore Data                   │  ← shape, info, index value counts
└────────────┬──────────────────┘
             │
             ▼
┌───────────────────────────────┐
│ Filter to NYSE Composite (NYA) │
└────────────┬──────────────────┘
             │
             ▼
┌───────────────────────────────┐
│ Clean & Sort by Date           │  ← parse dates, drop NaNs/duplicates
└────────────┬──────────────────┘
             │
             ▼
┌───────────────────────────────┐
│ Label Daily Gain/Loss/Flat     │  ← match/case
└────────────┬──────────────────┘
             │
   ┌─────────┼───────────┬───────────┐
   ▼         ▼           ▼           ▼
┌───────┐ ┌────────┐ ┌────────┐ ┌───────────┐
│Moving │ │ Volume │ │Return  │ │  Rolling  │
│Averages│ │ Trend │ │Histogram│ │Volatility │
└───┬───┘ └───┬────┘ └───┬────┘ └─────┬─────┘
    │         │          │            │
    ▼         ▼          ▼            ▼
┌─────────────────────────────────────────┐
│  Yearly Trend & Correlation Heatmap      │
└────────────────────┬─────────────────────┘
                      │
                      ▼
                Conclusion ✅
```

---

## 🧱 Notebook Design — Analysis Steps

The notebook follows a clear, linear analysis flow from raw multi-index data to a focused single-index trend story:

```python
def day_label(change):
    match change:
        case c if c > 0:
            return 'Gain'
        case c if c < 0:
            return 'Loss'
        case _:
            return 'Flat'
```

| Concept | Where it's used |
|---------|-----------------|
| 📥 **Data Loading** | `pd.read_csv('Market.csv')` |
| 🎯 **Filtering** | `df[df['Index'] == 'NYA'].copy()` |
| 🧹 **Cleaning** | `pd.to_datetime()`, `sort_values('Date')`, `dropna()`, `duplicated().sum()` |
| 🐍 **`match` / `case`** | `day_label()` classifies each day's percentage change into Gain / Loss / Flat |
| 📈 **Rolling Windows** | `rolling(window=50).mean()`, `rolling(window=200).mean()`, `rolling(window=30).std()` |
| 🔗 **Correlation** | `nya[corr_cols].corr()` and a Seaborn heatmap |
| 📊 **Visualization** | Line plots for price/volume/volatility, histogram for returns, heatmap for correlation |

---

## 🖥️ Example Output

```
df['Index'].value_counts()

Index
N225         14500
NYA          13948
IXIC         12690
GSPTSE       10776
...

nya['Day_Type'].value_counts()

Day_Type
Gain    7362
Loss    6500
Flat      69
Name: count, dtype: int64

yearly_avg = nya.groupby('Year')['Close'].mean()

Year
2017    11846.116877
2018    12653.069123
2019    12864.524546
2020    12624.352894
2021    15601.780551
Name: Close, dtype: float64
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.10+ | Core programming language (required for `match`/`case`) |
| 🐼 **Pandas** | Latest | Data loading, filtering, cleaning, and rolling-window calculations |
| 🔢 **NumPy** | Latest | Underlying numerical operations for rolling statistics |
| 📊 **Matplotlib** | Latest | Line plots for price, volume, and volatility trends |
| 🎨 **Seaborn** | Latest | Return distribution histogram and correlation heatmap |
| 📓 **Jupyter Notebook** | Latest | Interactive analysis environment with markdown narration |
| 🐍 **`match` / `case`** | Python 3.10+ | Structural pattern matching for daily Gain/Loss/Flat labeling |

---

## 📈 Results & Insights

Running the notebook produces:

- ✅ **Clean Single-Index Series** — NYSE Composite data parsed, sorted, and cleaned of missing values and duplicates
- 📈 **Clear Long-Term Uptrend** — the 50-day and 200-day moving averages smooth out daily noise to reveal a persistent upward trend
- 🔀 **Moving Average Crossovers** — periods where the 50-day average dips below the 200-day average line up with known market downturns
- 🌪️ **Volatility Spikes** — the 30-day rolling volatility plot shows clear spikes during major market events
- 🔔 **Symmetric Daily Returns** — daily returns are heavily concentrated around zero with a roughly symmetric distribution, typical of index-level data
- 🔗 **Weak Price-Volume Link** — price and volume show no strong direct correlation, since volume spikes independently of price direction
- 📅 **Rising Yearly Averages** — average yearly closing price trends upward across most of the recent decade

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎯 **Focused Scope** | Filters a large multi-index dataset down to one clean, consistent time series before analysis |
| 🐍 **Modern Python Syntax** | `match`/`case` used for daily return labeling instead of nested `if-elif` |
| 📚 **Educational** | Clear reference for rolling-window techniques like moving averages and rolling volatility |
| 📓 **Notebook Ready** | Fully annotated `.ipynb` with markdown explanations at every step |
| 🖥️ **Minimal Dependencies** | Just Pandas, NumPy, Matplotlib, and Seaborn — no heavyweight frameworks |
| 🧪 **Extensible** | Easy to swap in a different index or add additional technical indicators |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 👤 Author

<div align="center">

### Tejas Varma

[![GitHub](https://img.shields.io/badge/GitHub-Tejas14302-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Tejas14302)

> *"Every insight starts with a single row of data — just like every program starts with a single line."*

**🎓 Role:** Python Developer | Programming Enthusiast \
**📍 Location:** Surat, India \
**🛠️ Skills:** Python · Pandas · NumPy · Matplotlib · Seaborn · Object-Oriented Programming · CLI Applications

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Pandas Official Documentation](https://pandas.pydata.org/docs/) — Official Pandas reference
- 📚 [NumPy Official Documentation](https://numpy.org/doc/stable/) — Official NumPy reference
- 📊 [Matplotlib Official Documentation](https://matplotlib.org/stable/index.html) — Official Matplotlib reference
- 🎨 [Seaborn Official Documentation](https://seaborn.pydata.org/) — Official Seaborn reference
- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🐍 [Python `match` Statement Docs](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement) — Structural pattern matching reference
- 📈 [Historical Stock Market Index Data](https://finance.yahoo.com/) — Source dataset for this analysis
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support

---

<div align="center">

---

*Made with ❤️ and Pandas DataFrames — Last updated: 24 July, 2026*

</div>
