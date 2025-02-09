# 后门模型信息

1. **模型和数据集存储位置**：
   - 在服务器上，各种类型的后门模型已经提前训练好，存储路径为：`/projects/FreeEagle/backdoor_attack_simulation/saved_models`。
   - GitHub上模型和数据集难以上传，演示时请将服务器`/projects/FreeEagle/backdoor_attack_simulation`文件夹带上。

2. **主要运行代码**：
   - 运行代码为 `mydata_free.py`，用户可以自行修改参数。
   - **参数说明**：
     - `model`：模型类型
     - `n_cls`：分类数量
     - `size`：图像大小
     - `ckpt`：所检查的模型的地址
     - `num_important_neurons`：每次遮住的特征元素颗粒度（例如，vgg16模型建议选50，googlenet选20）

   - **输出**：
     - 在代码的第412行，会输出`n_cls`个csv文件，这些文件分别表示每个类对应的遮蔽元素数量和分类置信度的关系。

3. **额外功能**：
   - 如果在演示时需要可视化，可以使用 `piant.py` 文件将csv文件作为输入，从而得到坐标图。




