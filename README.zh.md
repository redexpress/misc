# misc

[简体中文](README.zh.md) | [English](README.md)

一些零散的小工具和参考文件合集。

## 目录说明

### `chinese/`

用于处理 **GB2312** 中文字符编码的小工具集。

- `print2312.py` — 用于生成 GB2312 “区—位” 码对照表的 Python 脚本。
- `gb2312.xlsx` — GB2312 汉字的参考电子表格。
- `gb2312_gbk.csv` — 由 `print2312.py` 生成的 CSV 表，包含所有已定义的 GB2312 码点（以 GBK 编码，未定义的区/位留空）。
- `gb2312_utf8.txt` — 与 `gb2312_gbk.csv` 内容相同，但转换为 UTF-8 编码，并将逗号替换为空格，便于在纯文本编辑器中查看或搜索。
