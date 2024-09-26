import os
from utils import parse_source, show_table


file_name = 'source.txt'

how_many_records = int(input("How many records to parse?\n"))

with open(file_name, 'r', encoding='utf-8') as file:
    content = file.read()
    data = parse_source(content, how_many_records)

# remove the file if already exists
output_file_name = 'output.html'
if os.path.exists(output_file_name):
    os.remove(output_file_name)

# prepare html for output.html
data_html = ""
for game in data:
    name_to_add = f"<h1>{game['name']}</h1>"
    discount_to_add = f"<p>discount: {game['discount']}</p>"
    price_to_add = f"<p>price: {game['price']}</p>"

    data_html += name_to_add
    data_html += discount_to_add
    data_html += price_to_add

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Steam sales</title>
</head>
<body>
    {data_html}
</body>
</html>"""

# write website to output.html
with open(output_file_name, 'w', encoding='utf-8') as file:
    file.write(html_template)

show_table(data)
