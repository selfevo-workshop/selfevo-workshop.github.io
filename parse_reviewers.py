import csv

# Assuming 'reviewers.csv' contains the reviewers' names, modify path as needed
reviewers = {}
with open("assets/accepted_papers/reviewers.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        reviewers[row["name"]] = row["institution name"]

# Generate HTML list items for each reviewer
reviewers_html = "\n".join(
    [
        f"<li>{name}, <it>{institution}</it></li>"
        for name, institution in reviewers.items()
    ]
)

# Output the HTML for manual insertion into the webpage
print("Reviewers List HTML:\n", reviewers_html)
