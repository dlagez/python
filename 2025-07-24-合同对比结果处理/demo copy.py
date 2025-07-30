import pandas as pd
#合并两个excel

# 读取主表和附表
main_df = pd.read_excel(r"D:\Download\dayu5000\全量匹配结果v2.xlsx")
attach_df = pd.read_excel(r"D:\Download\dayu5000\项目金额和结算情况2.xlsx")

# 去除可能存在的空格和换行，确保匹配稳定
main_df["合同名称"] = main_df["合同名称"].astype(str).str.strip()
attach_df["项目部"] = attach_df["项目部"].astype(str).str.strip()

# 进行合并，主表“合同名称” 对应 附表“项目部”
merged_df = pd.merge(main_df, attach_df, how="left", left_on="合同名称", right_on="项目部")

# 用附表中的“合同金额”替换“合同总金额”
merged_df["合同总金额"] = merged_df["合同金额"]

# 插入“分子公司”和“结算情况”列到“合同总金额”后面
cols = list(merged_df.columns)
insert_index = cols.index("合同总金额") + 1
for col in ["分子公司", "结算情况"]:
    cols.insert(insert_index, col)
    insert_index += 1
merged_df = merged_df[cols]

# 删除多余的“项目部”和“合同金额”列
merged_df.drop(columns=["项目部", "合同金额"], inplace=True)

# 保存合并后的新文件
merged_df.to_excel(r"D:\Download\dayu5000\合并后结果.xlsx", index=False)
