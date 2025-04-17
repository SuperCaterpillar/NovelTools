import json
from dataclasses import dataclass, field
from typing import Dict, List, Any

# from functions.singleton_meta import SingletonMeta


@dataclass
class Config:
    data: dict = field(default_factory=dict)


@dataclass
class Component:
    module_path: str
    class_name: str
    func_name: str


@dataclass
class Page:
    component: Component
    config: Config


@dataclass
class PageRootConfig:
    pages: Dict[str, Page] = field(default_factory=dict)


class PagesConfigParser:
    @staticmethod
    def parse(json_path: str) -> PageRootConfig:

        with open(json_path, "r", encoding="utf-8") as f:
            config_dict = json.load(f)

        root = PageRootConfig()

        for page_name, page_data in config_dict.get("pages", {}).items():
            # compoent_node = page_data.get("component", {})
            # component = Component(
            #     module_path=compoent_node.get("module_path", ""),
            #     class_name=compoent_node.get("class_name", ""),
            #     func_name=compoent_node.get("func_name", ""),
            # )

            component = Component(**page_data['component'])
            page_config = Config(data=page_data.get("config", {}))

            root.pages[page_name] = Page(component=component, config=page_config)

        return root


# 使用示例
if __name__ == "__main__":

    config = PagesConfigParser.parse("D:/code/NovelTools/config/pages.json")

    print(config.pages["merge"].component.module_path)
