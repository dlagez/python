
from paddleocr import PaddleOCR

ocr = PaddleOCR(
    use_doc_orientation_classify=False, 
    use_doc_unwarping=False, 
    use_textline_orientation=False)

# result = ocr.predict(r"D:\Download\dayu5000\testpdf\test4.pdf")
result = ocr.predict(r"D:\Download\all07162\(父)济南遥墙机场配套设施项目C6-05地块3#旅客过夜用房精装修施工总承包\合同最终附件列表\济南遥墙机场配套设施项目C6-05地块3旅客过夜用房精装修施工总承包（终版扫描件）.pdf")


# for res in result:
#     res.print()
#     res.save_to_img("output")
#     res.save_to_json("output")


# 提取纯文本并保存到 txt 文件
with open("output/text_only2.txt", "w", encoding="utf-8") as f:
    for res in result:
        json_data = res.json  # 获取结果的 dict 格式
        json_data = json_data.get('res')
        for rec_text in json_data.get("rec_texts", []):
            f.write(rec_text + "\n")

