import os
import shutil

# 我有个文件夹里面有很多子文件夹，我想使用python代码将其中的md文件选择出来，放在一个文件夹里面。

# 设置源文件夹和目标文件夹路径（确保使用合适的路径）
source_dir = r'C:\Users\admin\OneDrive\Documents\汇科智创\19-ai\2025-02-12-运维知识库的搭建\0x00 部署和配置文档\0x00 部署和配置文档'
target_dir = r'C:\Users\admin\OneDrive\Documents\汇科智创\19-ai\2025-02-12-运维知识库的搭建\0x00 部署和配置文档\md'

# 如果目标文件夹不存在，则创建它
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# 遍历源文件夹及其子文件夹
for root, dirs, files in os.walk(source_dir):
    for file in files:
        # 检查文件是否是 .md 文件
        if file.endswith('.md'):
            # 构造源文件和目标文件的路径
            source_file = os.path.join(root, file)
            target_file = os.path.join(target_dir, file)
            
            # 如果目标文件夹中已存在同名文件，则修改文件名以避免覆盖
            if os.path.exists(target_file):
                base, ext = os.path.splitext(file)
                counter = 1
                while os.path.exists(target_file):
                    target_file = os.path.join(target_dir, f"{base}_{counter}{ext}")
                    counter += 1
            
            # 复制文件到目标文件夹
            shutil.copy(source_file, target_file)
            print(f"已复制: {source_file} -> {target_file}")

print("所有 .md 文件已复制完成。")
