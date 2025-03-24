import csv
from collections import defaultdict

# Assuming 'papers.csv' content is loaded here, modify path as needed
papers_by_venue = defaultdict(list)
with open("assets/accepted_papers/papers.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        papers_by_venue[row["venue"]].append(row)


# Function to generate HTML for each paper
def generate_paper_html(paper):
    # Customize HTML structure as needed
    return f'<li><strong> {paper["title"]}</strong>, <br>{paper["authors"]}</li>'


# Generate HTML content for Oral and Poster
html_content_oral = (
    "<ul>"
    + "\n".join(
        [
            generate_paper_html(paper)
            for paper in papers_by_venue["LLMAgents @ ICLR 2024 Oral"]
        ]
    )
    + "</ul>"
)
html_content_poster = (
    "<ul>"
    + "\n".join(
        [
            generate_paper_html(paper)
            for paper in papers_by_venue["LLMAgents @ ICLR 2024 Poster"]
        ]
    )
    + "</ul>"
)

# Output the content for manual insertion
print("Oral Presentations:\n", html_content_oral)
print("\nPoster Presentations:\n", html_content_poster)
