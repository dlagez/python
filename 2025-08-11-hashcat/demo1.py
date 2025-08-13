import os
import subprocess
import sys
import re

# 配置路径
HASHCAT_PATH = r"D:\app\hashcat-7.0.0\hashcat.exe"   # Hashcat 可执行文件路径
OFFICE2HASHCAT = r"2025-08-11-hashcat/office2john.py"    # office2hashcat.py 路径
WORD_FILE = r"d:\Download\file\加密文档.docx"  # 你的Word文件
DICTIONARY = r"2025-08-11-hashcat/rockyou.txt"     # 字典文件路径
OUTPUT_FILE = r"2025-08-11-hashcat/cracked.txt"             # 保存破解结果

# Step 1: 提取哈希
print("[*] 提取 Word 哈希...")
try:
    # 获取原始字节，不直接 decode 避免出错
    raw_bytes = subprocess.check_output(
        ["python", OFFICE2HASHCAT, WORD_FILE],
        stderr=subprocess.STDOUT
    )

    # 用 Latin-1 安全解码
    text = raw_bytes.decode("latin-1")

    # 提取 $office$ 开头的哈希
    match = re.search(r"\$office\$.*", text)
    if not match:
        print("[!] 没有提取到哈希，请确认文件是否加密。")
        sys.exit(1)

    hash_data = match.group(0)

    # 保存到 UTF-8 文件
    with open("hash.txt", "w", encoding="utf-8") as f:
        f.write(hash_data + "\n")

    print(f"[+] 哈希已保存到 hash.txt: {hash_data}")

except subprocess.CalledProcessError as e:
    print("[!] 提取哈希失败：", e.output.decode("utf-8", errors="ignore"))
    sys.exit(1)

# Step 2: 调用 Hashcat 破解
# 根据 Word 版本修改 -m 参数：
# -m 9400 → Office 2007
# -m 9500 → Office 2010/2013
# -m 9600 → Office 2016+
hash_mode = "9500"

print("[*] 开始调用 Hashcat 破解...")
try:
    ret = subprocess.run([
        HASHCAT_PATH,
        "-m", hash_mode,
        "-a", "0",
        "hash.txt",
        DICTIONARY,
        "-o", OUTPUT_FILE,
        # "--force",
        "--opencl-device-types", "1"  # 只用CPU
    ], capture_output=True, text=True)

    print("Hashcat 输出：\n", ret.stdout)
    print("Hashcat 错误：\n", ret.stderr)

    print(f"[+] 破解完成，结果保存在 {OUTPUT_FILE}")

    # Step 3: 显示已破解密码
    print("[*] 已破解密码：")
    subprocess.run([HASHCAT_PATH, "-m", hash_mode, "--show", "hash.txt"])

except Exception as e:
    print("[!] 运行 Hashcat 失败：", e)
