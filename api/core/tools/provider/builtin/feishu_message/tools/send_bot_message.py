from typing import Any, Union

import httpx

from core.tools.entities.tool_entities import ToolInvokeMessage
from core.tools.tool.builtin_tool import BuiltinTool

DOMAIN = "https://lark-plugin-api.solutionsuite.cn/lark-plugin"

class SendBotMessageTool(BuiltinTool):
    def _invoke(self, user_id: str, tool_parameters: dict[str, Any]
                ) -> Union[ToolInvokeMessage, list[ToolInvokeMessage]]:
        tenant_access_token = tool_parameters.get('tenant-access-token', '')

        receive_id_type = tool_parameters.get('receive_id_type', '')
        receive_id = tool_parameters.get('receive_id', '')
        content = tool_parameters.get('content', '')
        msg_type = tool_parameters.get('msg_type', '')

        headers = {
            'Content-Type': 'application/json',
            'tenant-access-token': tenant_access_token,
        }
        params = {
            "receive_id_type": receive_id_type,
        }
        payload = {
            "receive_id": receive_id,
            "content": content,
            "msg_type": msg_type,
        }

        try:
            res = httpx.post(f"{DOMAIN}/message/send_bot_message", headers=headers, params=params, json=payload,
                             timeout=30)
            return self.create_json_message(res.json())
        except Exception as e:
            return self.create_json_message({
                'code': 10101,
                'msg': f'send bot message fail: {str(e)}'
            })
