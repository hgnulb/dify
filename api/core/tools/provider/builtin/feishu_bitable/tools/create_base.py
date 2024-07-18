from typing import Any, Union

import httpx

from core.tools.entities.tool_entities import ToolInvokeMessage
from core.tools.tool.builtin_tool import BuiltinTool

DOMAIN = "https://lark-plugin-api.solutionsuite.cn/lark-plugin"


class CreateBaseTool(BuiltinTool):
    def _invoke(self, user_id: str, tool_parameters: dict[str, Any]
                ) -> Union[ToolInvokeMessage, list[ToolInvokeMessage]]:
        tenant_access_token = tool_parameters.get('tenant_access_token', '')
        name = tool_parameters.get('name', '')
        headers = {
            'Content-Type': 'application/json',
            'tenant-access-token': tenant_access_token,
        }
        params = {}
        payload = {
            "name": name,
        }

        try:
            res = httpx.post(f"{DOMAIN}/base/create_base", headers=headers, params=params, json=payload,
                             timeout=30)
            return self.create_json_message(res.json())
        except Exception as e:
            return self.create_json_message({
                'code': 10100,
                'msg': f'create base fail: {str(e)}'
            })
