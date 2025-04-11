import json
from dataclasses import dataclass, field
from typing import Dict, List, Any


@dataclass
class FileRegEX:
    regex: str
    topic: str


@dataclass
class FunSetting:
    Name: str


@dataclass
class StackSetting:
    Module: str
    Page: str


@dataclass
class Pages:
    fun_setting: FunSetting
    stack_setting: StackSetting


@dataclass
class NovelConfig:
    name_reg_ex: List[FileRegEX] = field(default_factory=list)


@dataclass
class RootConfig:
    novel_config: NovelConfig
    pages: List[Pages]


class ConfigParser:
    @staticmethod
    def parse(json_path: str) -> RootConfig:
        """深度解析 JSON，返回强类型配置对象"""
        # 读取json文件
        with open(json_path, "r", encoding="utf-8") as f:
            config_dict = json.load(f)

        # 解析 NameRegEX 列表
        name_reg_ex = [
            FileRegEX(item["RegEX"], item["Topic"])
            for item in config_dict.get("NovelConfig", {}).get("FileRegEX", [])
        ]

        # 解析 Pages 列表
        pages = []
        for page in config_dict.get("Pages", []):
            pages.append(
                Pages(
                    fun_setting=FunSetting(**page["FunSetting"]),
                    stack_setting=StackSetting(**page["StackeSetting"]),
                )
            )

        return RootConfig(
            novel_config=NovelConfig(name_reg_ex=name_reg_ex), pages=pages
        )


# 使用示例
if __name__ == "__main__":

    # 解析配置
    config = ConfigParser.parse("D:/code/NovelTools/config/config.json")

    # 访问配置项（类型提示 + 自动补全支持）
    print(config.novel_config.name_reg_ex[0].regex)  # 输出正则表达式
    print(config.pages[0].fun_setting.name)  # 输出 "多文件合并"
    print(config.pages[1].stack_setting.module)  # 输出 "components.Page2"
