# quick script: fetch a few users and plot age as a score
import requests
import matplotlib.pyplot as plt
import os, sys

# fetch data with a short timeout
def fetch_students(limit=5):
    url = f"https://dummyjson.com/users?limit={limit}"
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
    except requests.RequestException as e:
        print("Failed to fetch students:", e)
        return []
    try:
        return r.json().get("users", [])
    except ValueError:
        print("Bad JSON response")
        return []

# build simple name/score lists (age used as proxy for score)
def names_and_scores(students):
    names = []
    scores = []
    for s in students:
        names.append(s.get("firstName", "Unknown"))
        scores.append(s.get("age", 0))  # age as stand-in score
    return names, scores

# average
def mean(xs):
    return sum(xs) / len(xs) if xs else 0

# plot and save
def plot(names, scores, avg):
    os.makedirs("output", exist_ok=True)
    plt.figure(figsize=(8, 5))
    plt.bar(names, scores, color='tab:blue')
    plt.title("Student scores (age as proxy)")
    plt.xlabel("Student"); plt.ylabel("Score")
    plt.xticks(rotation=30)
    plt.tight_layout()
    out = "output/scores_chart.png"
    plt.savefig(out); plt.close()
    print("Saved", out)
    print("Average:", round(avg, 2))

# main flow
def main():
    print("Fetching...")
    students = fetch_students()
    if not students:
        print("No data"); sys.exit(1)
    names, scores = names_and_scores(students)
    avg = mean(scores)
    print("Plotting...")
    plot(names, scores, avg)

if __name__ == "__main__":
    main()
