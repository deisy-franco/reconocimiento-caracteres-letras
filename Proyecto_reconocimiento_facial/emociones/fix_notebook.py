import json

with open('reconocimiento_emociones.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell.get('id') == '7bcb1a48':
        # Fix trailing comma on patience line
        for i, line in enumerate(cell['source']):
            if line == '    patience=5,\n':
                cell['source'][i] = '    patience=5\n'
                print(f'Fixed trailing comma on line {i}: {repr(cell["source"][i])}')

with open('reconocimiento_emociones.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print('Done. Notebook saved.')
