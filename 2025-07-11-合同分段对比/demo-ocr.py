
from paddleocr import PaddleOCR

ocr = PaddleOCR(
    use_doc_orientation_classify=False, 
    use_doc_unwarping=False, 
    use_textline_orientation=False)

result = ocr.predict(r"D:\Download\dayu5000\testpdf\test4.pdf")


for res in result:
    res.print()
    res.save_to_img("output")
    res.save_to_json("output")

