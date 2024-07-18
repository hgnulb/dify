from typing import Any, Union

import httpx

from core.tools.entities.tool_entities import ToolInvokeMessage
from core.tools.tool.builtin_tool import BuiltinTool

DOMAIN = "https://lark-plugin-api.solutionsuite.cn/lark-plugin"


class CreateTableTool(BuiltinTool):
    def _invoke(self, user_id: str, tool_parameters: dict[str, Any]
                ) -> Union[ToolInvokeMessage, list[ToolInvokeMessage]]:
        tenant_access_token = tool_parameters.get('tenant_access_token', '')

        app_token = tool_parameters.get('app_token', '')
        name = tool_parameters.get('name', '')
        default_view_name = tool_parameters.get('default_view_name', '')
        fields = tool_parameters.get('fields', '')

        headers = {
            'Content-Type': 'application/json',
            'tenant-access-token': tenant_access_token,
        }
        params = {
            'app_token': app_token,
        }
        payload = {
            "table": {
                "name": name,
                "default_view_name": default_view_name,
                "fields": fields,
            }
        }

        try:
            res = httpx.post(f"{DOMAIN}/base/create_table", headers=headers, params=params, json=payload,
                             timeout=30)
            return self.create_json_message(res.json())
        except Exception as e:
            return self.create_json_message({
                'code': 10100,
                'msg': f'create base table fail: {str(e)}'
            })
