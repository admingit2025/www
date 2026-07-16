from pathlib import Path
orig = Path(r'c:\Users\lenovo\Desktop\31047689 (1).vcf')
dedup = Path(r'c:\Users\lenovo\Desktop\31047689 (1)_dedup.vcf')
for p in (orig, dedup):
    if not p.exists():
        print(f'{p.name} not found')
        continue
    cnt = sum(1 for l in p.read_text(encoding='utf-8', errors='ignore').splitlines() if l.strip() == 'BEGIN:VCARD')
    print(f'{p.name}: {cnt} contacts')
