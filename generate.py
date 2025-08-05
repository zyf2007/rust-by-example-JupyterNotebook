import os
import re
import json
from pathlib import Path

def get_index_mapping(index_text):
    """解析索引文本，生成文件名到序号的映射"""
    mapping = {}
    level_counts = []
    pattern = re.compile(r'^(\s*)- \[(.*?)\]\((.*?)\)$')

    for line in index_text.split('\n'):
        if not line.strip():
            continue

        match = pattern.match(line)
        if not match:
            continue

        indent, title, path = match.groups()
        level = len(indent) // 2 

        # 保证level_counts长度等于当前层级+1
        while len(level_counts) <= level:
            level_counts.append(0)
        # 当前层级计数+1，低层级清零
        level_counts[level] += 1
        for i in range(level + 1, len(level_counts)):
            level_counts[i] = 0

        # 生成编号字符串
        nums = [str(level_counts[i]) for i in range(level + 1)]
        num_str = "_".join(nums)
        mapping[path] = num_str
    print(mapping)
    return mapping




def md_to_ipynb(md_content): 
    """将Markdown内容转换为ipynb格式的JSON数据"""
    cells = []
    current_md = []
    in_code_block = False
    current_code = []
    code_language = "rust"
    
    for line in md_content.split('\n'):
        # 检查代码块开始
        if line.startswith("```"):
            if in_code_block:
                # 代码块结束
                in_code_block = False
                # 添加Markdown单元格（如果有内容）
                if current_md:
                    cells.append({
                        "cell_type": "markdown",
                        "metadata": {},
                        "source": [line + "\n" for line in current_md]
                    })
                    current_md = []
                
                # 添加代码单元格
                # 处理Rust代码：如果是main函数，添加main()调用
                code_source = [line + "\n" for line in current_code]
                if code_language == "rust" and any("fn main()" in c for c in current_code):
                    code_source.append("main();\n")
                
                cells.append({
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {
                        "vscode": {
                            "languageId": code_language
                        }
                    },
                    "outputs": [],
                    "source": code_source
                })
                current_code = []
                code_language = "rust"
            else:
                # 代码块开始
                in_code_block = True
                # 提取代码语言（如```rust,editable）
                lang_part = line[3:].strip().split(',')[0]
                if lang_part:
                    code_language = lang_part
        else:
            # 根据是否在代码块中添加到不同的缓冲区
            if in_code_block:
                current_code.append(line)
            else:
                current_md.append(line)
    
    # 添加剩余的Markdown内容
    if current_md:
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [line + "\n" for line in current_md]
        })
    
    # 构建完整的ipynb结构
    ipynb_data = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Rust",
                "language": "rust",
                "name": "rust"
            },
            "language_info": {
                "codemirror_mode": "rust",
                "file_extension": ".rs",
                "mimetype": "text/rust",
                "name": "Rust",
                "pygment_lexer": "rust",
                "version": ""
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    
    return ipynb_data

def process_files(index_path, input_dir, output_dir):
    with open(index_path, 'r', encoding='utf-8') as f:
        index_text = f.read()
    index_mapping = get_index_mapping(index_text)
    
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 处理每个Markdown文件
    for md_path, num in index_mapping.items():
        full_md_path = os.path.join(input_dir, md_path)
        
        if not os.path.exists(full_md_path):
            print(f"警告：文件不存在 - {full_md_path}")
            continue
        
        # 读取Markdown内容
        with open(full_md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # 转换为ipynb
        ipynb_data = md_to_ipynb(md_content)
        
        # 生成输出文件名和路径
        md_filename = os.path.basename(md_path)
        ipynb_filename = f"{num}_{os.path.splitext(md_filename)[0]}.ipynb"
        
        # 找到这个文件对应的子目录的索引值
        md_dir = os.path.dirname(md_path)
        if md_dir:
            dir_index = None
            for path, num in index_mapping.items():
                if os.path.dirname(path) == "" and os.path.basename(path) == f"{os.path.basename(md_dir)}.md":
                    dir_index = num
                    break
            # 拼接编号前缀目录名
            if dir_index:
                dir_name = os.path.basename(md_dir)
                indexed_dir = f"{dir_index}_{dir_name}"
            else:
                indexed_dir = md_dir
            output_subdir = os.path.join(output_dir, indexed_dir)
        else:
            output_subdir = output_dir

        os.makedirs(output_subdir, exist_ok=True)
        
        # 保存ipynb文件
        output_path = os.path.join(output_subdir, ipynb_filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(ipynb_data, f, ensure_ascii=False, indent=2)
        
        print(f"已生成：{output_path}")

if __name__ == "__main__":
    INDEX_PATH = "../rust-by-example-cn/src/SUMMARY.md"
    INPUT_DIR = "../rust-by-example-cn/src/"
    OUTPUT_DIR = "Notebooks" 
    
    process_files(INDEX_PATH, INPUT_DIR, OUTPUT_DIR)
    print("转换完成！")