# 001-Pillow安装成功但from报错

## 1. 出现场景

我安装完 Pillow 后，在 PyCharm 终端里输入：

```powershell
from PIL import Image
```

结果报错。

## 2. 报错原文

```text
此语言版本中不支持 “from” 关键字。
```

## 3. 报错位置

- 报错位置：PowerShell 终端
- 当前目录：backend
- 虚拟环境：.venv

## 4. 原因解释

`from PIL import Image` 是 Python 代码，不能直接在 PowerShell 里运行。

PowerShell 看到 `from`，会把它当成 PowerShell 语法，所以报错。

## 5. 解决方法

方法一：进入 Python 解释器：

```powershell
python
```

看到 `>>>` 后再输入：

```python
from PIL import Image
```

方法二：直接在 PowerShell 里执行：

```powershell
python -c "from PIL import Image; print('Pillow 正常')"
```

## 6. 下次怎么判断

如果前面是：

```text
PS C:\Users\...\backend>
```

说明当前是 PowerShell，不是 Python 环境。

如果前面是：

```text
>>>
```

说明当前是 Python 环境。

## 7. 相关知识点

- PowerShell
- Python 解释器
- Pillow
- 虚拟环境
