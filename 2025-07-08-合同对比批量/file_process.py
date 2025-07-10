import os
import difflib
import csv
from openpyxl import Workbook
import re
from openpyxl.utils import get_column_letter

# 文件名处理脚本

# 顶层目录路径（包含多个项目子目录）
root_dir = r'D:\Download\dayu5000'  # 替换为你的总目录路径

# 获取文件夹下所有文件路径
def get_all_files(directory):
    file_paths = []
    for root, _, files in os.walk(directory):
        for name in files:
            file_paths.append(os.path.join(root, name))
    return file_paths

# 找到最相似的文件
# def find_best_match(target_file, candidates):
#     target_name = os.path.basename(target_file)
#     best_match = None
#     best_ratio = 0
#     for candidate in candidates:
#         candidate_name = os.path.basename(candidate)
#         ratio = difflib.SequenceMatcher(None, target_name, candidate_name).ratio()
#         if ratio > best_ratio:
#             best_ratio = ratio
#             best_match = candidate
#     return best_match, best_ratio


def extract_keywords(filename):
    # 去掉扩展名并按非字母数字汉字拆分
    name = os.path.splitext(os.path.basename(filename))[0]
    # 保留中文、字母、数字
    return set(re.findall(r'[\u4e00-\u9fa5\w]+', name.lower()))

def find_best_match(target_file, candidates):
    target_keywords = extract_keywords(target_file)
    best_match = None
    best_score = -1

    for candidate in candidates:
        candidate_keywords = extract_keywords(candidate)
        common_keywords = target_keywords & candidate_keywords
        score = len(common_keywords)

        if score > best_score:
            best_score = score
            best_match = candidate

    return best_match, best_score


# 所有匹配结果
all_results = []

# 遍历总目录下的每个子文件夹
for project_name in os.listdir(root_dir):
    project_path = os.path.join(root_dir, project_name)
    if not os.path.isdir(project_path):
        continue

    final_dir = os.path.join(project_path, '合同最终附件列表')
    create_dir = os.path.join(project_path, '合同创建附件列表')

    if not os.path.exists(final_dir) or not os.path.exists(create_dir):
        print(f"跳过 {project_name}，两个必要子目录缺失。")
        continue

    final_files = get_all_files(final_dir)
    create_files = get_all_files(create_dir)

    for final_file in final_files:
        match_file, similarity = find_best_match(final_file, create_files)
        all_results.append([project_name, final_file, match_file])

# 输出所有匹配到 CSV
output_csv = os.path.join(root_dir, '所有匹配结果.csv')
with open(output_csv, mode='w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['合同名称', '合同最终附件路径', '最相似合同创建附件路径'])
    writer.writerows(all_results)

print(f"所有项目匹配完成，结果保存在：{output_csv}")
