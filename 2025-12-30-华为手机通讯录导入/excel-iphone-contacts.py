import pandas as pd

# 

# ===== 配置区 =====
EXCEL_FILE = r"D:\hysz\00-record\2025-12-30-华为手机通讯录导入\汉阳国资集团等169个部门通讯录.xlsx"   # Excel 文件名
VCF_FILE = r"D:\hysz\00-record\2025-12-30-华为手机通讯录导入\汉阳国资集团等169个部门通讯录-iphone.vcf"      # 输出的 vcf 文件
# =================

df = pd.read_excel(EXCEL_FILE, engine="openpyxl")

vcards = []

for _, row in df.iterrows():
    name = str(row.get("姓名", "")).strip()
    mobile = str(row.get("手机", "")).strip()

    if not name or not mobile:
        continue  # 跳过没有姓名或手机号的行

    # 可以选择加集团短号或者备注，这里只保留姓名+手机号
    vcard = f"""BEGIN:VCARD
VERSION:3.0
PRODID:-//Apple Inc.//iPhone OS 18.7.2//EN
N:;{name};;;
FN:{name}
TEL;type=CELL;type=VOICE;type=pref:{mobile}
END:VCARD
"""
    vcards.append(vcard)

# 写入文件（UTF-8）
with open(VCF_FILE, "w", encoding="utf-8") as f:
    f.writelines(vcards)

print(f"已生成 {VCF_FILE}，共 {len(vcards)} 个联系人")
