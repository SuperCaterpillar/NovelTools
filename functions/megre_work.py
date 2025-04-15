import os
import re

from collections import defaultdict

from PySide6.QtCore import QObject, Signal, Slot
# from functions.config import RootConfig


class MergeWorker(QObject):
    progress = Signal(int)
    status = Signal(str)
    finished = Signal()
    error = Signal(str)

    # {novel_name: [(start, end, filepath),...],...}
    def __init__(
        self, output_path: str, input_path: str, file_RegEx: str, is_single_file=False
    ):
        super(MergeWorker, self).__init__()
        self._is_single_file = is_single_file
        self._output_path = output_path
        self._input_path = input_path
        self._file_RegEx = file_RegEx
        self._progressCount = 0
        self._is_cannelled = False
        self._fileDict: defaultdict[list]

    @property
    def IsSingleFile(self):
        return self._is_single_file

    @property
    def fileRegEx(self):
        return self._fileRegEx

    @property
    def IsCannelled(self):
        return self._is_cannelled
    
    def Cannelled(self):
        self._is_cannelled = True

    def get_all_file(self) -> defaultdict[list]:
        if not os.path.isdir(self._input_path):
            self.error.emit("没有输入目录")
            return None

        pattern = re.compile(self._file_RegEx)

        self._fileDict = defaultdict(list)
        for filename in os.listdir(self._input_path):
            filepath = os.path.join(self._input_path, filename)
            if not os.path.isfile(filepath):
                continue
            match = pattern.match(filename)
            if match:
                novel_name = match.group(1)
                start = int(match.group(2))
                end = int(match.group(3))
                self._fileDict[novel_name].append((start, end, filepath))
        return self._fileDict

    def merge_filse_list(self) -> defaultdict[list]:
        if self._is_single_file:
            print("单文件模式")
            return self.get_single_file()
        else:
            print("多文件模式")
            return self.get_all_file()

    def get_single_file(self) -> defaultdict[list]:
        if not os.path.isfile(self._input_path):
            self.error.emit("没有输入文件")
            return None

        input_dir = os.path.dirname(self._input_path)
        input_file = os.path.basename(self._input_path)

        pattern = re.compile(self._file_RegEx)
        match = pattern.match(input_file)

        novel_name = ""
        if match:
            novel_name = match.group(1)
        else:
            self.error.emit("文件名匹配失败")
            return
        signalFile = defaultdict(list)
        signalFile[novel_name].extend(self.get_all_file()[novel_name])
        self._fileDict = signalFile
        return self._fileDict 

    def get_file_count(self, files: defaultdict[list]) -> int:
        total = 0
        for _, files in files.items():
            total += len(files)
        return total

    def merge_file(self, fileName: str, files: list):
        files.sort(key=lambda x: x[0])
        output_path = os.path.join(self._output_path, f"{fileName}.txt")
        total_chapters = 0
        with open(output_path, "w", encoding="utf-8") as outfile:
            self.status.emit(f"开始合并：《{fileName}》")
            prev_end = -1
            for i, (start, end, filepath) in enumerate(files):
                # 检查章节连续性
                if start != prev_end + 1 and i != 0:
                    self.status.emit(
                        f"警告：章节不连续！当前开始章节 {start}，前一个结束章节 {prev_end}"
                    )
                prev_end = end

                try:
                    with open(filepath, "r", encoding="utf-8") as infile:
                        content = infile.read()
                        outfile.write(content + "\n")
                        chapters = end - start + 1
                        total_chapters += chapters
                        self.status.emit(
                            f"已合并 {os.path.basename(filepath)}（{chapters}章）"
                        )
                        self._progressCount = self._progressCount + 1
                        self.progress.emit(self._progressCount)
                except Exception as e:
                    self.error.emit(f"处理 {os.path.basename(filepath)} 时出错：{str(e)}")
                    return False

            self.status.emit(f"合并完成！总章节数：{total_chapters}")
        return True

    def init(self):
        self.merge_filse_list()




    @Slot()
    def do_merge(self):
        # self.merge_filse_list()
        self._progressCount = 0
        print(self._fileDict)
        for novel_name, files in self._fileDict.items():
            
            self.merge_file(novel_name, files)
       
        self.finished.emit()