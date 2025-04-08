from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QHBoxLayout,
    QLineEdit, QProgressBar, QPushButton, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget,QFileDialog,QMessageBox)
from UI.megre_ui import Ui_Megre
import os
import re
import sys
from collections import defaultdict
class Megre(QWidget):
    fileRegEx = r'^(.+?)\((\d+)-(\d+)章\)\.txt$'
    def __init__(self):
        super().__init__()
        self.ui = Ui_Megre()
        self.ui.setupUi(self)

        sizePolichy = self.ui.textBrowser.sizePolicy()
        sizePolichy.setRetainSizeWhenHidden(True)

        self.ui.textBrowser.setSizePolicy(sizePolichy)

        self.ui.regExEdit.setPlaceholderText(self.fileRegEx + "   (默认正则表达式，匹配xxx(0000-1111).txt)")
    
        self.ui.srcBtn.clicked.connect(self.selectSrcFile)
        self.ui.outputBtn.clicked.connect(self.selectOutputFile)
        self.ui.fileSeletBtn.toggled.connect(self.fileSelectToggled)
        self.ui.buttonBox.accepted.connect(self.start)
        

    def fileSelectToggled(self, flag):
        if self.ui.fileSeletBtn.isChecked():
            self.ui.regExEdit.setEnabled(False)
        else:
            self.ui.regExEdit.setEnabled(True)


    def selectSrcFile(self):
        if self.ui.fileSeletBtn.isChecked():
            fileName, _ = QFileDialog.getOpenFileName(self, "选择源文件", "", "All Files (*)")
        else:
            fileName = QFileDialog.getExistingDirectory(self, "选择源文件夹")
        self.ui.srcEdit.setText(fileName)

    def selectOutputFile(self):
        fileName = QFileDialog.getExistingDirectory(self, "选择输出文件夹")
        self.ui.outputEdit.setText(fileName)
       
    
    def getSingleFile(self)-> defaultdict[list]:
        input_file_path = self.ui.srcEdit.text()
        input_dir = os.path.dirname(input_file_path)
        input_file = os.path.basename(input_file_path)

        pattern =re.compile(self.fileRegEx)
        match = pattern.match(input_file)

        novel_name = ""
        if match:
            novel_name = match.group(1)
        else:
            QMessageBox(QMessageBox.Icon.Information, "提示", "文件名不符合正则表达式", QMessageBox.StandardButton.Ok).exec()
            return
        signalFile = defaultdict(list)
        signalFile[novel_name].extend(self.getAllFile(input_dir)[novel_name])
        return signalFile

    def getAllFile(self, input_dir:str)-> defaultdict[list]:
        # input_dir = self.ui.srcEdit.text()
        if input_dir == "":
            self.ui.textBrowser.append("请选择源文件夹")
            QMessageBox(QMessageBox.Icon.Critical, "错误", "请选择源文件夹", QMessageBox.StandardButton.Ok).exec()
            return
        
        # 使用正则表达式匹配文件名
        pattern =re.compile(self.fileRegEx)
        # 创建一个默认字典，用于存储小说文件
        novel_files = defaultdict(list)

        # 遍历源文件夹中的所有文件
        for filename in os.listdir(input_dir):
            filepath = os.path.join(input_dir, filename)
            # 如果不是文件，则跳过
            if not os.path.isfile(filepath):
                continue
            
            # 使用正则表达式匹配文件名
            match = pattern.match(filename)
            if match:
                # 获取小说名、起始页码和结束页码
                novel_name = match.group(1)
                start = int(match.group(2))
                end = int(match.group(3))
                # 将小说文件添加到字典中
                novel_files[novel_name].append((start, end, filepath))

        # 如果字典为空，则提示未找到有效小说文件
        if not novel_files:
            self.ui.textBrowser.append(f"在目录 {os.path.abspath(input_dir)} 中未找到有效小说文件")
            return
        
        # 返回字典
        return novel_files

        
 
    def merge(self, fileName:str, files:list, output_dir:str)-> bool:
        files.sort(key=lambda x: x[0])

        output_path = os.path.join(output_dir, f"{fileName}.txt")
        total_chapters = 0
        
        with open(output_path, 'w', encoding='utf-8') as outfile:
            self.ui.textBrowser.append(f"\n正在合并小说：《{fileName}》...")
            
            prev_end = -1
            for i, (start, end, filepath) in enumerate(files):
                # 检查章节连续性
                if start != prev_end + 1 and i != 0:
                    self.ui.textBrowser.append(f"警告：章节不连续！当前开始章节 {start}，前一个结束章节 {prev_end}")
                prev_end = end
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        outfile.write(content + "\n")
                        chapters = end - start + 1
                        total_chapters += chapters
                        self.ui.textBrowser.append(f"已合并 {os.path.basename(filepath)}（{chapters}章）")
                        self.ui.progressBar.setValue(self.ui.progressBar.value() + 1)
                except Exception as e:
                    self.ui.textBrowser.append(f"处理 {os.path.basename(filepath)} 时出错：{str(e)}")
        
            self.ui.textBrowser.append(f"合并完成！总章节数：{total_chapters}")
        return True
    def getFileCount(self, files:defaultdict[list])-> int:
        total = 0
        for novel_name, files in files.items():
            total += len(files)
        return total

    def start(self):
        input_dir = self.ui.srcEdit.text()
        output_dir = self.ui.outputEdit.text()
            
        if input_dir == "":
            QMessageBox(QMessageBox.Icon.Critical, "错误", "请选择源文件夹", QMessageBox.StandardButton.Ok).exec()
            return
        if output_dir == "":
            output_dir = self.ui.outputEdit.placeholderText()
            self.ui.textBrowser.append(f"未选择输出文件夹，使用默认输出文件夹：{output_dir}")

        novel_files = defaultdict(list)
        if self.ui.fileSeletBtn.isChecked():
            novel_files = self.getSingleFile()
            pass
        else:
            novel_files = self.getAllFile(input_dir)

        total = self.getFileCount(novel_files)
        self.ui.progressBar.setMaximum(total)

        for novel_name, files in novel_files.items():
            self.merge(novel_name, files, output_dir)

    
