import requests
from superagi.tools.base_tool import BaseTool

class BrainTool(BaseTool):
    def post(self, route, data) -> dict:
        access_token = self.get_tool_config("ACCESS_TOKEN")
        response = requests.post(
            f"https://api.brn.ai{route}",
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Access-Token": access_token
            },
            json = data,
        )
        return response.json()