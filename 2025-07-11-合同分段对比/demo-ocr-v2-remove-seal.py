import cv2
import numpy as np
from paddleocr import PaddleOCR
import fitz  # PyMuPDF，用于PDF处理
import os

def remove_seal(image):
    """
    去除图像中的红色印章
    """
    # 转换为HSV颜色空间，更容易识别红色
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # 定义红色的HSV范围（红色在HSV中分为两个区域）
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    
    # 创建红色掩码
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2
    
    # 对掩码进行形态学操作，填充印章内部并去除小噪点
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    
    # 使用掩码进行修复，去除印章
    result = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)
    return result

def process_pdf(pdf_path, output_dir="output"):
    """
    处理PDF文件，去除印章后进行OCR识别
    """
    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 初始化OCR
    ocr = PaddleOCR(
        use_doc_orientation_classify=False, 
        use_doc_unwarping=False, 
        use_textline_orientation=False
    )
    
    # 打开PDF文件
    doc = fitz.open(pdf_path)
    results = []
    
    # 逐页处理
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap()
        
        # 转换为OpenCV格式
        img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, pix.n)
        if pix.n == 4:  # 如果是RGBA格式，转换为RGB
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # 去除印章
        processed_img = remove_seal(img)
        
        # 保存处理后的图像
        output_img_path = os.path.join(output_dir, f"page_{page_num+1}_processed.jpg")
        cv2.imwrite(output_img_path, processed_img)
        
        # 进行OCR识别
        result = ocr.predict(processed_img)
        
        # 保存结果
        results.append(result)
        
        # 打印当前页的识别结果
        print(f"Page {page_num+1} OCR Result:")
        for line in result[0]:
            print(line)
        
        # 保存为JSON和图像
        # result_obj = ocr.postprocess_outputs(result, output_img_path)
        # result_obj.save_to_img(output_dir)
        # result_obj.save_to_json(output_dir)
    
    doc.close()
    return results

# 主函数
if __name__ == "__main__":
    pdf_path = r"D:\Download\dayu5000\testpdf\test4.pdf"
    results = process_pdf(pdf_path)
    print(results)
    print("处理完成！结果已保存到output目录")