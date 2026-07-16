<div align="center">

# -- ! Pandas Analyzer & Data Visualization ! --
### *An Interactive Console-Based Sales Data Analysis & Visualization Toolkit Built with OOP Principles*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Array%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![OOP](https://img.shields.io/badge/Design-OOP%20%2F%20Classes-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Console](https://img.shields.io/badge/Console-Interactive%20CLI-4CAF50?style=for-the-badge&logo=windowsterminal&logoColor=white)](https://www.python.org/)

<br/>

> *"Raw sales data is just numbers — until you clean it, shape it, and let it tell a story."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧱 Class Design — `SalesDataAnalyzer`](#-class-design--salesdataanalyzer)
- [🖥️ Example Console Interaction](#️-example-console-interaction)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Pandas Analyzer & Data Visualization** tool is an interactive, console-based Python application that combines **Pandas** and **NumPy** for data manipulation with **Matplotlib** and **Seaborn** for visualization — all wrapped inside a single encapsulated `SalesDataAnalyzer` class. It lets users load a sales dataset, explore and clean it, run mathematical and statistical operations, and generate a full range of charts, entirely through a clean, menu-driven interface.

This project is designed to:
- Demonstrate how Pandas, NumPy, Matplotlib, and Seaborn can be combined inside a well-structured class
- Practice encapsulation, constructors/destructors, static methods, and class methods in Python
- Apply `match`/`case` structural pattern matching instead of long `if-elif` chains
- Provide a hands-on, menu-driven tool for data cleaning, analysis, and visualization

---

## 🎯 Problem Statement

> **Objective:** Develop a comprehensive Sales Data Analysis and Visualization tool in Python. The project uses Pandas for data manipulation and analysis, and Matplotlib and Seaborn for data visualization, giving hands-on experience handling real-world sales datasets, performing data operations, and creating insightful visualizations to support business decisions.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Loading & Exploration | Core | Load a CSV dataset and inspect rows, columns, dtypes, and info |
| Data Cleaning | Core | Detect, fill, drop, or replace missing values |
| DataFrame Operations | Core | NumPy conversion/indexing/slicing, math operations, combine, split, pivot tables |
| Search, Sort & Filter | Core | Search records, sort by any column, filter with custom conditions |
| Aggregates & Statistics | Core | Sum, mean, count, standard deviation, variance, percentiles |
| Data Visualization | Core | Bar, line, scatter, pie, histogram, and stack plots, saved to file |
| OOP Design | Structure | Constructor/destructor, encapsulation, operator overloading, `@classmethod` |

The goal is to demonstrate a **clean, class-based approach to sales data analytics** through a fully interactive CLI.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔁 **Persistent Menu Loop** | Program runs continuously until the user selects Exit |
| 📥 **CSV Dataset Loading** | Load any sales dataset with graceful error handling for bad paths |
| 🔍 **Data Exploration** | Head, tail, column names, data types, and full `info()` summary |
| 🧹 **Missing Data Handling** | Detect, mean-fill, drop, or replace missing values |
| 🧮 **NumPy-Powered Math** | Convert columns to NumPy arrays and run element-wise operations |
| 🔗 **Combine / Split** | Merge or concatenate DataFrames, or split by group |
| 📊 **Pivot Tables** | Summarize data with `pd.pivot_table()` using sum, mean, or count |
| 🔎 **Search, Sort, Filter** | Locate records, sort by any column, filter with conditions like `> 600` |
| 📈 **Six Chart Types** | Bar, line, scatter, pie, histogram, and stack plots via Matplotlib |
| 💾 **Save Visualizations** | Export the most recent chart to a PNG/JPEG file |
| 🧱 **True OOP Encapsulation** | Internal `data` state managed through class methods, with `__len__` and `__add__` overloading |
| 🐍 **Modern `match`/`case` Control Flow** | No `if-elif` chains — every menu uses structural pattern matching |

---

## 🏗️ Project Structure

```
📦 pandas-analyzer/
│
├── 📓 PR-9.ipynb             ← Jupyter Notebook version with explanatory markdown cells
├── 📁 data/
│   └── 📄 sales_data.csv    ← Sample sales dataset
│
└── 📄 README.md             ← Project documentation
```

---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌─────────────────────────────┐
│   Display Main Menu         │  ← Load / Explore / Operations / Clean / Stats / Visualize / Save / Exit
└────────────┬────────────────┘
             │
   ┌───────┬─┴──────┬─────────┬─────────┬──────────┬─────────┐
   ▼        ▼        ▼         ▼         ▼          ▼         ▼
┌──────┐ ┌───────┐ ┌────────┐ ┌───────┐ ┌────────┐ ┌───────┐ ┌──────┐
│Choice1│ │Choice2│ │Choice3 │ │Choice4│ │Choice5 │ │Choice6│ │Choice7│
│ Load │ │Explore│ │DataFrame│ │ Clean │ │ Stats  │ │Visualize│ │ Save │
│Dataset│ │ Data  │ │ Ops    │ │ Data  │ │        │ │        │ │ Plot │
└───┬──┘ └───┬───┘ └───┬────┘ └───┬───┘ └───┬────┘ └───┬───┘ └───┬──┘
    │        │         │          │         │          │         │
    ▼        ▼         ▼          ▼         ▼          ▼         ▼
┌───────────────────────────────────────────────────────────────────┐
│                     Print Output to Console                       │
└────────────────────────────┬──────────────────────────────────────┘
                              │
                              ▼
                      Loop Back to Menu
                              │
                     (Choice: 8) Exit ✅
```

---

## 🧱 Class Design — `SalesDataAnalyzer`

The entire toolkit is built around one encapsulated class:

```python
class SalesDataAnalyzer:
    def __init__(self, file_path=None):
        self.data = None
        self._last_figure = None
        if file_path:
            self.load_data(file_path)

    def __del__(self):
        plt.close('all')
```

| Concept | Where it's used |
|---------|-----------------|
| 🏗️ **Constructor / Destructor** | `__init__` initializes the dataset; `__del__` closes any open Matplotlib figures |
| 🔒 **Encapsulation** | `self.data` (the Pandas DataFrame) is managed entirely through class methods |
| ➕ **Operator Overloading** | `__add__` combines two `SalesDataAnalyzer` instances via `pd.concat`; `__len__` returns row count |
| 🏛️ **`@classmethod`** | `about()` provides class-level information |
| 🐍 **`match` / `case`** | Every menu (explore, operations, math, missing data, search/sort/filter, statistics, visualization) uses structural pattern matching instead of `if-elif` chains |
| 🧩 **Method Coverage** | `load_data`, `explore_data`, `clean_data`, `mathematical_operations`, `combine_data`, `split_data`, `search_sort_filter`, `aggregate_functions`, `statistical_analysis`, `create_pivot_table`, `visualize_data`, `save_visualization` |

---

## 🖥️ Example Console Interaction

```
========== Data Analysis & Visualization Program ==========
Please select an option:
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
============================================================

Enter your choice: 1

== Load Dataset ==
Enter the path of the dataset (CSV file): data/sales_data.csv
Dataset loaded successfully!

========== Data Analysis & Visualization Program ==========
...
Enter your choice: 2

== Explore Data ==
1. Display the first 5 rows
2. Display the last 5 rows
3. Display column names
4. Display data types
5. Display basic info
Enter your choice: 1

   SalesID    Product      Region  Sales  Year
0      101  Product A       North    500  2022
1      102  Product B        East    600  2022
2      103  Product C  West Coast    700  2022
3      104  Product D       South    800  2022
4      105  Product E     Central    550  2022

========== Data Analysis & Visualization Program ==========
...
Enter your choice: 4

== Handle Missing Data ==
1. Display rows with missing values
2. Fill missing values with mean
3. Drop rows with missing values
4. Replace missing values with a specific value
Enter your choice: 1

No missing values found in the dataset!

========== Data Analysis & Visualization Program ==========
...
Enter your choice: 6

== Data Visualization ==
1. Bar Plot
2. Line Plot
3. Scatter Plot
4. Pie Chart
5. Histogram
6. Stack Plot
Enter your choice: 3

== Scatter Plot ==
Enter x-axis column name: Sales
Enter y-axis column name: Year
Generating scatter plot...
Scatter plot displayed successfully!

========== Data Analysis & Visualization Program ==========
...
Enter your choice: 7

== Save Visualization ==
Enter file name to save the plot (e.g., scatter_plot.png): scatter_plot.png
Visualization saved as scatter_plot.png successfully!

========== Data Analysis & Visualization Program ==========
...
Enter your choice: 8

Exiting the program. Goodbye!
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.10+ | Core programming language (required for `match`/`case`) |
| 🐼 **Pandas** | Latest | Data loading, cleaning, manipulation, and analysis |
| 🔢 **NumPy** | Latest | Array conversion and element-wise math operations |
| 📊 **Matplotlib** | Latest | Bar, line, scatter, pie, histogram, and stack plots |
| 🎨 **Seaborn** | Latest | Enhanced statistical visualizations |
| 🐍 **`match` / `case`** | Python 3.10+ | Structural pattern matching for all menu logic |
| 🧱 **OOP** | Built-in | Classes, constructors/destructors, operator overloading, class methods |
| 🖨️ **print() / input()** | Built-in | Console I/O and user interaction |

---

## 📈 Results & Insights

Running the program produces:

- ✅ **Full Data Lifecycle** — load, explore, clean, transform, and analyze a sales dataset end-to-end
- 🔢 **Accurate DataFrame Operations** — NumPy conversions, math operations, combine/split, and pivot tables all verified against expected output
- 📊 **Reliable Statistics** — sum, mean, count, standard deviation, variance, and percentiles computed correctly
- 📈 **Six Working Chart Types** — bar, line, scatter, pie, histogram, and stack plots, each savable to file
- 🔁 **Persistent Menu** — the program loops back after every task until the user exits
- ⚠️ **Clear Error Feedback** — missing files, bad column names, and invalid choices are all caught gracefully

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🧱 **True OOP Design** | Constructor/destructor, encapsulation, and operator overloading used meaningfully |
| 🐍 **Modern Python Syntax** | `match`/`case` throughout instead of nested `if-elif` chains |
| 📚 **Educational** | Great reference for combining Pandas, NumPy, and Matplotlib inside one class |
| 📓 **Notebook & Script Ready** | Available as both a standalone `.py` script and an annotated `.ipynb` notebook |
| 🖥️ **Minimal Dependencies** | Just Pandas, NumPy, Matplotlib, and Seaborn — no heavyweight frameworks |
| 🧪 **Extensible** | Easy to add new chart types or statistical functions |
| 🛡️ **Input Safety** | Missing files, bad columns, and invalid menu choices are handled without crashing |

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
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support

---

<div align="center">

---

*Made with ❤️ and Pandas DataFrames — Last updated: 16 July, 2026*

</div>
