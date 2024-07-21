from bs4 import BeautifulSoup
import csv

for i in range(0, 17):
    with open(f"sitemap-{i}.xml", "r") as f:
        content = f.read()
        sitemap_index = BeautifulSoup(content, 'html.parser')
        urls = [element.text for element in sitemap_index.findAll('loc')]
        with open(f"no-{i}.csv", "w") as csvf:
            writer = csv.writer(csvf)
            for url in urls:
                writer.writerow([url, "no"])
