from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from create_bot import CreateBotTool

class BrainToolkit(BaseToolkit, ABC):
    name: str = "Brain system Toolkit"
    description: str = "Brain Tool kit contains all tools related to Brain system"

    def get_tools(self) -> List[BaseTool]:
        return [CreateBotTool()]

    def get_env_keys(self) -> List[str]:
        return ["ACCESS_TOKEN"]