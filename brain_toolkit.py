from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from superagi-brain-tool.create_bot import CreateBotTool
from superagi-brain-tool.send_message import SendMessageTool
from superagi-brain-tool.send_attachment import SendAttachmentTool

class BrainToolkit(BaseToolkit, ABC):
    name: str = "Brain system Toolkit"
    description: str = "Brain Tool kit contains all tools related to Brain system"

    def get_tools(self) -> List[BaseTool]:
        return [CreateBotTool(), SendMessageTool(), SendAttachmentTool()]

    def get_env_keys(self) -> List[str]:
        return ["ACCESS_TOKEN"]