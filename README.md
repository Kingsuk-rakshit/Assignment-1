# Assignment 1 — Python Data Handling

A robust set of Python scripts demonstrating data handling capabilities: fetching data from APIs, importing CSVs into SQLite databases, and generating data visualizations.

> [!NOTE]
> This project has been verified to work on Windows with Python 3.

---

## 📂 Project Layout

```text
assignment-1/
├── data/                   # Input data files
│   └── users.csv           # Source CSV for user data
├── database/               # Generated SQLite databases
│   ├── books.db            # Output from api_to_sqlite.py
│   └── users.db            # Output from csv_to_db.py
├── output/                 # Generated artifacts
│   └── scores_chart.png    # Visualization output
├── src/                    # Source code
│   ├── api_to_sqlite.py    # Fetches OpenLibrary data
│   ├── csv_to_db.py        # Processes CSV to SQLite
│   └── student_scores_visualization.py # Generates charts
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Installation & Execution

Run the following commands in PowerShell to set up and verify the project:

```powershell
# 1. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Processing CSV to Database
# Reads data/users.csv, handles BOM/encoding, dedupes by email
python src\csv_to_db.py

# 4. Fetching API Data to Database
# Fetches book data from OpenLibrary API
python src\api_to_sqlite.py

# 5. Generating Visualization
# Creates a bar chart of student scores
python src\student_scores_visualization.py
```

---

## ✅ Verified Outputs

After running the above commands, verify the following files are created:

| Category | File Path | Description |
|----------|-----------|-------------|
| **Database** | `database/users.db` | Contains unique user records imported from CSV. |
| **Database** | `database/books.db` | Contains book data fetched from external API. |
| **Visualization** | `output/scores_chart.png` | Bar chart visualizing student scores/ages. |

---

## 🛠 Features & Capabilities

- **Robust CSV Handling**: Automatically detects and handles UTF-8 BOM signatures in CSV files to prevent encoding errors.
- **Data Deduplication**: Ensures data integrity by preventing duplicate email entries during database insertion.
- **API Integration**: Demonstrates handling of external API responses and mapping them to a relational database schema.
- **Visualization**: automated chart generation using `matplotlib` for data insights.

---

## 🔗 References

- **Complex Python Code**: [AI-SDR-System](https://github.com/Kingsuk-rakshit/AI-SDR-System)
- **Complex Database Code**: [GoogleAnalytics4-BigQuery-SQL](https://github.com/Kingsuk-rakshit/GoogleAnalytics4-BigQuery-SQL)
