from collections import defaultdict
import os, sys
path = r'c:\Users\lenovo\Desktop\31047689 (1).vcf'
if not os.path.isfile(path):
    print('ERROR: vcf 文件不存在:', path)
    sys.exit(1)
with open(path, encoding='utf-8', errors='ignore') as f:
    lines = f.read().splitlines()

cards = []
card = []
for line in lines:
    if line.strip() == 'BEGIN:VCARD':
        card = [line]
    elif line.strip() == 'END:VCARD':
        card.append(line)
        cards.append(card)
        card = []
    else:
        if card is not None:
            card.append(line)

print('cards', len(cards))

seen_uid = set()
seen_nonuid = set()
keep = []

for i, c in enumerate(cards):
    # 解析字段
    n = ''
    fn = ''
    uid = ''
    fields = []
    for l in c:
        if l.startswith('N:'):
            n = l[2:]
        elif l.startswith('FN:'):
            fn = l[3:]
        elif l.startswith('UID:'):
            uid = l[4:]
        elif not any(l.startswith(prefix) for prefix in ('BEGIN:VCARD', 'END:VCARD', 'VERSION:', 'PRODID:')):
            fields.append(l)

    # 如果只有 N/FN/UID（没有其他属性），则认为空联系人，删除
    is_empty_card = True
    for l in c:
        if not any(l.startswith(prefix) for prefix in ('BEGIN:VCARD', 'END:VCARD', 'VERSION:', 'PRODID:', 'N:', 'FN:', 'UID:')):
            is_empty_card = False
            break
    if is_empty_card:
        continue

    # 判断去重：UID 相同直接重复（删除后者）
    if uid.strip() and uid.strip() in seen_uid:
        continue
    if uid.strip():
        seen_uid.add(uid.strip())

    # 非UID内容一致也视为重复（只要内容完全相同，UID可以不同）
    nonuid_content = tuple(sorted([l for l in c if not l.startswith('UID:') and not l.startswith('BEGIN:VCARD') and not l.startswith('END:VCARD')]))
    if nonuid_content in seen_nonuid:
        continue
    seen_nonuid.add(nonuid_content)

    keep.append(c)

print('keep', len(keep))
out_vcf = path.replace('.vcf', '_dedup.vcf')
with open(out_vcf, 'w', encoding='utf-8') as f:
    for c in keep:
        for l in c:
            f.write(l + '\n')
print('wrote', out_vcf)

# 输出 CSV：N,FN,UID,EMAIL,TEL,NOTE,ADR,ORG,URL 等
out_csv = path.replace('.vcf', '_dedup.csv')
import csv
csv_fields = ['N', 'FN', 'UID', 'EMAIL', 'TEL', 'NOTE', 'ADR', 'ORG', 'URL', 'TITLE', 'EMAIL_ALL', 'TEL_ALL', 'OTHER']
with open(out_csv, 'w', newline='', encoding='utf-8') as cf:
    writer = csv.DictWriter(cf, fieldnames=csv_fields)
    writer.writeheader()
    for c in keep:
        row = {k: '' for k in csv_fields}
        emails = []
        tels = []
        others = []
        for l in c:
            if l.startswith('N:'):
                row['N'] = l[2:]
            elif l.startswith('FN:'):
                row['FN'] = l[3:]
            elif l.startswith('UID:'):
                row['UID'] = l[4:]
            elif l.startswith('EMAIL'):
                v = l.split(':', 1)[1] if ':' in l else ''
                emails.append(v)
            elif l.startswith('TEL'):
                v = l.split(':', 1)[1] if ':' in l else ''
                tels.append(v)
            elif l.startswith('NOTE:'):
                row['NOTE'] = l[5:]
            elif l.startswith('ADR:'):
                row['ADR'] = l[4:]
            elif l.startswith('ORG:'):
                row['ORG'] = l[4:]
            elif l.startswith('URL:'):
                row['URL'] = l[4:]
            elif l.startswith('TITLE:'):
                row['TITLE'] = l[6:]
            else:
                if not any(l.startswith(p) for p in ('BEGIN:VCARD', 'END:VCARD', 'VERSION:', 'PRODID:', 'N:', 'FN:', 'UID:')):
                    others.append(l)
        if emails:
            row['EMAIL'] = emails[0]
            row['EMAIL_ALL'] = ';'.join(emails)
        if tels:
            row['TEL'] = tels[0]
            row['TEL_ALL'] = ';'.join(tels)
        if others:
            row['OTHER'] = ' | '.join(others)
        writer.writerow(row)
print('wrote', out_csv)

out = path.replace('.vcf', '_dedup.vcf')
with open(out, 'w', encoding='utf-8') as f:
    for c in keep:
        for l in c:
            f.write(l + '\n')
print('wrote', out)
