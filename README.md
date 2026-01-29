# Assignment 1 — Python Data Handling 

A small set of scripts that demonstrate fetching data from APIs, importing CSVs into SQLite, and producing a simple visualization.

---

## Project layout

```
assignment-1/
├── data/                   # input CSVs
│   └── users.csv
├── database/               # generated sqlite databases
│   ├── books.db
│   └── users.db
├── output/                 # generated artifacts
│   └── scores_chart.png
├── src/                    # source scripts
│   ├── api_to_sqlite.py
│   ├── student_scores_visualization.py
│   └── csv_to_db.py
├── requirements.txt
└── README.md
```

---

## What each script does 

- `src/api_to_sqlite.py` — fetches programming books (OpenLibrary) and stores them in `database/books.db`.
- `src/student_scores_visualization.py` — fetches sample users (DummyJSON), treats `age` as a demo "score", and saves a bar chart to `output/scores_chart.png`.
- `src/csv_to_db.py` — reads `data/users.csv`, writes users into `database/users.db` (handles BOM and dedupes by email).

---

## Quick start (Windows) 

1. Create and activate a virtual environment:

```powershell
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

3. Run the scripts:

```powershell
python src\csv_to_db.py
python src\api_to_sqlite.py
python src\student_scores_visualization.py
```

---

## Notes & troubleshooting 

- CSV encoding: The CSV reader prefers `utf-8-sig` and strips a BOM (if present). If you get decoding errors, re-save the file as **CSV UTF-8 (comma delimited)** from Excel.
- CSV headers: `name` and `email` headers are required (case-insensitive).
- Deduplication: `csv_to_db.py` keeps the earliest record per email and adds a unique index to prevent duplicates.
- Network calls use a short timeout and print friendly messages on failure.

---

## Outputs at a glance 

| Task | Output |
|------|--------|
| API → DB | `database/books.db` |
| Visualization | `output/scores_chart.png` |
| CSV → DB | `database/users.db` |

---

## Suggested improvements 

- Add `pandas`/`openpyxl` to accept `.xlsx` files directly.
- Add command-line options to control CSV/DB paths or quiet mode.
- Add tests and a simple CI workflow.

---

## 🔗 Complex Code References(4, 5)

- Complex Python Code: *(https://github.com/Kingsuk-rakshit/AI-SDR-System)*  
- Complex Database Code: *(https://github.com/Kingsuk-rakshit/GoogleAnalytics4-BigQuery-SQL)*  

---
