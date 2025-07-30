import os

# 设置主目录
base_dir = r"D:\your_path\all0716"  # 替换为你的 all0716 路径
size_threshold_mb = 40

# 检查合同是否超过40M

# 转换为字节
size_threshold_bytes = size_threshold_mb * 1024 * 1024

# 统计
large_pdfs = []

# 遍历所有项目子文件夹
for root, dirs, files in os.walk(base_dir):
    if os.path.basename(root) == "合同最终附件列表":
        for file in files:
            if file.lower().endswith(".pdf"):
                file_path = os.path.join(root, file)
                try:
                    file_size = os.path.getsize(file_path)
                    if file_size > size_threshold_bytes:
                        large_pdfs.append((file_path, file_size))
                except Exception as e:
                    print(f"❌ 无法读取 {file_path}，原因：{e}")

# 输出结果
if large_pdfs:
    print(f"\n📄 大于 {size_threshold_mb}MB 的 PDF 文件列表：\n")
    for path, size in large_pdfs:
        print(f"{path} —— {round(size / (1024 * 1024), 2)} MB")
else:
    print(f"✅ 所有合同 PDF 均小于 {size_threshold_mb}MB")
