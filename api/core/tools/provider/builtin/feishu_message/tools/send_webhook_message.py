from typing import Any, Union

import httpx

from core.tools.entities.tool_entities import ToolInvokeMessage
from core.tools.tool.builtin_tool import BuiltinTool

DOMAIN = "https://lark-plugin-api.solutionsuite.cn/lark-plugin"

class SendWebhookMessageTool(BuiltinTool):
    def _invoke(self, user_id: str, tool_parameters: dict[str, Any]
                ) -> Union[ToolInvokeMessage, list[ToolInvokeMessage]]:
        key = tool_parameters.get('key', '')
        msg_type = tool_parameters.get('msg_type', '')
        content = tool_parameters.get('content', '')

        headers = {
            'Content-Type': 'application/json',
        }
        params = {
        }
        payload = {
            "key": key,
            "content": content,
            "msg_type": msg_type,
        }

        try:
            res = httpx.post(f"{DOMAIN}/message/send_webhook_message", headers=headers, params=params, json=payload,
                             timeout=30)
            return self.create_json_message(res.json())
        except Exception as e:
            return self.create_json_message({
                'code': 10101,
                'msg': f'send webhook message fail: {str(e)}'
            })
