<div align="center">

# -- ! Global Happiness Report Analysis ! --
### *An Exploratory Data Analysis & Visualization Project Uncovering What Drives National Happiness*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/)

<br/>

> *"Happiness isn't random — it leaves fingerprints in the data, from GDP to good health to who you can lean on."*

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

The **Global Happiness Report Analysis** is a Jupyter Notebook project that explores the 2015 **World Happiness Report** dataset using **Pandas** for data cleaning and manipulation, and **Matplotlib**/**Seaborn** for visualization. It walks through the full analysis lifecycle — from loading and cleaning the raw data, to categorizing countries by happiness level, to visualizing how GDP per capita, social support, and life expectancy relate to a country's overall happiness score.

This project is designed to:
- Demonstrate how Pandas can be used to clean, rename, and reshape a real-world dataset
- Practice grouping, sorting, and correlation analysis on tabular data
- Apply Python's `match`/`case` structural pattern matching to bucket countries into happiness levels
- Build a clear, step-by-step visual narrative using Matplotlib and Seaborn

---

## 🎯 Problem Statement

> **Objective:** Analyze the World Happiness Report data to understand what factors contribute to happiness in different countries. Visualize correlations between happiness scores and variables such as GDP per capita, social support, and life expectancy.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Loading & Exploration | Core | Load the CSV dataset and inspect shape, dtypes, and summary statistics |
| Data Cleaning | Core | Check for missing/duplicate values and rename columns for clarity |
| Happiness Categorization | Core | Bucket each country into a happiness level using `match`/`case` |
| Ranking & Comparison | Core | Identify the top and bottom countries by happiness score |
| Regional Analysis | Core | Compare average happiness score across world regions |
| Correlation Analysis | Core | Measure how strongly GDP, family, health, freedom, trust, and generosity relate to happiness |
| Data Visualization | Core | Bar chart, heatmap, scatter plots, and a pairplot |

The goal is to demonstrate a **clean, structured approach to exploratory data analysis** using a real-world happiness dataset.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📥 **CSV Dataset Loading** | Loads the 2015 World Happiness Report dataset with Pandas |
| 🔍 **Data Exploration** | Shape, dtypes, `describe()`, and missing value checks |
| 🧹 **Column Renaming** | Long column names simplified for readability (`GDP_per_Capita`, `Life_Expectancy`, etc.) |
| 🐍 **`match`/`case` Categorization** | Countries labeled Very Happy / Happy / Moderate / Low / Very Low based on score |
| 🏅 **Top & Bottom Rankings** | Surfaces the 10 happiest and 10 least happy countries |
| 🌍 **Regional Comparison** | Groups and ranks average happiness score by world region |
| 🔗 **Correlation Heatmap** | Shows how GDP, family, health, freedom, trust, and generosity relate to happiness |
| 📊 **Scatter Plots** | Happiness Score vs GDP per Capita, Social Support, and Life Expectancy |
| 🧩 **Pairplot** | Visualizes relationships across all key factors at once |
| 📝 **Narrative Markdown Cells** | Every section explained in plain language alongside the code |

---

## 🏗️ Project Structure

```
📦 global-happiness-analysis/
│
├── 📓 Final_PR-1.ipynb        ← Jupyter Notebook with full EDA and visualizations
├── 📄 2015.csv                ← World Happiness Report dataset (2015)
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
│   Load 2015.csv with Pandas │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Explore Data               │  ← shape, info, describe, null check
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Clean & Rename Columns     │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Categorize Happiness Level │  ← match/case buckets
└────────────┬────────────────┘
             │
   ┌─────────┼─────────────┐
   ▼         ▼             ▼
┌───────┐ ┌────────┐ ┌────────────┐
│ Top/  │ │Regional│ │ Correlation │
│Bottom │ │Average │ │  Heatmap    │
└───┬───┘ └───┬────┘ └──────┬─────┘
    │         │             │
    ▼         ▼             ▼
┌───────────────────────────────────┐
│  Scatter Plots & Pairplot         │
└────────────────┬───────────────────┘
                  │
                  ▼
            Conclusion ✅
```

---

## 🧱 Notebook Design — Analysis Steps

The notebook follows a clear, linear analysis flow from raw data to insight:

```python
def happiness_level(score):
    match score:
        case s if s >= 7:
            return 'Very Happy'
        case s if s >= 6:
            return 'Happy'
        case s if s >= 5:
            return 'Moderate'
        case s if s >= 4:
            return 'Low'
        case _:
            return 'Very Low'
```

| Concept | Where it's used |
|---------|-----------------|
| 📥 **Data Loading** | `pd.read_csv('2015.csv')` |
| 🧹 **Cleaning** | `df.rename()`, `df.isnull().sum()`, `df.duplicated().sum()` |
| 🐍 **`match` / `case`** | `happiness_level()` buckets each country's score into a category |
| 📊 **Grouping** | `df.groupby('Region')['Happiness_Score'].mean()` for regional comparison |
| 🔗 **Correlation** | `df[cols].corr()` and a Seaborn heatmap |
| 📈 **Visualization** | Bar chart, heatmap, scatter plots, and `sns.pairplot()` |

---

## 🖥️ Example Output

```
df.head()

       Country         Region  Happiness Rank  Happiness Score  ...
0  Switzerland  Western Europe               1            7.587  ...
1      Iceland  Western Europe               2            7.561  ...
2      Denmark  Western Europe               3            7.527  ...

df['Happiness_Level'].value_counts()

Happiness_Level
Moderate      49
Low           44
Happy         29
Very Low      21
Very Happy    15
Name: count, dtype: int64

region_avg = df.groupby('Region')['Happiness_Score'].mean().sort_values(ascending=False)

Region
Australia and New Zealand    7.285000
North America                7.273000
Western Europe                6.689619
...
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.10+ | Core programming language (required for `match`/`case`) |
| 🐼 **Pandas** | Latest | Data loading, cleaning, renaming, and grouping |
| 📊 **Matplotlib** | Latest | Bar chart and figure sizing/labels |
| 🎨 **Seaborn** | Latest | Heatmap, scatter plots, and pairplot |
| 📓 **Jupyter Notebook** | Latest | Interactive analysis environment with markdown narration |
| 🐍 **`match` / `case`** | Python 3.10+ | Structural pattern matching for happiness-level categorization |

---

## 📈 Results & Insights

Running the notebook produces:

- ✅ **Clean Dataset** — no missing values or duplicates found in the 2015 report
- 🏅 **Clear Rankings** — Switzerland, Iceland, and Denmark top the happiness table; Togo, Burundi, and Syria sit at the bottom
- 🌍 **Regional Patterns** — Australia/New Zealand, North America, and Western Europe lead in average happiness; Sub-Saharan Africa trails
- 🔗 **Strong Correlations** — GDP per capita, family (social support), and life expectancy show the strongest positive relationship with happiness
- 📊 **Five Visualizations** — a regional bar chart, a correlation heatmap, three scatter plots, and a pairplot
- 📝 **Clear Narrative** — every step explained in plain language between code cells

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🧹 **Thoughtful Cleaning** | Columns renamed for readability before any analysis begins |
| 🐍 **Modern Python Syntax** | `match`/`case` used for happiness-level categorization instead of nested `if-elif` |
| 📚 **Educational** | Clear reference for combining Pandas grouping with Seaborn visualization |
| 📓 **Notebook Ready** | Fully annotated `.ipynb` with markdown explanations at every step |
| 🖥️ **Minimal Dependencies** | Just Pandas, Matplotlib, and Seaborn — no heavyweight frameworks |
| 🧪 **Extensible** | Easy to swap in a newer year's report or add more factors to the correlation analysis |

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
- 📊 [Matplotlib Official Documentation](https://matplotlib.org/stable/index.html) — Official Matplotlib reference
- 🎨 [Seaborn Official Documentation](https://seaborn.pydata.org/) — Official Seaborn reference
- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🐍 [Python `match` Statement Docs](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement) — Structural pattern matching reference
- 📊 [World Happiness Report Dataset (Kaggle)](https://www.kaggle.com/) — Source dataset for this analysis
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support

---

<div align="center">

---

*Made with ❤️ and Pandas DataFrames — Last updated: 24 July, 2026*

</div>
