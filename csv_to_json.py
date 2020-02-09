import csv
import json

l = []

with open("countries_dependencies.csv") as fp:
    for i, r in enumerate(csv.reader(fp, delimiter=';')):
        if i == 0:
            continue

        print(";".join(r))

        l.append({
            "dependent_country": r[0],
            "country": r[1],
            "relationship": r[2],
            "seeks_independence": json.loads(r[3].lower()), # convert to bool
            "disputed_territory": json.loads(r[4].lower())  # convert to bool
        })

with open('countries_dependencies.json', 'w') as fp:
    json.dump(l, fp)
