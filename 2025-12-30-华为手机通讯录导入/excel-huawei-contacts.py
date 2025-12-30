import pandas as pd

# 华为导入用vcf好用一点

# ===== 配置区 =====
EXCEL_FILE = r"D:\hysz\00-record\2025-12-30-华为手机通讯录导入\汉阳国资集团等169个部门通讯录.xlsx"   # Excel 文件名
VCF_FILE = r"D:\hysz\00-record\2025-12-30-华为手机通讯录导入\汉阳国资集团等169个部门通讯录.vcf"      # 输出的 vcf 文件
# =================

df = pd.read_excel(EXCEL_FILE)

vcards = []

for _, row in df.iterrows():
    name = str(row.get("姓名", "")).strip()
    title = str(row.get("职务", "")).strip()
    dept = str(row.get("部门", "")).strip()
    gender = str(row.get("性别", "")).strip()
    mobile = str(row.get("手机", "")).strip()
    short = str(row.get("集团短号", "")).strip()

    if not name or not mobile:
        continue  # 没姓名或手机号的不导

    # 姓名拆分（姓 + 名）
    if len(name) >= 2:
        family_name = name[0]
        given_name = name[1:]
    else:
        family_name = name
        given_name = ""

    note_parts = []
    if dept:
        note_parts.append(f"部门：{dept}")
    if gender:
        note_parts.append(f"性别：{gender}")
    if short:
        note_parts.append(f"集团短号：{short}")

    note = "；".join(note_parts)

    vcard = f"""BEGIN:VCARD
VERSION:3.0
N:{family_name};{given_name};;;
FN:{name}
"""

    if title:
        vcard += f"TITLE:{title}\n"

    if mobile:
        vcard += f"TEL;TYPE=CELL:{mobile}\n"

    if short:
        vcard += f"TEL;TYPE=WORK:{short}\n"

    if note:
        vcard += f"NOTE:{note}\n"

    vcard += "END:VCARD\n"

    vcards.append(vcard)

with open(VCF_FILE, "w", encoding="utf-8") as f:
    f.writelines(vcards)

print(f"已生成 {VCF_FILE}，共 {len(vcards)} 个联系人")
