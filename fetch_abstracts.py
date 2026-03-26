import requests
import csv
import time

INPUT_FILE = "articles_raw.csv"
OUTPUT_FILE = "articles_with_abstracts.csv"

def get_abstract(title):
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": title,
        "limit": 1,
        "fields": "title,abstract"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if "data" in data and len(data["data"]) > 0:
            return data["data"][0].get("abstract", "")
    except:
        return ""

    return ""

with open(INPUT_FILE, newline='', encoding="utf-8") as infile, \
     open(OUTPUT_FILE, 'w', newline='', encoding="utf-8") as outfile:

    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        title = row["Title"]
        print(f"Fetching: {title}")

        abstract = get_abstract(title)
        row["Abstract"] = abstract

        writer.writerow(row)
        time.sleep(1)

print("Done! File saved as articles_with_abstracts.csv")
