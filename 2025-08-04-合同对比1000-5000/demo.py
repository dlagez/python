import os
import shutil
import pandas as pd

# 设置路径
src_dir = r"D:\Download\all0716"
dst_dir = r"D:\Download\all0804-1000-5000"
excel_path = r"C:\Users\admin\OneDrive\Documents\汉阳市政\00-record\2025-08-04-合同对比-1000-5000\合同对比-1000-5000.xlsx"

# 读取 Excel 文件中的“项目部”列
df = pd.read_excel(excel_path)
project_names = df['项目部'].dropna().unique().tolist()

# 打印读取的项目列表
print("📄 从 Excel 读取到的项目名称列表：")
for i, name in enumerate(project_names, 1):
    print(f"{i:>3}. {name}")

# 分别记录“找到”和“未找到”的项目
found_projects = []
missing_projects = []

# 检查每个项目是否存在于源目录中
for name in project_names:
    check_path = os.path.join(src_dir, name)
    if os.path.exists(check_path):
        found_projects.append(name)
    else:
        missing_projects.append(name)

# 分别打印检查结果
print("\n✅ 已找到以下项目文件夹：")
for name in found_projects:
    print(f"  - {name}")

print("\n❌ 未找到以下项目文件夹：")
for name in missing_projects:
    print(f"  - {name}")

# 用户确认是否进行复制
confirm = input("\n👉 是否继续复制以上存在的项目文件夹？输入 1 确认，其他键退出：")

if confirm.strip() == '1':
    # 创建目标目录（如果不存在）
    os.makedirs(dst_dir, exist_ok=True)

    # 执行复制操作
    for name in project_names:
        src_path = os.path.join(src_dir, name)
        dst_path = os.path.join(dst_dir, name)

        if os.path.exists(src_path):
            try:
                shutil.copytree(src_path, dst_path)
                print(f"✅ 已复制: {name}")
            except Exception as e:
                print(f"⚠️ 复制失败: {name}，原因：{e}")
else:
    print("⛔ 已取消复制操作。")
