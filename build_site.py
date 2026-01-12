import json
import os

# 1. Load your JSON data
try:
    with open('data/phones.json', 'r') as f:
        phones = json.load(f)
    print(f"Successfully loaded {len(phones)} phones from JSON.")
except FileNotFoundError:
    print("Error: data/phones.json not found!")
    phones = []

# 2. Build the HTML string
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mobile Specs Pro</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; background: #f0f2f5; }
        .phone-card { background: white; border-radius: 12px; padding: 20px; margin-bottom: 20px; shadow: 0 4px 6px rgba(0,0,0,0.1); border: 1px solid #ddd; }
        h1 { text-align: center; color: #2c3e50; }
        h2 { color: #3498db; margin-top: 0; }
        .spec-label { font-weight: bold; color: #7f8c8d; }
    </style>
</head>
<body>
    <h1>Mobile Specification Directory</h1>
"""

for phone in phones:
    html_content += f"""
    <div class="phone-card">
        <h2>{phone['brand']} {phone['model']}</h2>
        <p><span class="spec-label">Display:</span> {phone['specs']['display']}</p>
        <p><span class="spec-label">Processor:</span> {phone['specs']['processor']}</p>
        <p><span class="spec-label">Battery:</span> {phone['specs']['battery']}</p>
    </div>
    """

html_content += "</body></html>"

# 3. Save to the 'docs' folder for GitHub Pages
if not os.path.exists('docs'):
    os.makedirs('docs')
    print("Created 'docs' directory.")

with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("SUCCESS: docs/index.html has been generated.")
