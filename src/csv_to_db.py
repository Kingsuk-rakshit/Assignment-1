# load data/users.csv into database/users.db
from pathlib import Path
import csv, sqlite3, sys

# read csv
def read_users(path=Path("data/users.csv")):
    p = Path(path)
    if not p.exists(): raise FileNotFoundError(p)
    with p.open(encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f)
        if not r.fieldnames: raise ValueError("missing header")
        hdr = [h.strip().lstrip('\ufeff').lower() if h else "" for h in r.fieldnames]
        if "name" not in hdr or "email" not in hdr:
            raise ValueError(f"headers must include name and email: {r.fieldnames}")
        out = []
        for row in r:
            name = None; email = None
            for k, v in row.items():
                if not k: continue
                k2 = k.strip().lstrip('\ufeff').lower()
                if k2 == "name": name = v.strip() if v else None
                elif k2 == "email": email = v.strip() if v else None
            if name or email: out.append((name, email))
        return out

# save to db
def save_users(db=Path("database/users.db"), users=None):
    db = Path(db); db.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db) as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
        c.execute("DELETE FROM users WHERE id NOT IN (SELECT MIN(id) FROM users GROUP BY email)")
        c.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_email ON users(email)")
        before = conn.total_changes
        c.executemany("INSERT OR IGNORE INTO users(name,email) VALUES(?,?)", users or [])
        conn.commit()
        return max(0, conn.total_changes - before)

# run
if __name__ == "__main__":
    try:
        users = read_users()
    except Exception as e:
        print("Error:", e); sys.exit(1)
    if not users:
        print("No users found"); sys.exit(0)
    ins = save_users(users=users)
    print(f"Inserted {ins} new users")
    with sqlite3.connect("database/users.db") as conn:
        for n, e in conn.execute("SELECT name,email FROM users ORDER BY id"):
            print(f" - {n or ''} <{e or ''}>")
