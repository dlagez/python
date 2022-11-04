# os: macOS 12.5.1 (21G83)
# author roczhang
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import StrMethodFormatter
mpl.rcParams['lines.linewidth'] = 2
plt.rcParams['font.sans-serif']=['Songti SC'] 
plt.rcParams['axes.unicode_minus']=False 
plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.2f}'))
plt.locator_params(axis='y', nbins=10)
datax1 = [98.42, 98.65, 98.94, 99.34, 99.5, 99]
datay1 = [3, 4, 5, 6, 7, 8]
plt.plot(datay1, datax1, marker='o', markersize=5, label='Indian Pines')

datax2 = [ 96.53, 97.01, 97.24, 97.63, 97.89, 96.85]
datay2 = [3, 4, 5, 6, 7, 8]
plt.plot(datay2, datax2, marker='v', markersize=5, label='Pavia University')
plt.ylim((94, 100))
plt.legend()#显示图例，如果注释改行，即使设置了图例仍然不显示
plt.ylabel('OA(%)')
plt.xlabel(u'网络的深度')
plt.show()
plt.savefig('parameter-analysis2.png', dpi=600)