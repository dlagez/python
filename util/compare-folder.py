import os
import filecmp
import re

# 自然排序的 key 函数
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def compare_folders(main_dir, sub_dir):
    print(f"🔍 主目录: {main_dir}")
    print(f"🔍 副目录: {sub_dir}\n")

    # 获取主文件夹中的所有子目录
    main_subfolders = set([name for name in os.listdir(main_dir) if os.path.isdir(os.path.join(main_dir, name))])
    sub_subfolders = set([name for name in os.listdir(sub_dir) if os.path.isdir(os.path.join(sub_dir, name))])

    # 差异部分
    only_in_main = main_subfolders - sub_subfolders
    only_in_sub = sub_subfolders - main_subfolders
    in_both = main_subfolders & sub_subfolders

    if only_in_main:
        print("📁 主文件夹中多出的子文件夹：")
        for name in sorted(only_in_main, key=natural_sort_key):
            print(f"  - {name}")
    if only_in_sub:
        print("📁 副文件夹中多出的子文件夹：")
        for name in sorted(only_in_sub, key=natural_sort_key):
            print(f"  - {name}")
    if not only_in_main and not only_in_sub:
        print("✅ 子文件夹结构完全一致。")

    for folder in sorted(in_both, key=natural_sort_key):
        main_path = os.path.join(main_dir, folder)
        sub_path = os.path.join(sub_dir, folder)
        diff = filecmp.dircmp(main_path, sub_path)

        if diff.left_only or diff.right_only or diff.diff_files:
            print(f"\n📂 子文件夹 '{folder}' 有差异：")
            if diff.left_only:
                print(f"  📁 主文件夹中多出的文件： {sorted(diff.left_only, key=natural_sort_key)}")
            if diff.right_only:
                print(f"  📁 副文件夹中多出的文件： {sorted(diff.right_only, key=natural_sort_key)}")
            if diff.diff_files:
                print(f"  🧾 文件内容不同： {sorted(diff.diff_files, key=natural_sort_key)}")

if __name__ == "__main__":
    main_folder = r"D:\Download\all0804-1000-5000"  # 修改为你的主文件夹路径
    sub_folder = r"D:\Download\all0804-1000-5000 - 副本"    # 修改为你的副文件夹路径
    compare_folders(main_folder, sub_folder)
