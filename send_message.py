from typing import Type
from pydantic import BaseModel, Field
from tool import BrainTool

class SendMessageSchema(BaseModel):
    user_id: str = Field(..., description="ID of the user to send message to")
    text: str = Field(..., description="Text of the message")

class SendMessageTool(BrainTool):
    name: str = "Brain Send Message"
    args_schema: Type[BaseModel] = SendMessageSchema
    description: str = "Sends a message to the specific user"

    def _execute(self, user_id: str, text: str) -> str:
        try:
            data = self.post(
                f"/message/send/{user_id}",
                { "type": "text", "content": { "text": text } },
            )
            if data["status"] == True:
                return "Message sent successfully"
            else:
                raise Exception(data["error"])
        except Exception as err:
            return f"Error: Unable to send a message {err}"