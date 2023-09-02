from typing import Type
from pydantic import BaseModel, Field
from brain_tool import BrainTool

class SendAttachmentSchema(BaseModel):
    user_id: str = Field(..., description="ID of the user to send attachment to")
    attachment_type: str = Field(..., description="Type of the attachment, it can be image, video, audio, file")
    url: str = Field(..., description="URL of the attachment")

class SendAttachmentTool(BrainTool):
    name: str = "Brain Send Attachment"
    args_schema: Type[BaseModel] = SendAttachmentSchema
    description: str = "Sends an attachment to the specific user"

    def _execute(self, user_id: str, attachment_type: str, url: str) -> str:
        try:
            data = self.post(
                f"/message/send/{user_id}",
                { "type": attachment_type, "content": { "url": url } },
            )
            if data["status"] == True:
                return "Attachment sent successfully"
            else:
                raise Exception(data["error"])
        except Exception as err:
            return f"Error: Unable to send an attachment {err}"