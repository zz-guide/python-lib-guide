# opencv

## 安装
在Python中安装cv2（即OpenCV库）可以通过pip进行。以下是安装命令：

```shell
pip install opencv-python
```

如果你需要包含完整的OpenCV功能（包括视频处理等），你可以安装带有额外贡献库的版本：

```shell
pip install opencv-python-headless
```

或者，如果你需要包含OpenCV的完整功能，包括GUI接口等，可以安装带有额外贡献库的版本：

```shell
pip install opencv-contrib-python
```

或者对于不需要GUI功能的服务器版本：

```shell
pip install opencv-contrib-python-headless
```

安装完成后，你可以通过以下Python代码来验证是否成功安装了cv2：

```python
import cv2
```

# 输出OpenCV版本
print(cv2.__version__)