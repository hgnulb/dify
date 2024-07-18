from typing import Any, Union

import httpx

from core.tools.entities.tool_entities import ToolInvokeMessage
from core.tools.tool.builtin_tool import BuiltinTool

DOMAIN = "https://lark-plugin-api.solutionsuite.cn/lark-plugin"


class SearchRecordTool(BuiltinTool):
    def _invoke(self, user_id: str, tool_parameters: dict[str, Any]
                ) -> Union[ToolInvokeMessage, list[ToolInvokeMessage]]:
        tenant_access_token = tool_parameters.get('tenant_access_token', '')

        app_token = tool_parameters.get('app_token', '')
        table_id = tool_parameters.get('table_id', '')
        user_id_type = tool_parameters.get('user_id_type', '')
        page_token = tool_parameters.get('page_token', '')
        page_size = tool_parameters.get('page_size', '')

        automatic_fields = tool_parameters.get('automatic_fields', '')
        field_names = tool_parameters.get('field_names', '')
        filter_condition = tool_parameters.get('filter', '')
        sort_list = tool_parameters.get('sort', '')
        view_id = tool_parameters.get('view_id', '')

        headers = {
            'Content-Type': 'application/json',
            'tenant-access-token': tenant_access_token,
        }
        params = {
            "app_token": app_token,
            "table_id": table_id,
            "user_id_type": user_id_type,
            "page_token": page_token,
            "page_size": page_size,
        }
        payload = {
            "automatic_fields": automatic_fields,
            "field_names": field_names,
            "filter": filter_condition,
            "sort": sort_list,
            "view_id": view_id
        }

        try:
            res = httpx.post(f"{DOMAIN}/base/search_record", headers=headers, params=params, json=payload, timeout=30)
            return self.create_json_message(res.json())
        except Exception as e:
            return self.create_json_message({
                'code': 10100,
                'msg': f'search record fail: {str(e)}'
            })
