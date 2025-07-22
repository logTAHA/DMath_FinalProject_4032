import csv

selected = set()
with open('selected-users.txt', 'r', encoding='utf-8') as f:
    for line in f:
        uid = line.strip()
        if uid:
            selected.add(uid)

with open('following.csv', 'r', newline='', encoding='utf-8') as infile, \
     open('selected-following.csv', 'w', newline='', encoding='utf-8') as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # write header in "selected-following.csv" and skip header in "following.csv"
    header = next(reader)
    writer.writerow(header)

    count = 0

    for src, rel, tgt in reader:
        if src in selected and tgt in selected:
            writer.writerow([src, rel, tgt])
            count += 1

    print(f"relation count: {count}")

print(f"Filtered relations saved to selected-following.csv ({len(selected)} users wrote).")
