import os    
import pandas as pd
#获取该目录下所有文件，存入列表中
path = r'C:\Users\roc\OneDrive\Desktop\武汉大区简历2\武汉大区简历2'
fileList=os.listdir(path)


df = pd.read_excel('wuhan.xlsx', converters={'姓名':str, '组别':str})

for i in df.index:
    name = df['姓名'][i]
    zubie = df['组别'][i]
    for filename in fileList:
        if name in filename:
            
            #设置旧文件名（就是路径+文件名）
            oldname=path+ os.sep + filename   # os.sep添加系统分隔符
            
            #设置新文件名
            newname=path + os.sep + name+'-'+zubie+'.docx'
            os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
            print(oldname,'======>',newname)
        
        
