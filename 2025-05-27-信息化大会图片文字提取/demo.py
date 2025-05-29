import os
import cv2
from paddleocr import PaddleOCR

# 初始化 OCR（使用中文和英文，开启静默模式）
ocr = PaddleOCR(use_angle_cls=True, lang="ch")

# 设置图片所在文件夹
image_folder = r'D:\hysz\Archive_jpg'  # 替换为你实际的文件夹路径
output_file = r'D:\hysz\output_all.txt'

# 获取所有 JPG 文件，按名称排序
jpg_files = sorted([f for f in os.listdir(image_folder) if f.lower().endswith('.jpg')])

with open(output_file, 'w', encoding='utf-8') as outfile:
    for filename in jpg_files:
        image_path = os.path.join(image_folder, filename)
        try:
            print(image_path)
            results = ocr.predict(image_path)
            # results 是包含一个字典的列表
            if results and isinstance(results[0], dict):
                rec_texts = results[0].get('rec_texts', [])
                lines = [text for text in rec_texts if text.strip()]  # 去除空文本

                # 写入结果
                outfile.write('\n'.join(lines))
                outfile.write(f'\n[图片文件名: {filename}]\n\n\n')
                print(f"已完成：{filename}")
            else:
                print(f"未识别到内容：{filename}")
        except Exception as e:
            print(f"跳过 {filename}，出错：{e}")

print(f"\n完成！结果已写入：{output_file}")

