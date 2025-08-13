import os
import subprocess
import sys
import re

# 配置路径（使用绝对路径）
HASHCAT_PATH = os.path.abspath(r"D:\app\hashcat-7.0.0\hashcat.exe")
OFFICE2HASHCAT = os.path.abspath(r"2025-08-11-hashcat/office2john.py")
WORD_FILE = os.path.abspath(r"d:\Download\file\加密文档.docx")
DICTIONARY = os.path.abspath(r"2025-08-11-hashcat/rockyou.txt")
OUTPUT_FILE = os.path.abspath(r"2025-08-11-hashcat/cracked.txt")
HASH_FILE = os.path.abspath("hash.txt")

# 确保 Hashcat 目录存在
if not os.path.exists(os.path.dirname(HASHCAT_PATH)):
    print(f"[!] Hashcat 路径不存在：{os.path.dirname(HASHCAT_PATH)}")
    sys.exit(1)

# Step 1: 提取哈希
print("[*] 提取 Word 哈希...")
try:
    raw_bytes = subprocess.check_output(
        ["python", OFFICE2HASHCAT, WORD_FILE],
        stderr=subprocess.STDOUT
    )
    text = raw_bytes.decode("latin-1")
    match = re.search(r"\$office\$.*", text)
    if not match:
        print("[!] 没有提取到哈希，请确认文件是否加密。")
        sys.exit(1)

    hash_data = match.group(0)
    with open(HASH_FILE, "w", encoding="utf-8") as f:
        f.write(hash_data + "\n")
    print(f"[+] 哈希已保存到 {HASH_FILE}: {hash_data}")

except subprocess.CalledProcessError as e:
    print("[!] 提取哈希失败：", e.output.decode("utf-8", errors="ignore"))
    sys.exit(1)

# Step 2: 调用 Hashcat 破解
hash_mode = "9600"
print("[*] 开始调用 Hashcat 破解...")

try:
    # 切换到 Hashcat 目录
    os.chdir(os.path.dirname(HASHCAT_PATH))
    ret = subprocess.run([
        HASHCAT_PATH,
        "-m", hash_mode,
        "-a", "0",
        HASH_FILE,
        DICTIONARY,
        "-o", OUTPUT_FILE,
        "--opencl-device-types", "1"
    ], capture_output=True, text=True)

    print("Hashcat 输出：\n", ret.stdout)
    if ret.stderr:
        print("Hashcat 错误：\n", ret.stderr)

    if ret.returncode == 0:
        print(f"[+] 破解完成，结果保存在 {OUTPUT_FILE}")
    else:
        print(f"[!] Hashcat 运行失败，返回码：{ret.returncode}")

    # Step 3: 显示已破解密码
    print("[*] 已破解密码：")
    ret = subprocess.run([HASHCAT_PATH, "-m", hash_mode, "--show", HASH_FILE], capture_output=True, text=True)
    print(ret.stdout)
    if ret.stderr:
        print("错误：", ret.stderr)

except Exception as e:
    print("[!] 运行 Hashcat 失败：", e)
    sys.exit(1)