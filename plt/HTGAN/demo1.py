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
datax1 = [95.3, 96.3, 96.8, 97, 98.59, 99.5, 99, 98, 96.5]
datay1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
plt.plot(datay1, datax1, marker='o', markersize=5, label='Indian Pines')

datax2 = [93.90, 94.10, 94.57, 95.12, 95.67, 96.54, 97.89, 96.85, 93.34]
datay2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
plt.plot(datay2, datax2, marker='v', markersize=5, label='Pavia University')
plt.ylim((92, 100))
plt.legend()#显示图例，如果注释改行，即使设置了图例仍然不显示
plt.ylabel('OA(%)')
plt.xlabel(u'ST占百分比')
plt.show()
plt.savefig('parameter-analysis.png', dpi=600)