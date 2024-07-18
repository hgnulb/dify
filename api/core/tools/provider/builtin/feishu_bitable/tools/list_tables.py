from typing import Any, Union

import httpx

from core.tools.entities.tool_entities import ToolInvokeMessage
from core.tools.tool.builtin_tool import BuiltinTool

DOMAIN = "https://lark-plugin-api.solutionsuite.cn/lark-plugin"


class ListTablesTool(BuiltinTool):
    def _invoke(self, user_id: str, tool_parameters: dict[str, Any]
                ) -> Union[ToolInvokeMessage, list[ToolInvokeMessage]]:
        tenant_access_token = tool_parameters.get('tenant_access_token', '')
        app_token = tool_parameters.get('app_token', '')
        page_token = tool_parameters.get('page_token', '')
        page_size = int(tool_parameters.get('page_size', ''), 0)
        if page_size <= 0:
            page_size = 20
        if page_size > 100:
            page_size = 100

        headers = {
            'Content-Type': 'application/json',
            'tenant-access-token': tenant_access_token,
        }
        params = {
            'app_token': app_token,
            'page_token': page_token,
            'page_size': page_size,
        }

        try:
            res = httpx.post(f"{DOMAIN}/base/list_tables", headers=headers, params=params, timeout=30)
            return self.create_json_message(res.json())
        except Exception as e:
            return self.create_json_message({
                'code': 10100,
                'msg': f'list tables fail: {str(e)}'
            })
