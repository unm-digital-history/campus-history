import os
import yaml
import pandas as pd

ESSAYS_DIR = 'essays'
CSV_PATH = 'gsheet-to-csv.csv'  # Update if your CSV filename is different

def read_yaml_header(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if lines and lines[0].strip() == '---':
        end_idx = next((i for i, line in enumerate(lines[1:], 1) if line.strip() == '---'), None)
        if end_idx is not None:
            yaml_str = ''.join(lines[1:end_idx])
            try:
                existing_header = yaml.safe_load(yaml_str) or {}
            except Exception as e:
                print(f"YAML parse error in {md_path}: {e}")
                existing_header = {}
            body = lines[end_idx+1:]
            return existing_header, body
    return {}, lines

def update_yaml_header(md_path, new_fields):
    existing_header, body = read_yaml_header(md_path)
    # Merge: new_fields overwrite existing_header
    merged_header = {**existing_header, **new_fields}
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('---\n')
        yaml.dump(merged_header, f, sort_keys=False, allow_unicode=True)
        f.write('---\n')
        f.writelines(body)

# Read CSV
df = pd.read_csv(CSV_PATH)

for _, row in df.iterrows():
    folder_name = row.get('folder-name')
    if not folder_name:
        continue
    md_path = os.path.join(ESSAYS_DIR, folder_name, 'index.md')
    if not os.path.exists(md_path):
        print(f"Markdown file not found: {md_path}")
        continue
    # Remove 'folder-name' from new fields
    new_fields = {k: v for k, v in row.items() if k != 'folder-name'}
    update_yaml_header(md_path, new_fields)
    print(f"Updated YAML for {md_path}")

print("Done updating YAML headers from CSV.")