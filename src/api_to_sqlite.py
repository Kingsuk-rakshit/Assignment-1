# simple script to fetch programming books and save to sqlite
import requests, sqlite3, os
from pathlib import Path
from typing import List, Tuple

Book = Tuple[str, str, int]

# fetch from api (with timeout)
def fetch_books(limit: int = 10) -> List[dict]:
    url = f"https://openlibrary.org/subjects/programming.json?limit={limit}"
    try:
        r = requests.get(url, timeout=6)
        r.raise_for_status()
        return r.json().get("works", [])
    except requests.RequestException as e:
        print("Could not fetch books:", e)
        return []

# turn raw api items into tuples
def parse_books(raw: List[dict]) -> List[Book]:
    out: List[Book] = []
    for b in raw:
        title = b.get("title") or "Unknown"
        authors = b.get("authors") or []
        author = authors[0].get("name") if authors and isinstance(authors[0], dict) else "Unknown"
        year = b.get("first_publish_year")
        out.append((title, author, year))
    return out

# save list of (title,author,year) into sqlite
def save_books(db_path: str = "database/books.db", books: List[Book] = None) -> int:
    db = Path(db_path)
    db.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db) as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, publish_year INTEGER)")
        c.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_title_author ON books(title,author)")
        before = conn.total_changes
        c.executemany("INSERT OR IGNORE INTO books (title,author,publish_year) VALUES (?,?,?)", books or [])
        conn.commit()
        return max(0, conn.total_changes - before)

# display saved books
def show_books(db_path: str = "database/books.db") -> None:
    if not os.path.exists(db_path):
        print("no database yet")
        return
    with sqlite3.connect(db_path) as conn:
        for row in conn.execute("SELECT id,title,author,publish_year FROM books ORDER BY id"):
            print(f"{row[0]:3d} {row[1]} — {row[2]} ({row[3] or 'n/a'})")

# main flow
def main():
    print("fetching books...")
    raw = fetch_books()
    if not raw:
        print("no books returned")
        return
    books = parse_books(raw)
    added = save_books(books=books)
    print(f"added {added} new books")
    print("current books:")
    show_books()

if __name__ == "__main__":
    main()
