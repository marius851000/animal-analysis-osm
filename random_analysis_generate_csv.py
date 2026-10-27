import csv
import json
import random

with open("./attraction-animal-overpass.json") as f:
    data = json.load(f)

elements = data["elements"]
sample = random.sample(elements, min(100, len(elements)))

rows = []
for entry in sample:
    tags = entry.get("tags", {})
    name = tags.get("name", "")
    species = tags.get("species", "")
    animal = tags.get("animal", "")
    # language codes of species:<lang> tags, excluding non-language keys
    langs = sorted(
        key.split("species:", 1)[1]
        for key in tags
        if key.startswith("species:")
        and key.split("species:", 1)[1] not in ("wikidata", "wikipedia")
    )
    url = f"https://www.openstreetmap.org/{entry['type']}/{entry['id']}"
    rows.append([name, species, animal, ",".join(langs), url])

with open("./random_sample.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "species", "animal", "species_lang", "url"])
    writer.writerows(rows)

print(f"Wrote {len(rows)} rows to random_sample.csv")
