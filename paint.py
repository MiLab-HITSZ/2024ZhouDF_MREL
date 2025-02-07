import os
os.environ["CUDA_VISIBLE_DEVICES"] = "4"
import matplotlib.pyplot as plt
import pandas as pd
num_acs=[]
import os
import re
import pandas as pd
import matplotlib.pyplot as plt

folder_path = '/home/zq/projects/FreeEagle/record/cifar-vgg16/csv/target0'

def extract_number_from_filename(filename):
    # 使用正则表达式提取文件名中的数字部分
    match = re.search(r'(\d+)', filename)
    if match:
        return int(match.group())
    else:
        return None
plt.figure(figsize=(10, 6))
# 循环处理每个CSV文件
csv_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.csv')])
for csv_file in csv_files:
    csv_path = os.path.join(folder_path, csv_file)

    # 从CSV文件读取数据
    df = pd.read_csv(csv_path)

    # 提取数据列
    confidence_values = df['confidence'].tolist()

    # 横坐标：序号乘以50
    x_values = [i * 50 for i in range(len(confidence_values))]

    # 限制横坐标范围不超过4096
    x_values = [x for x in x_values if x <= 4096]

    # 纵坐标：浮点数
    y_values = confidence_values[:len(x_values)]

    # 绘制曲线
    number = extract_number_from_filename(csv_file)
    label_name = f"Class {number}" if number is not None else "Unknown Curve"
    plt.plot(x_values, y_values,label=label_name)

# 设置图形属性
plt.title('Confidence of Every Class in Backdoor VGG16 Model (target=0)',fontsize=15)
plt.xlabel('Number of Masked Factors',fontsize=15)
plt.ylabel('Confidence',fontsize=15)
plt.legend()
plt.savefig('output_vgg16_target0.png')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()
