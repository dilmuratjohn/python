import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn import preprocessing

stats = pd.read_excel('all.xlsx', sheet_name='stats')
fault = pd.read_excel('all.xlsx', sheet_name='fault')
# 数据框基本信息
stats.info()
fault.info()

fault_start1 = []
fault_end1 = []
fault_start2 = []
fault_end2 = []
for i in fault.index:
    if '氨泵故障状态' in fault.loc[i, '故障名称']:
        fault_start1.extend(fault.loc[[i], '故障开始时间'])
        fault_end1.extend(fault.loc[[i], '故障结束时间'])
    if '冷间漏氨报警' in fault.loc[i, '故障名称']:
        fault_start2.extend(fault.loc[[i], '故障开始时间'])
        fault_end2.extend(fault.loc[[i], '故障结束时间'])

# 将记录时间作为数据框索引
stats = stats.set_index("记录时间", drop=True)
stats.describe()
# 箱线图
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
column_names = ['低压桶液位', '贮氨器液位', '低压桶压力', '贮氨器压力', '室外温度', '室外湿度', '冷凝器回液温度', '低压桶大库出液温度', '低压桶制冰出液温度', '低压桶大库回气温度', '低压桶制冰回气温度']
fig = plt.figure(1, figsize=(20, 10))
box = fig.add_subplot(111)
plt.boxplot(stats.T[0:11],
            notch=True,
            sym='r*',
            vert=False,
            showmeans=True,
            patch_artist=True,
            boxprops={'color': 'black', 'facecolor': '#eefff1'},
            flierprops={'marker': 'o', 'markerfacecolor': 'red', 'color': 'black'},
            meanprops={'marker': 'D', 'markerfacecolor': 'indianred'},
            medianprops={'linestyle': '--', 'color': 'blue'}
            )

plt.title('监测数据箱线图')
box.set_yticklabels(column_names)
plt.savefig("box.png")
plt.show()

# 散点图
sns.pairplot(stats, diag_kind='kde', size=2)
plt.savefig("pairplot.png")
plt.show()

# 数据直方图
stats.hist(xlabelsize=7, ylabelsize=7, figsize=(20, 20))
plt.savefig("hist.png")
plt.show()

# 密度图矩阵
stats.plot(kind='density', subplots=True, layout=(3, 4), sharex=False, fontsize=8, figsize=(20, 20))
plt.savefig("density.png")
plt.show()

# 绘制相关系数图
correlations = stats.corr()  # 计算变量之间的相关系数矩阵
fig = plt.figure(1, figsize=(20, 10))  # 调用figure创建一个绘图对象
ax = fig.add_subplot(111)
sns.heatmap(correlations, linewidths=0.05, ax=ax, vmax=1, vmin=-1)
ticks = np.arange(0.5, 11, 1)  # 生成0-9，步长为1
ax.set_xticks(ticks)  # 生成刻度
ax.set_yticks(ticks)
ax.set_xticklabels(column_names)  # 生成x轴标签
ax.set_yticklabels(column_names)
plt.savefig("correlation.png")
plt.show()

# 绘制平行坐标图
data_para = stats
scaler = preprocessing.StandardScaler()
data_para = scaler.fit_transform(data_para)
# 筛选故障时间
data_para = pd.DataFrame(data_para)
data_para = data_para.set_index(stats.index)
data_para.columns = stats.columns
# 将故障状态置1
data_para['运行状态'] = '运行正常'
for i in (range(0, len(fault_start1))):
    data_para.loc[fault_start1[i]:fault_end1[i], '运行状态'] = '低压桶氨泵故障'

for i in (range(0, len(fault_start2))):
    data_para.loc[fault_start2[i]:fault_end2[i], '运行状态'] = '冷间漏氨'

data_para['运行状态'].value_counts()

# 绘制平行坐标图
plt.figure(1, figsize=(20, 10))
fig = pd.plotting.parallel_coordinates(data_para, class_column='运行状态', color=sns.color_palette())
plt.show()

