# Rust-by-Example (Jupyter Notebook Edition)
[简体中文](README.md)/English  

Convert the content of the "Rust-by-Example" book into Jupyter Notebook format, allowing you to learn Rust programming more efficiently in any IDE/editor that supports Jupyter. The repository contains the converted Chinese book files in the `Notebooks` directory.

**If your preferred language is not Chinese, you can download `generate.py` and then clone the book version in your own language. Before using this script to generate .ipynb files, remember to modify the book source file storage path as prompted below.**
```python
# Modify the paths in the __main__ section of the generate.py file
if __name__ == "__main__":
    INDEX_PATH = "../rust-by-example-cn/src/SUMMARY.md"
    INPUT_DIR = "../rust-by-example-cn/src/"
    OUTPUT_DIR = "Notebooks"  # Parent directory for output files
    
    process_files(INDEX_PATH, INPUT_DIR, OUTPUT_DIR)
    print("Conversion completed!")
```

## Tool Introduction

This project batch converts Markdown documents from the [rust-by-example](https://github.com/rust-lang/rust-by-example) project into Jupyter Notebook files (.ipynb), enabling you to:

- Learn Rust in your favorite IDE (such as VS Code)
- Run code blocks directly without relying on the official website environment (the one on `doc.rust-lang.org/stable/rust-by-example/` is a bit slow, isn't it?)
- Preserve the original book's chapter structure and content formatting (the generated filenames include indexes ↓)

```bash
❯ tree ./JupyterNotebooks
./JupyterNotebooks
├── 1_hello
│   ├── 1_1_comment.ipynb
│   └── 1_2_print.ipynb
├── 2_primitives
│   ├── 2_1_literals.ipynb
│   ├── 2_2_tuples.ipynb
│   └── 2_3_array.ipynb
├── 3_custom_types
│   ├── 3_1_structs.ipynb
│   ├── 3_2_enum.ipynb
│   └── 3_3_constants.ipynb
├── 4_variable_bindings
│   ├── 4_1_mut.ipynb
│   ├── 4_2_scope.ipynb
│   ├── 4_3_declare.ipynb
│   └── 4_4_freeze.ipynb
...
```


## Usage

### Prerequisites

- Jupyter lab environment installed
- Rust development environment (I use rustup)

### Steps

1. Clone this repository

```bash
git clone https://github.com/zyf2007/rust-by-example-JupyterNotebook.git
```

2. Clone the rust-by-example project (or use an existing clone)

```bash
git clone https://github.com/rust-lang/rust-by-example.git
```

3. Modify the path configuration in the script (generate.py)

```python
# Modify the paths in the __main__ section of the generate.py file
INDEX_PATH = "../rust-by-example/src/SUMMARY.md"  # Path to the index file
INPUT_DIR = "../rust-by-example/src/"            # Root directory of Markdown files
OUTPUT_DIR = "JupyterNotebooks"                  # Output directory
```

4. Run the conversion script

```bash
python generate.py
```

5. Configure the Rust interactive interpreter for Jupyter
```bash
cargo install evcxr_jupyter
evcxr_jupyter --install
```

6. Find the converted .ipynb files in the generated `JupyterNotebooks` directory and open them with your favorite editor to start learning!


## Contribution

Issues and pull requests are welcome to improve this tool!