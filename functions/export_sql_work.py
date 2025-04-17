import os
import re
from functions.base_work import BaseWork
from collections import defaultdict


class ExportSqlWork(BaseWork):
    """Export SQL work class."""

    """
    input_file: str, input file path
    output_file: str, output file path
    chapter_reg_ex: str, regular expression for chapters
    context_filter_list: list, list of context filter
    content_replace_list: list, list of content replace
    """

    def __init__(
        self,
        input_file,
        output_file,
        chapter_reg_ex,
        context_filter_list,
        content_replace_list,
    ):
        super().__init__()
        self._input_file = input_file
        self._output_file = output_file
        self._chapter_reg_ex = chapter_reg_ex
        self._context_filter_list = context_filter_list
        self._content_replace_list = content_replace_list

    """测试正则表达式能否匹配到章节名"""

    def test_chapter_reg_ex_from_file(self, input_file, pattern):
        with open(input_file, "r", encoding="utf-8") as f:
            for line in f:
                if re.match(pattern, line):
                    self.status.emit(f"章节名匹配成功 {line.strip()}")
                    return True

        self.status.emit(f"章节名匹配失败 reg_ex: {pattern} input_file: {input_file}")
        return False
    
    def test_chapter_reg_ex_from_string(self, input_string, pattern):
        if re.match(pattern, input_string):
            self.status.emit(f"章节名匹配成功 {input_string.strip()}")
            return True

        self.status.emit(f"章节名匹配失败 reg_ex: {pattern} input_string: {input_string}")
        return False

    """获取所有章节名，和章节在文件中的位置"""
    def get_chapter_list(self, input_file, pattern):
        chapter_list = []

        with open(input_file, "r", encoding="utf-8") as f:
            current_byte = 0  # 记录当前字节位置
            line_number = 0  # 记录行号

            while True:
                line_start = current_byte  # 记录行首字节位置
                line = f.readline()
                if not line:
                    break

                # 匹配章节标题
                match = re.match(pattern, line.strip())
                if match:
                    s ,s1  = match.groups()
                    chapter_name = match.group()
                    chapter_list.append(
                        {
                            "name": chapter_name,
                            "line": line_number,
                            "byte_position": line_start,
                        }
                    )

                current_byte = f.tell()  # 更新当前字节位置
                line_number += 1

        return chapter_list

    def jump_to_chapter(self, file_path, target_byte):
        with open(file_path, "r", encoding="utf-8") as f:
            f.seek(target_byte)  # 跳转到指定字节位置
            print("tiaozhuan: ", f.readline())  # 读取章节标题行

    """打开一个文件，获取章节和内容，记录在对应的字典中"""

    def _get_chapter_content(self):
        chapter_content_dict = {}
        with open(self._input_file, "r", encoding="utf-8") as f:
            chapter_content = ""
            for line in f:
                if re.match(self._chapter_reg_ex, line):
                    chapter_content_dict[line.strip()] = chapter_content.strip()
                    chapter_content = ""
                else:
                    chapter_content += line.strip()
        chapter_content_dict[line.strip()] = chapter_content.strip()
        return chapter_content_dict


if __name__ == "__main__":
    input_file = r"C:\Users\jingchao\Desktop\jt\北宋穿越指南(1-500章).txt"
    work = ExportSqlWork(
        input_file,
        r"d:\code\NovelTools\test_data\test_output.txt",
        r"^\s*第\s*\d+\s*章\s*$",
        [],
        [],
    )
    chapter_list = work.get_chapter_list(input_file, r"^(\d{4})【([\u4e00-\u9fff]+)】$")
    print()

    for chapter_pos in chapter_list:
        print(chapter_pos)
        work.jump_to_chapter(input_file, chapter_pos["byte_position"])
