# test_script.py
import json
import sys

def main():
    # 接收来自 Java 的 JSON 数据
    if len(sys.argv) > 1:
        json_data = sys.argv[1]
        try:
            # 解析 JSON 数据
            data = json.loads(json_data)
            print("Received JSON data:", data)

            # 假设我们处理一些数据并生成新的结果
            processed_data = {"status": "success", "message": "Data processed", "original_data": data}

            # 返回处理结果
            print(json.dumps(processed_data))
        except json.JSONDecodeError as e:
            print(json.dumps({"status": "error", "message": f"Invalid JSON format: {e}"}))
    else:
        print(json.dumps({"status": "error", "message": "No data received"}))

if __name__ == "__main__":
    main()
