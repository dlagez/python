import os
import random
import glob

# 将数据集分类训练集和测试集，并将文件名写入txt文件
BASE = '/Volumes/roczhang/code/python/pytorch_classification/data/'
traindata_path = BASE + 'train'
labels = os.listdir(traindata_path)
valdata_path = BASE + 'test'
##写train.txt文件
txtpath = BASE
# print(labels)
for index, label in enumerate(labels):
    imglist = glob.glob(os.path.join(traindata_path,label, '*.png'))
    # print(imglist)
    random.shuffle(imglist)
    print(len(imglist))
    trainlist = imglist[:int(0.8*len(imglist))]
    vallist = imglist[(int(0.8*len(imglist))+1):]
    with open(txtpath + 'train.txt', 'a')as f:
        for img in trainlist:
            # print(img + ' ' + str(index))
            f.write(img + ' ' + str(index))
            f.write('\n')

    with open(txtpath + 'val.txt', 'a')as f:
        for img in vallist:
            # print(img + ' ' + str(index))
            f.write(img + ' ' + str(index))
            f.write('\n')


imglist = glob.glob(os.path.join(valdata_path, '*.jpg'))
with open(txtpath + 'test.txt', 'a')as f:
    for img in imglist:
        f.write(img)
        f.write('\n')