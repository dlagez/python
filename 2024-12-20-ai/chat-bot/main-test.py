from extractor import TextExtractor, get_extraction_strategy

def main():
    file_path = r'C:\Users\admin\Desktop\03-豆包.pdf'  # 替换为您的文件路径
    strategy = get_extraction_strategy(file_path)

    if strategy:
        extractor = TextExtractor(strategy)
        extracted_text = extractor.extract(file_path)
        
        if extracted_text:
            print(extracted_text)
        else:
            print("Failed to extract text.")
    else:
        print("No strategy available for this file type.")

if __name__ == '__main__':
    main()
