<div align="center">

# -- ! COVID-19 Data Analysis & Visualization ! --
### *A Notebook-Based COVID-19 Data Analysis & Visualization Toolkit Built with OOP Principles*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Array%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/python/)
[![OOP](https://img.shields.io/badge/Design-OOP%20%2F%20Classes-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

<br/>

> *"A pandemic leaves behind numbers — cases, deaths, recoveries. Analysis is how those numbers become understanding."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧱 Class Design — `CovidDataAnalyzer` & `ChartDispatcher`](#-class-design--coviddataanalyzer--chartdispatcher)
- [🖥️ Example Notebook Output](#️-example-notebook-output)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **COVID-19 Data Analysis & Visualization** project is a Jupyter Notebook that combines **Pandas** and **NumPy** for data manipulation with **Matplotlib**, **Seaborn**, and **Plotly** for visualization — all wrapped inside two encapsulated classes, `CovidDataAnalyzer` and `ChartDispatcher`. It loads a global COVID-19 snapshot, separates country-level records from continent and global aggregate rows, computes death and recovery rates, and generates a full range of static and interactive charts.

This project is designed to:
- Demonstrate how Pandas, NumPy, Matplotlib, Seaborn, and Plotly can be combined inside well-structured classes
- Practice encapsulation and clean method-based data pipelines in Python
- Apply `match`/`case` structural pattern matching for chart dispatching instead of long `if-elif` chains
- Turn a raw country-level dataset into clear, comparable insights across continents

---

## 🎯 Problem Statement

> **Objective:** Analyze the spread of COVID-19 across countries and regions using Pandas for data manipulation, and Matplotlib, Seaborn, and Plotly for visualization, giving hands-on experience handling real-world pandemic data, computing rates, and creating insightful charts that compare outcomes across the globe.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Loading & Cleaning | Core | Load the CSV dataset, fill missing values, and separate aggregate rows from country-level rows |
| Rate Calculation | Core | Compute Death Rate and Recovery Rate per country |
| Continent-Wise Analysis | Core | Group and compare Cases, Deaths, and Recovered totals by continent |
| Top-N Analysis | Core | Rank countries by Cases, Deaths, Death Rate, and Recovery Rate |
| Correlation Analysis | Core | Correlate Cases, Recovered, Deaths, Tests, and Population |
| Static Visualization | Core | Bar charts, scatter plots, pie chart, and correlation heatmap via Matplotlib and Seaborn |
| Interactive Visualization | Core | Treemap, bar chart, and scatter plot via Plotly |
| OOP Design | Structure | Two classes (`CovidDataAnalyzer`, `ChartDispatcher`), each with clearly separated responsibilities |

The goal is to demonstrate a **clean, class-based approach to pandemic data analytics** through a fully documented notebook.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📥 **CSV Dataset Loading** | Load the COVID-19 country-level snapshot dataset into a Pandas DataFrame |
| 🧹 **Missing Data Handling** | Fill missing continent, recovery, death, test, and population values |
| 🧩 **Aggregate Row Separation** | Splits true country-level rows away from continent/global total rows |
| 🧮 **Death & Recovery Rate Calculation** | Adds `DeathRate` and `RecoveryRate` columns for every country |
| 🌍 **Continent-Wise Grouping** | Summarizes total Cases, Deaths, and Recovered by continent |
| 🔝 **Top-N Ranking** | Ranks countries by any metric, with an optional minimum-case filter |
| 📊 **Six+ Chart Types** | Bar, pie, scatter, heatmap, treemap, and interactive scatter charts |
| 🌐 **Interactive Plotly Charts** | Treemap and bar/scatter charts with hover tooltips, zoom, and color scales |
| 🧱 **True OOP Encapsulation** | `CovidDataAnalyzer` owns the data pipeline; `ChartDispatcher` owns chart rendering |
| 🐍 **Modern `match`/`case` Control Flow** | Chart selection in `ChartDispatcher.display_chart()` uses structural pattern matching instead of `if-elif` |

---

## 🏗️ Project Structure

```
📦 covid19-data-analysis/
│
├── 📓 Final_PR-1.ipynb        ← Jupyter Notebook with explanatory markdown cells
├── 📁 data/
│   └── 📄 covid_19.csv        ← COVID-19 country-level snapshot dataset
│
└── 📄 README.md               ← Project documentation
```

---

## 🔄 Project Workflow

```
Notebook Start
      │
      ▼
┌─────────────────────────────┐
│   Load Raw Dataset          │  ← CovidDataAnalyzer.load_data()
└────────────┬────────────────┘
             ▼
┌─────────────────────────────┐
│   Clean & Fill Missing Data │  ← clean_data()
└────────────┬────────────────┘
             ▼
┌─────────────────────────────┐
│   Separate Country-Level    │  ← split_country_level()
│   Rows from Aggregate Rows  │
└────────────┬────────────────┘
             ▼
┌─────────────────────────────┐
│   Add Death & Recovery Rates│  ← add_rate_columns()
└────────────┬────────────────┘
             │
   ┌─────────┼──────────┬───────────────┐
   ▼         ▼          ▼               ▼
┌───────┐ ┌────────┐ ┌─────────┐ ┌─────────────┐
│Global │ │Continent│ │ Top-N   │ │ Correlation │
│Summary│ │ Summary │ │ Ranking │ │  Analysis   │
└───┬───┘ └────┬───┘ └────┬────┘ └──────┬──────┘
    │          │          │             │
    └──────────┴────┬─────┴─────────────┘
                     ▼
┌───────────────────────────────────────────────┐
│   Static Charts (Matplotlib / Seaborn)         │
│   Interactive Charts (Plotly via ChartDispatcher)│
└────────────────────┬────────────────────────────┘
                      ▼
              Key Insights Summary ✅
```

---

## 🧱 Class Design — `CovidDataAnalyzer` & `ChartDispatcher`

The notebook is built around two encapsulated classes:

```python
class CovidDataAnalyzer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.raw_df = None
        self.df = None
        self.country_df = None

    def load_data(self):
        self.raw_df = pd.read_csv(self.filepath)
        self.df = self.raw_df.copy()
        return self.df
```

```python
class ChartDispatcher:
    def __init__(self, country_df, continent_df):
        self.country_df = country_df
        self.continent_df = continent_df

    def display_chart(self, chart_type):
        match chart_type:
            case "top_cases":
                ...
            case "top_deaths":
                ...
            case "continent_pie":
                ...
            case "recovery_vs_death":
                ...
            case _:
                print(f"No chart available for '{chart_type}'")
```

| Concept | Where it's used |
|---------|-----------------|
| 🏗️ **Constructor** | `__init__` initializes the file path and empty DataFrame state in both classes |
| 🔒 **Encapsulation** | `self.df` and `self.country_df` are managed entirely through class methods |
| 🧩 **Single Responsibility** | `CovidDataAnalyzer` handles data loading, cleaning, and aggregation; `ChartDispatcher` handles rendering only |
| 🐍 **`match` / `case`** | `ChartDispatcher.display_chart()` uses structural pattern matching to select between chart types instead of `if-elif` |
| 🧮 **Method Coverage** | `load_data`, `clean_data`, `split_country_level`, `add_rate_columns`, `global_summary`, `continent_summary`, `top_n`, `display_chart` |

---

## 🖥️ Example Notebook Output

```
Missing values before cleaning
country         0
continent       2
population      9
Cases           0
Recovered      48
Deaths          5
Tests          25
dtype: int64

Country-level records: 229

Total Countries: 229
Total Cases: 704,753,169
Total Deaths: 7,010,666
Total Recovered: 560,566,960
Global Death Rate (%): 0.99

Top 10 Countries by Cases
   country      Cases
0      USA  111820082
1    India   45035393
2   France   40138560
3  Germany   38828995
4   Brazil   38743918
...

>>> dispatcher.display_chart("continent_pie")
[Pie chart of global case share by continent is displayed]
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.10+ | Core programming language (required for `match`/`case`) |
| 🐼 **Pandas** | Latest | Data loading, cleaning, aggregation, and rate calculation |
| 🔢 **NumPy** | Latest | Supporting numerical operations |
| 📊 **Matplotlib** | Latest | Bar charts, scatter plots, and pie chart |
| 🎨 **Seaborn** | Latest | Statistical bar/scatter plots and correlation heatmap |
| 🌐 **Plotly** | Latest | Interactive treemap, bar chart, and scatter plot |
| 🐍 **`match` / `case`** | Python 3.10+ | Structural pattern matching for chart dispatch logic |
| 🧱 **OOP** | Built-in | Two-class design with clear separation of data and visualization logic |
| 📓 **Jupyter Notebook** | Latest | Interactive, documented execution environment |

---

## 📈 Results & Insights

Running the notebook produces:

- ✅ **Full Data Lifecycle** — load, clean, split, and analyze a global COVID-19 snapshot end-to-end
- 🌍 **Continent-Level Comparison** — Europe and Asia account for the largest share of global cases, followed by North America
- 🏆 **Top-N Rankings** — USA, India, and France lead in total cases; USA, Brazil, and India lead in total deaths
- 🧮 **Reliable Rate Calculations** — Death Rate and Recovery Rate computed per country, filtered to avoid misleading results from low-case countries
- 📊 **Six Working Chart Types** — bar, pie, scatter, heatmap (static) plus treemap and scatter (interactive)
- 🌐 **Interactive Exploration** — Plotly charts allow hovering over individual countries to inspect exact figures
- 📉 **Global Death Rate** — works out to just under **1%** across all countries in the dataset, with wide variation by country

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🧱 **Clean OOP Design** | Data pipeline and chart rendering are cleanly separated into two focused classes |
| 🐍 **Modern Python Syntax** | `match`/`case` used for chart dispatch instead of nested `if-elif` chains |
| 📚 **Educational** | Great reference for combining Pandas, Matplotlib, Seaborn, and Plotly inside one workflow |
| 🌐 **Static + Interactive** | Covers both publication-style static charts and explorable interactive charts |
| 🖥️ **Minimal Dependencies** | Just Pandas, NumPy, Matplotlib, Seaborn, and Plotly — no heavyweight frameworks |
| 🧪 **Extensible** | Easy to add new chart types to `ChartDispatcher` or new metrics to `CovidDataAnalyzer` |
| 🛡️ **Data Safety** | Aggregate rows (continent/global totals) are explicitly filtered out before per-country analysis |

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
- 🌐 [Plotly Python Documentation](https://plotly.com/python/) — Official Plotly reference
- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🐍 [Python `match` Statement Docs](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement) — Structural pattern matching reference
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support

---

<div align="center">

---

*Made with ❤️ and Pandas DataFrames — Last updated: 24 July, 2026*

</div>
