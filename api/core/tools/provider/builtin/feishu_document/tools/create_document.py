from typing import Any, Union

import httpx

from core.tools.entities.tool_entities import ToolInvokeMessage
from core.tools.tool.builtin_tool import BuiltinTool

DOMAIN = "https://lark-plugin-api.solutionsuite.cn/lark-plugin"

class CreateDocumentTool(BuiltinTool):
    def _invoke(self, user_id: str, tool_parameters: dict[str, Any]
                ) -> Union[ToolInvokeMessage, list[ToolInvokeMessage]]:
        tenant_access_token = tool_parameters.get('tenant_access_token', '')
        title = tool_parameters.get('title', '')
        content = tool_parameters.get('content', '')
        folder_token = tool_parameters.get('folder_token', '')

        headers = {
            'Content-Type': 'application/json',
            'tenant-access-token': tenant_access_token,
        }
        params = {}
        payload = {
            "title": title,
            "content": content,
            "folder_token": folder_token,
        }

        try:
            res = httpx.post(f"{DOMAIN}/document/create_document", headers=headers, params=params, json=payload,
                             timeout=30)
            return self.create_json_message(res.json())
        except Exception as e:
            return self.create_json_message({
                'code': 10101,
                'msg': f'create document fail: {str(e)}'
            })
