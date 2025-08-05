# Rust-by-Example （Jupyter Notebook 版）
简体中文/[English](README-EN.md)

将《Rust-by-Example》书籍内容转换为 Jupyter Notebook 格式，让你可以在任意支持 Jupyter 的 IDE/编辑器中更高效地学习 Rust 编程。仓库中包含转换完成的中文书籍文件，在 `Notebooks` 目录下。  

**如果你使用的语言不是中文，可以下载 `generate.py` ，然后克隆自己语言版本的书籍。在使用此脚本生成 .ipynb 文件之前，记得按照下面的提示修改书籍源文件存储路径。**
```python
# 在 generate.py 文件的 __main__ 部分修改路径
if __name__ == "__main__":
    INDEX_PATH = "../rust-by-example-cn/src/SUMMARY.md"
    INPUT_DIR = "../rust-by-example-cn/src/"
    OUTPUT_DIR = "Notebooks" # 输出文件的父目录
    
    process_files(INDEX_PATH, INPUT_DIR, OUTPUT_DIR)
    print("转换完成！")
```
## 工具简介

这个项目将 [rust-by-example](https://github.com/rust-lang/rust-by-example) 项目中的 Markdown 文档批量转换为 Jupyter Notebook 文件（.ipynb）,让你能够：

- 在你喜欢的 IDE（如 VS Code）中学习 Rust
- 直接运行代码块，无需依赖官网环境（doc.rust-lang.org 上那个运行起来有点慢不是吗）
- 保留原书的章节结构和内容排版（生成结果的文件名中带有索引↓）

```bash
❯ tree ./JupyterNotebooks
./JupyterNotebooks
├── 1_hello
│   ├── 1_1_comment.ipynb
│   └── 1_2_print.ipynb
├── 2_primitives
│   ├── 2_1_literals.ipynb
│   ├── 2_2_tuples.ipynb
│   └── 2_3_array.ipynb
├── 3_custom_types
│   ├── 3_1_structs.ipynb
│   ├── 3_2_enum.ipynb
│   └── 3_3_constants.ipynb
├── 4_variable_bindings
│   ├── 4_1_mut.ipynb
│   ├── 4_2_scope.ipynb
│   ├── 4_3_declare.ipynb
│   └── 4_4_freeze.ipynb
...
```


## 使用方法

### 前提条件

- 已安装 Jupyter lab 环境
- Rust 开发环境（我使用的是rustup）

### 步骤

1. 克隆本仓库

```bash
git clone https://github.com/zyf2007/rust-by-example-JupyterNotebook.git
```

2. 克隆 rust-by-example 项目（或使用已有克隆）

```bash
git clone https://github.com/rust-lang/rust-by-example.git
```

3. 修改脚本中的路径配置（generate.py）

```python
# 在 generate.py 文件的 __main__ 部分修改路径
INDEX_PATH = "../rust-by-example/src/SUMMARY.md"  # 索引文件路径
INPUT_DIR = "../rust-by-example/src/"            # Markdown 文件根目录
OUTPUT_DIR = "JupyterNotebooks"                  # 输出目录
```

4. 运行转换脚本

```bash
python generate.py
```
5. 配置 Rust 交互式解释器到 Jupyter
```bash
cargo install evcxr_jupyter
evcxr_jupyter --install
```
6. 在生成的 `JupyterNotebooks` 目录中找到转换后的 .ipynb 文件，用你喜欢的编辑器打开即可开始学习



## 贡献

欢迎提交 issues 和 pull requests 来改进这个工具！

