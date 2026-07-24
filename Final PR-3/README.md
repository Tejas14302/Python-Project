<div align="center">

# -- ! Titanic Survival Analysis ! --
### *An Exploratory Data Analysis & Visualization Project Uncovering What Influenced Passenger Survival*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/)

<br/>

> *"Behind every survival statistic on the Titanic is a story of class, gender, and age — and the data still remembers."*

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

The **Titanic Survival Analysis** is a Jupyter Notebook project that explores the classic **Titanic** dataset using **Pandas** for data cleaning and manipulation, and **Matplotlib**/**Seaborn** for visualization. It walks through the full analysis lifecycle — from loading and cleaning the raw passenger data, to labeling survival outcomes and age groups, to visualizing how class, gender, age, and embarkation port relate to a passenger's chances of survival.

This project is designed to:
- Demonstrate how Pandas can be used to clean, impute, and reshape a real-world dataset
- Practice grouping, sorting, and correlation analysis on tabular passenger data
- Apply Python's `match`/`case` structural pattern matching to label survival outcomes and age groups
- Build a clear, step-by-step visual narrative using Matplotlib and Seaborn

---

## 🎯 Problem Statement

> **Objective:** Perform exploratory data analysis (EDA) on the Titanic dataset to understand the factors that influenced passenger survival. Create visualizations to represent survival rates by class, gender, age, and other features.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Loading & Exploration | Core | Load the CSV dataset and inspect shape, dtypes, and summary statistics |
| Data Cleaning | Core | Drop the mostly-empty Cabin column, impute Age with the median, and Embarked with the mode |
| Survival & Age Labeling | Core | Convert raw survival codes and ages into readable categories using `match`/`case` |
| Class & Gender Analysis | Core | Compare survival rates across passenger class, gender, and their combination |
| Age Group Analysis | Core | Compare survival rates across Child, Teenager, Adult, and Senior groups |
| Embarkation Analysis | Core | Compare survival rates across the three ports of embarkation |
| Correlation Analysis | Core | Measure how strongly class, age, siblings/spouses, parents/children, and fare relate to survival |
| Data Visualization | Core | Count plot, bar plots, histogram, and a correlation heatmap |

The goal is to demonstrate a **clean, structured approach to exploratory data analysis** using a real-world survival dataset.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📥 **CSV Dataset Loading** | Loads the Titanic passenger dataset with Pandas |
| 🔍 **Data Exploration** | Shape, dtypes, `describe()`, and missing value checks |
| 🧹 **Missing Value Handling** | Cabin dropped, Age filled with median, Embarked filled with mode |
| 🐍 **`match`/`case` Labeling** | Survival coded as `Survived` / `Did Not Survive`, and age bucketed into Child / Teenager / Adult / Senior |
| 🚢 **Class-Based Analysis** | Survival rate compared across 1st, 2nd, and 3rd passenger class |
| 🚻 **Gender-Based Analysis** | Survival rate compared between male and female passengers |
| 👶 **Age Group Analysis** | Survival rate compared across age categories |
| ⚓ **Embarkation Analysis** | Survival rate compared across Cherbourg, Queenstown, and Southampton |
| 🔗 **Correlation Heatmap** | Shows how class, age, family size, and fare relate to survival |
| 📊 **Combined Visualizations** | Class-and-gender combined bar plot and a stacked age/survival histogram |
| 📝 **Narrative Markdown Cells** | Every section explained in plain language alongside the code |

---

## 🏗️ Project Structure

```
📦 titanic-survival-analysis/
│
├── 📓 Final_PR-3.ipynb        ← Jupyter Notebook with full EDA and visualizations
├── 📄 Titanic-Dataset.csv     ← Titanic passenger dataset
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
│ Load Titanic-Dataset.csv      │
└────────────┬──────────────────┘
             │
             ▼
┌───────────────────────────────┐
│ Explore Data                  │  ← shape, info, describe, null check
└────────────┬──────────────────┘
             │
             ▼
┌───────────────────────────────┐
│ Clean Data                    │  ← drop Cabin, fill Age/Embarked
└────────────┬──────────────────┘
             │
             ▼
┌───────────────────────────────┐
│ Label Survival & Age Groups    │  ← match/case labeling
└────────────┬──────────────────┘
             │
   ┌─────────┼───────────┬───────────┐
   ▼         ▼           ▼           ▼
┌───────┐ ┌────────┐ ┌────────┐ ┌───────────┐
│ Class │ │ Gender │ │  Age   │ │Embarkation│
│Survival│ │Survival│ │Survival│ │ Survival  │
└───┬───┘ └───┬────┘ └───┬────┘ └─────┬─────┘
    │         │          │            │
    ▼         ▼          ▼            ▼
┌─────────────────────────────────────────┐
│  Combined Plots & Correlation Heatmap    │
└────────────────────┬─────────────────────┘
                      │
                      ▼
                Conclusion ✅
```

---

## 🧱 Notebook Design — Analysis Steps

The notebook follows a clear, linear analysis flow from raw data to insight:

```python
def survival_label(value):
    match value:
        case 1:
            return 'Survived'
        case 0:
            return 'Did Not Survive'
        case _:
            return 'Unknown'

def age_group(age):
    match age:
        case a if a < 13:
            return 'Child'
        case a if a < 20:
            return 'Teenager'
        case a if a < 60:
            return 'Adult'
        case _:
            return 'Senior'
```

| Concept | Where it's used |
|---------|-----------------|
| 📥 **Data Loading** | `pd.read_csv('Titanic-Dataset.csv')` |
| 🧹 **Cleaning** | `df.drop(columns=['Cabin'])`, `fillna()` with median/mode, `df.duplicated().sum()` |
| 🐍 **`match` / `case`** | `survival_label()` and `age_group()` convert raw values into readable categories |
| 📊 **Grouping** | `df.groupby('Pclass' / 'Sex' / 'Age_Group' / 'Embarked')['Survived'].mean()` |
| 🔗 **Correlation** | `df[num_cols].corr()` and a Seaborn heatmap |
| 📈 **Visualization** | Count plot, bar plots, stacked histogram, and combined class/gender bar plot |

---

## 🖥️ Example Output

```
df.head()

   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S

df['Survival_Status'].value_counts()

Survival_Status
Did Not Survive    549
Survived           342
Name: count, dtype: int64

df.groupby('Sex')['Survived'].mean()

Sex
female    0.742038
male      0.188908
Name: Survived, dtype: float64

df.groupby('Pclass')['Survived'].mean()

Pclass
1    0.629630
2    0.472826
3    0.242363
Name: Survived, dtype: float64
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.10+ | Core programming language (required for `match`/`case`) |
| 🐼 **Pandas** | Latest | Data loading, cleaning, imputation, and grouping |
| 📊 **Matplotlib** | Latest | Figure sizing, labeling, and layout |
| 🎨 **Seaborn** | Latest | Count plot, bar plots, histogram, and heatmap |
| 📓 **Jupyter Notebook** | Latest | Interactive analysis environment with markdown narration |
| 🐍 **`match` / `case`** | Python 3.10+ | Structural pattern matching for survival and age-group labeling |

---

## 📈 Results & Insights

Running the notebook produces:

- ✅ **Clean Dataset** — Cabin dropped, Age imputed with the median, Embarked imputed with the mode, no duplicates found
- 🚻 **Gender Was Decisive** — women survived at roughly 74%, compared to about 19% for men
- 🚢 **Class Mattered** — 1st class passengers survived at nearly 63%, versus about 24% for 3rd class
- 👶 **Age Played a Role** — children had the highest survival rate among all age groups
- ⚓ **Embarkation Differences** — passengers who boarded at Cherbourg survived at a higher rate than those from Southampton or Queenstown
- 🔗 **Fare and Class Linked** — fare correlates negatively with class number, reflecting that higher fares bought better cabins and easier lifeboat access
- 📊 **Six Visualizations** — a count plot, four bar plots, a stacked histogram, and a correlation heatmap
- 📝 **Clear Narrative** — every step explained in plain language between code cells

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🧹 **Thoughtful Cleaning** | Missing values handled with sensible, column-specific strategies rather than a blanket drop |
| 🐍 **Modern Python Syntax** | `match`/`case` used for survival and age-group labeling instead of nested `if-elif` |
| 📚 **Educational** | Clear reference for combining Pandas grouping with Seaborn visualization |
| 📓 **Notebook Ready** | Fully annotated `.ipynb` with markdown explanations at every step |
| 🖥️ **Minimal Dependencies** | Just Pandas, Matplotlib, and Seaborn — no heavyweight frameworks |
| 🧪 **Extensible** | Easy to add new features (like title extracted from Name) or test additional survival factors |

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
- 🚢 [Titanic Dataset (Kaggle)](https://www.kaggle.com/) — Source dataset for this analysis
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support

---

<div align="center">

---

*Made with ❤️ and Pandas DataFrames — Last updated: 24 July, 2026*

</div>
