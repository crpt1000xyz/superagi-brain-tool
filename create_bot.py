from typing import Type
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool
import requests

class CreateBotSchema(BaseModel):
    bot_name: str = Field(
        ...,
        description="Bot name",
    )

class CreateBotTool(BaseTool):
    name: str = "Brain Create Bot"
    args_schema: Type[BaseModel] = CreateBotSchema
    description: str = "Create a bot in Brain system"

    def _execute(self, name: str) -> str:
        try:
            access_token = self.get_tool_config("ACCESS_TOKEN")
            response = requests.post(
                f"https://api.brn.ai/bot",
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Access-Token": access_token
                },
                json = {
                    "name": name,
                },
            )
            data = response.json()
            if data.status == True:
                return f"Bot {name} created successfully with ID: {data.bot_id}"
            else:
                raise Exception(data.error)
        except Exception as err:
            return f"Error: Unable to create a bot {err}"