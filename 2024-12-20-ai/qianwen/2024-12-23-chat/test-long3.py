import os
from openai import OpenAI
import time

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
start_time = time.time()
completion = client.chat.completions.create(
    model="qwen-long",
    messages=[
        {'role': 'system', 'content': '你是一个合同审批人员，需要对合同进行审批，找出合同中异常的部分，以合同数据为基准.'},
        # {'role': 'system', 'content': '直接输出结果，不需要解析过程，精炼输出，并将输出控制在50-100字.'},
        # {'role': 'system', 'content': 'fileid://file-fe-DFOhTK7DfuzvAAcT5xITaNaY'},
        {'role': 'system', 'content': f'fileid://file-fe-91ERzUJNxmXugxQ5OnOgbFIV,fileid://file-fe-l9e6dOOb04bGHYb36bnqhuN0'},
        {'role': 'user', 'content': '''我现在是审批人员,需要审批图片，请找出图片上的差异，并给出相应的建议'''}
    ],
    stream=True,
    stream_options={"include_usage": True}
)

full_content = ""
for chunk in completion:
    if chunk.choices and chunk.choices[0].delta.content:
        full_content += chunk.choices[0].delta.content
        print(chunk.model_dump())

print({full_content})

end_time = time.time()
response_time = end_time - start_time
print(f"Response Time: {response_time} seconds")


# 从您提供的两份文档（图片）内容来看，它们都涉及到武汉市汉阳市政建设集团有限公司对武汉汇科智创有限公司项目的验收情况。以下是这两张图片的主要差异点  个验收文档的内容与实际交付物一致，特别是对接模型、字段说明和功能说明等关键部
# 以及相应的审批建议：\n\n### 差异点分析\n\n1. **项目名称和时间**：\n   - **文档1**：验收的是“OA综合应用系统”项目，验收日期为2024年11月25日。\n   - *步骤，可以确保验收文档的完整性和准确性，从而顺利完成审批流程。'}*文档2**：验收的是“系统中台”项目，验收日期为2024年4月17日。\n\n2. **验收文档内容**：\n   - **文档1**：涉及“数据标准集成验收文档”，包括完整的对接模 
# 型及必要的字段说明。\n   - **文档2**：涉及“门户中心集成验收文档”，提供与门户中心对接的功能说明。\n\n3. **签字部分**：\n   - **文档1**：有明确的“中 
# 方项目代表签字”和“乙方项目代表签字”，但部分签字内容模糊不清。\n   - **文档2**：乙方项目代表签字处为空白，且部分文字如“验收日期：有限公 3 S0105100210 3： null”显得混乱且不清晰。\n\n4. **格式和排版**：\n   - **文档1**：整体排版较为清晰，信息相对完整。\n   - **文档2**：存在明显的排版问题，例如“有
# 限公 3 S0105100210 3： null”等非正常字符，影响了文档的可读性和专业性。\n\n### 审批建议\n\n1. **确认项目名称和时间**：\n   - 确认两个项目是否为同一 
# 项目的不同阶段或不同模块。如果是不同的项目，确保每个项目的验收文档独立且准确无误。\n\n2. **补充和完善签字部分**：\n   - 对于**文档1**，要求提供更清
# 晰的签字图片或手写签字扫描件，确保签字真实有效。\n   - 对于**文档2**，乙方项目代表必须补签，确保所有验收文档都有完整的签字确认。\n\n3. **清理和规范
# 排版**：\n   - **文档2**中的排版问题需要立即修正，特别是去除“有限公 3 S0105100210 3： null”等无关字符，确保文档的专业性和可读性。\n\n4. **核对验收 
# 文档内容**：\n   - 确保每个验收文档的内容与实际交付物一致，特别是对接模型、字段说明和功能说明等关键部分，避免遗漏或错误描述。\n\n5. **保留清晰的电 
# 子存档**：\n   - 建议将所有验收文档整理成PDF格式，确保文档清晰可读，并便于长期保存和查阅。\n\n通过以上步骤，可以确保验收文档的完整性和准确性，从而 
# 顺利完成审批流程。'