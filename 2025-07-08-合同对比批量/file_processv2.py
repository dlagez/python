import os
import difflib
import csv
from openpyxl import Workbook
import re
from openpyxl.utils import get_column_letter

# 不需要匹配文件了，合同最终附件列表、合同创建附件列表文件夹下面只有一个文件，把他们做成表格即可。

# 顶层目录路径（包含多个项目子目录）
root_dir = r'D:\Download\all07164-手动删除部分数据'  # 替换为你的目录路径

# 结果存储
all_results = []

# 遍历每个项目子目录
for project_name in os.listdir(root_dir):
    project_path = os.path.join(root_dir, project_name)
    if not os.path.isdir(project_path):
        continue

    final_dir = os.path.join(project_path, '合同最终附件列表')
    create_dir = os.path.join(project_path, '合同最终附件列表')

    if not os.path.exists(final_dir) or not os.path.exists(create_dir):
        print(f"跳过 {project_name}，两个必要子目录缺失。")
        continue

    # 获取两个文件夹中唯一文件
    final_files = [f for f in os.listdir(final_dir) if os.path.isfile(os.path.join(final_dir, f))]
    create_files = [f for f in os.listdir(create_dir) if os.path.isfile(os.path.join(create_dir, f))]

    if len(final_files) != 1 or len(create_files) != 1:
        print(f"跳过 {project_name}，文件数异常。最终附件：{len(final_files)}，创建附件：{len(create_files)}")
        continue

    final_file_path = os.path.join(final_dir, final_files[0])
    create_file_path = os.path.join(create_dir, create_files[0])

    all_results.append([project_name, final_file_path, create_file_path])

# 写入CSV文件
output_csv = os.path.join(root_dir, '所有匹配结果-2025-07-30.csv')
with open(output_csv, mode='w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['项目名称', '合同最终附件路径', '最相似合同创建附件路径'])
    writer.writerows(all_results)

print(f"处理完成，共处理 {len(all_results)} 个项目，结果保存在：{output_csv}")