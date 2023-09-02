from typing import Type
from pydantic import BaseModel, Field
from tool import BrainTool

class CreateBotSchema(BaseModel):
    bot_name: str = Field(..., description="Bot name")

class CreateBotTool(BrainTool):
    name: str = "Brain Create Bot"
    args_schema: Type[BaseModel] = CreateBotSchema
    description: str = "Create a bot in Brain system"

    def _execute(self, bot_name: str) -> str:
        try:
            data = self.post("/bot", { "name": bot_name })
            if data["status"] == True:
                bot_id = data["bot_id"]
                return f"Bot '{bot_name}' created successfully with ID: {bot_id}"
            else:
                raise Exception(data["error"])
        except Exception as err:
            return f"Error: Unable to create a bot {err}"