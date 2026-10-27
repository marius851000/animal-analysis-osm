import csv
from collections import Counter

with open("./manual_random_analysis.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

name_use = Counter(row["NAME_USE"] for row in rows)
animal_use = Counter(row["ANIMAL_USE"] for row in rows)


def print_counts(title, counter):

    # percentages are only computed for non-empty, non-??? values;
    # empty and ??? are displayed with their count but no percentage
    known_total = sum(
        count for value, count in counter.items() if value and value != "???"
    )
    print(f"{title}:")
    for value, count in counter.most_common():
        label = value if value else "(empty)"
        if value and value != "???":
            proportion = count / known_total if known_total else 0
            print(f"  {label}: {count} ({proportion:.1%})")
        else:
            print(f"  {label}: {count}")
    print()


print(f"Total rows: {len(rows)}")
print_counts("NAME_USE", name_use)
print_counts("ANIMAL_USE", animal_use)
