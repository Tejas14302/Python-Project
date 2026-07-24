<div align="center">

# -- ! Air Quality Analysis ! --
### *An OOP-Driven Exploratory Analysis of Urban Air Pollution & Weather Patterns*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Array%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![OOP](https://img.shields.io/badge/Design-OOP%20%2F%20Classes-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

<br/>

> *"The air tells time too — you just have to average it by the hour to hear it."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧱 Class Design — `AirQualityAnalyzer`](#-class-design--airqualityanalyzer)
- [🖥️ Example Output](#️-example-output)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Air Quality Analysis** project explores hourly air quality sensor readings using **Pandas** and **NumPy** for data cleaning and feature engineering, and **Matplotlib**/**Seaborn** for visualization — all wrapped inside an encapsulated `AirQualityAnalyzer` class. It loads the raw sensor export, fixes its quirks (sentinel missing values, stray trailing columns, blank rows), engineers time-based features, and then visualizes how pollutant concentrations vary by hour, day type, month, and weather condition.

This project is designed to:
- Demonstrate how Pandas and NumPy can be combined inside a well-structured class for a real-world sensor dataset
- Practice handling sentinel missing values (`-200`), interpolation, and datetime feature engineering
- Apply `match`/`case` structural pattern matching for day-type and air-quality-category classification
- Build a clear, step-by-step visual narrative using Matplotlib and Seaborn

---

## 🎯 Problem Statement

> **Objective:** Analyze historical air quality sensor data to identify pollution trends and patterns over time. Visualize how pollutant concentrations relate to time of day, day of week, month, and weather conditions such as temperature and humidity.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Loading & Exploration | Core | Load the raw sensor CSV and inspect its shape and structure |
| Data Cleaning | Core | Drop empty trailing columns, drop blank rows, convert `-200` sentinels to `NaN`, drop the mostly-empty `NMHC(GT)` column |
| Missing Value Handling | Core | Fill remaining gaps using time-based interpolation |
| Feature Engineering | Core | Build a proper `Datetime` column and derive `Hour`, `Month`, and `DayOfWeek` |
| Day-Type Classification | Core | Label each day as Weekday or Weekend using `match`/`case` |
| Air Quality Classification | Core | Bucket CO readings into Good / Moderate / Poor / Severe using `match`/`case` |
| Correlation & Weather Analysis | Core | Relate pollutant levels to temperature and humidity |
| Data Visualization | Core | Line plots, box plot, scatter plots, bar chart, and a correlation heatmap |
| OOP Design | Structure | Encapsulated `AirQualityAnalyzer` class managing load/clean/feature-engineering state |

The goal is to demonstrate a **clean, class-based approach to air quality analytics** through structured, hourly sensor data.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📥 **CSV Dataset Loading** | Loads the raw air quality sensor export inside the analyzer class |
| 🧹 **Sentinel Value Handling** | Converts `-200` placeholder readings into proper `NaN` values |
| 🗑️ **Structural Cleanup** | Drops empty trailing columns, fully blank rows, and the mostly-missing `NMHC(GT)` column |
| 🔧 **Time-Based Interpolation** | Fills remaining gaps using `interpolate(limit_direction="both")` |
| 🕒 **Datetime Feature Engineering** | Combines `Date` and `Time` into a `Datetime` column, then derives `Hour`, `Month`, and `DayOfWeek` |
| 🐍 **`match`/`case` Day Typing** | Maps each day name to Weekday or Weekend |
| 🐍 **`match`/`case` Air Quality Grading** | Buckets CO readings into Good / Moderate / Poor / Severe |
| 📈 **Trend Visualizations** | Daily CO trend, hourly pollutant pattern, and monthly pollutant trend |
| 📦 **Weekday vs Weekend Comparison** | Box plot comparing CO concentration across day types |
| 🔗 **Correlation Heatmap** | Relates pollutants to temperature, relative humidity, and absolute humidity |
| 📊 **Scatter Plots** | Temperature vs CO and Relative Humidity vs NO2 |
| 🧱 **True OOP Encapsulation** | Load, clean, datetime-build, and fill-missing logic isolated inside class methods |

---

## 🏗️ Project Structure

```
📦 air-quality-analysis/
│
├── 📓 Final_PR-4.ipynb        ← Jupyter Notebook with full EDA and visualizations
├── 📄 Air_Quality.csv         ← Hourly air quality sensor dataset
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
│ Load Air_Quality.csv          │  ← AirQualityAnalyzer.load_data()
└────────────┬──────────────────┘
             │
             ▼
┌───────────────────────────────┐
│ Clean Data                    │  ← drop empty cols/rows, -200 → NaN, drop NMHC(GT)
└────────────┬──────────────────┘
             │
             ▼
┌───────────────────────────────┐
│ Build Datetime Features       │  ← Hour, Month, DayOfWeek
└────────────┬──────────────────┘
             │
             ▼
┌───────────────────────────────┐
│ Fill Missing (Interpolation)  │
└────────────┬──────────────────┘
             │
   ┌─────────┼───────────┬───────────┐
   ▼         ▼           ▼           ▼
┌───────┐ ┌────────┐ ┌────────┐ ┌───────────┐
│ Daily │ │ Hourly │ │Monthly │ │ Weekday / │
│  CO   │ │Pattern │ │ Trend  │ │ Weekend   │
└───┬───┘ └───┬────┘ └───┬────┘ └─────┬─────┘
    │         │          │            │
    ▼         ▼          ▼            ▼
┌─────────────────────────────────────────┐
│  Weather Correlation & Scatter Plots     │
└────────────────────┬─────────────────────┘
                      │
                      ▼
       Air Quality Classification (Good→Severe) ✅
```

---

## 🧱 Class Design — `AirQualityAnalyzer`

The entire toolkit is built around one encapsulated class:

```python
class AirQualityAnalyzer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.raw_df = None
        self.df = None

    def load_data(self):
        self.raw_df = pd.read_csv(self.filepath)
        self.df = self.raw_df.copy()
        return self.df

    def clean_data(self):
        self.df = self.df.drop(columns=["Unnamed: 15", "Unnamed: 16"], errors="ignore")
        self.df = self.df.dropna(how="all")
        self.df = self.df.replace(-200, np.nan)
        self.df = self.df.drop(columns=["NMHC(GT)"])
        return self.df

    def build_datetime(self):
        self.df["Datetime"] = pd.to_datetime(self.df["Date"] + " " + self.df["Time"], format="%d/%m/%Y %H:%M:%S")
        self.df["Hour"] = self.df["Datetime"].dt.hour
        self.df["Month"] = self.df["Datetime"].dt.month
        self.df["DayOfWeek"] = self.df["Datetime"].dt.day_name()
        return self.df

    def fill_missing(self):
        numeric_columns = self.df.select_dtypes(include="number").columns
        self.df[numeric_columns] = self.df[numeric_columns].interpolate(limit_direction="both")
        return self.df
```

| Concept | Where it's used |
|---------|-----------------|
| 🏗️ **Constructor** | `__init__` stores the file path and initializes empty raw/clean DataFrames |
| 🔒 **Encapsulation** | `self.df` is progressively transformed through dedicated class methods |
| 🐍 **`match` / `case`** | `classify_day_type()` and `classify_air_quality()` use structural pattern matching instead of `if-elif` chains |
| 🧩 **Method Coverage** | `load_data`, `clean_data`, `build_datetime`, `fill_missing` |
| 🕒 **Feature Engineering** | `build_datetime()` derives `Hour`, `Month`, and `DayOfWeek` from combined `Date`/`Time` strings |

---

## 🖥️ Example Output

```
analyzer = AirQualityAnalyzer("Air_Quality.csv")
raw_data = analyzer.load_data()
raw_data.shape
(9471, 17)

clean_data = analyzer.clean_data()
Missing values after replacing -200 with NaN
CO(GT)      1683
NOx(GT)     1639
NO2(GT)     1642
...

category_counts = clean_data["AirQualityCategory"].value_counts().reindex(
    ["Good", "Moderate", "Poor", "Severe"]
)

AirQualityCategory
Good         ...
Moderate     ...
Poor         ...
Severe       ...
Name: count, dtype: int64
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.10+ | Core programming language (required for `match`/`case`) |
| 🐼 **Pandas** | Latest | Data loading, cleaning, interpolation, and datetime feature engineering |
| 🔢 **NumPy** | Latest | Sentinel value replacement (`-200` → `NaN`) |
| 📊 **Matplotlib** | Latest | Trend line plots and figure styling |
| 🎨 **Seaborn** | Latest | Box plot, bar chart, scatter plots, and heatmap |
| 📓 **Jupyter Notebook** | Latest | Interactive analysis environment with markdown narration |
| 🐍 **`match` / `case`** | Python 3.10+ | Structural pattern matching for day-type and air-quality classification |
| 🧱 **OOP** | Built-in | `AirQualityAnalyzer` class encapsulating the cleaning and feature-engineering pipeline |

---

## 📈 Results & Insights

Running the notebook produces:

- ✅ **Fixed Sensor Quirks** — trailing empty columns and blank rows removed, `-200` sentinels converted to proper missing values, and the mostly-empty `NMHC(GT)` column dropped
- 🕒 **Clear Daily Rhythm** — CO, NOx, NO2, and Benzene all peak during morning and evening traffic hours and dip overnight
- 📅 **Weekday vs Weekend Gap** — pollution levels run noticeably higher on weekdays than weekends, consistent with reduced weekend traffic
- 🌡️ **Weak Temperature Link to CO** — temperature shows almost no direct correlation with CO, but a clearer negative correlation with NOx and NO2
- 💧 **Humidity vs NO2** — a weak negative relationship between relative humidity and NO2 concentration
- 🔗 **Pollutants Move Together** — CO, NOx, NO2, and Benzene are all strongly positively correlated, reflecting a shared traffic/combustion source
- 🚦 **Air Quality Breakdown** — Poor is the largest CO-based category, closely followed by Moderate, with Good less common and Severe the smallest share

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🧱 **True OOP Design** | Load, clean, datetime-build, and fill-missing logic cleanly separated into class methods |
| 🐍 **Modern Python Syntax** | `match`/`case` used for day-type and air-quality classification instead of nested `if-elif` |
| 🧹 **Realistic Data Cleaning** | Handles the exact quirks of real sensor exports — sentinel values, stray columns, blank rows |
| 📚 **Educational** | Clear reference for combining Pandas, NumPy, and Matplotlib inside one class |
| 📓 **Notebook Ready** | Fully annotated `.ipynb` with markdown explanations at every step |
| 🖥️ **Minimal Dependencies** | Just Pandas, NumPy, Matplotlib, and Seaborn — no heavyweight frameworks |
| 🧪 **Extensible** | Easy to add new pollutants, weather variables, or classification thresholds |

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
- 🌫️ [UCI Air Quality Dataset](https://archive.ics.uci.edu/) — Source dataset for this analysis
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support

---

<div align="center">

---

*Made with ❤️ and Pandas DataFrames — Last updated: 24 July, 2026*

</div>
