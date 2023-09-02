from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from . import CreateBotTool, SendMessageTool, SendAttachmentTool

class BrainToolkit(BaseToolkit, ABC):
    name: str = "Brain system Toolkit"
    description: str = "Brain Tool kit contains all tools related to Brain system"

    def get_tools(self) -> List[BaseTool]:
        return [CreateBotTool(), SendMessageTool(), SendAttachmentTool()]

    def get_env_keys(self) -> List[str]:
        return ["ACCESS_TOKEN"]