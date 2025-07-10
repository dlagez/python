import os
import requests

# ====== 配置区 ======
API_KEY = 'app-YZHlycEoDIa6ov4lLGoIlK9C'
USER_ID = 'abc-123'
UPLOAD_URL = 'https://dev-dify.hysz.co/v1/files/upload'
TEST_FILE = r'D:\data\所有合同\(父)建始县国家储备林建设项目(EPC)\合同创建附件列表\主文件：主合同(建始县国家储备林建设项目（EPC） ）2023-10-20）.docx'  # 替换为你的真实文件路径

# ====== 上传函数 ======
def test_upload(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"文件不存在：{filepath}")
    headers = {'Authorization': f'Bearer {API_KEY}'}
    data = {'user': USER_ID}
    with open(filepath, 'rb') as f:
        files = {'file': (os.path.basename(filepath), f, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')}  # 避免文件名编码问题
        response = requests.post(UPLOAD_URL, headers=headers, files=files, data=data)
    response.raise_for_status()
    print("✅ 上传成功！响应结果如下：")
    print(response.json())

# ====== 执行上传 ======
if __name__ == '__main__':
    try:
        test_upload(TEST_FILE)
    except Exception as e:
        print(f"❌ 上传失败：{e}")
