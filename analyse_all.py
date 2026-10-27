import json

with open("./attraction-animal-overpass.json") as f:
    data = json.load(f)

element_count_buckets={}

for entry in data["elements"]:
    nb_elem = len(entry["tags"])
    if nb_elem not in element_count_buckets:
        element_count_buckets[nb_elem] = 0
    element_count_buckets[nb_elem] += 1

print(f"Number of attraction=animal: {len(data["elements"])}")

other_key_count = 0
for i in sorted(element_count_buckets.keys()):
    if i > 10:
        other_key_count += element_count_buckets[i]
    else:
        print(f"key count: {i} key: {element_count_buckets[i]}")
print(f"key count: other: {other_key_count}")