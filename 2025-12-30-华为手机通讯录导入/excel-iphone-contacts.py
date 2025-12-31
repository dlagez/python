import pandas as pd

# 

# ===== 配置区 =====
EXCEL_FILE = r"D:\hysz\00-record\2025-12-30-华为手机通讯录导入\汉阳国资集团等169个部门通讯录.xlsx"   # Excel 文件名
VCF_FILE = r"D:\hysz\00-record\2025-12-30-华为手机通讯录导入\汉阳国资集团等169个部门通讯录-iphone-v3.vcf"      # 输出的 vcf 文件
# =================

df = pd.read_excel(EXCEL_FILE, engine="openpyxl")

vcards = []

for _, row in df.iterrows():
    name = str(row.get("姓名", "")).strip()
    mobile = str(row.get("手机", "")).strip()
    short = str(row.get("集团短号", "")).strip()
    dept = str(row.get("部门", "")).strip()
    title = str(row.get("职务", "")).strip()
    gender = str(row.get("性别", "")).strip()

    if not name or not mobile:
        continue

    notes = []
    if title:
        notes.append(f"职务：{title}")
    if gender:
        notes.append(f"性别：{gender}")

    note_field = "\\n".join(notes)

    vcard = f"""BEGIN:VCARD
VERSION:3.0
PRODID:-//Apple Inc.//iPhone OS 18.7.2//EN
N:;{name};;;
FN:{name}
ORG:{dept};
TEL;type=CELL;type=VOICE;type=pref:{mobile}
"""

    # 第二个号码：集团短号
    if short and short.lower() != "nan":
        vcard += f"TEL;type=CELL;type=VOICE:{short}\n"

    if note_field:
        vcard += f"NOTE:{note_field}\n"

    vcard += "END:VCARD\n"

    vcards.append(vcard)

with open(VCF_FILE, "w", encoding="utf-8") as f:
    f.writelines(vcards)

print(f"已生成 {VCF_FILE}，共 {len(vcards)} 个联系人")