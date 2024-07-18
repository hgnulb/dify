from typing import Any, Union

import httpx

from core.tools.entities.tool_entities import ToolInvokeMessage
from core.tools.tool.builtin_tool import BuiltinTool

DOMAIN = "https://lark-plugin-api.solutionsuite.cn/lark-plugin"


class UpdateRecordsTool(BuiltinTool):
    def _invoke(self, user_id: str, tool_parameters: dict[str, Any]
                ) -> Union[ToolInvokeMessage, list[ToolInvokeMessage]]:
        tenant_access_token = tool_parameters.get('tenant_access_token', '')

        app_token = tool_parameters.get('app_token', '')
        table_id = tool_parameters.get('table_id', '')
        user_id_type = tool_parameters.get('user_id_type', '')
        records = tool_parameters.get('records', '')

        headers = {
            'Content-Type': 'application/json',
            'tenant-access-token': tenant_access_token,
        }
        params = {
            "app_token": app_token,
            "table_id": table_id,
            "user_id_type": user_id_type,
        }
        payload = {
            "records": records
        }

        try:
            res = httpx.post(f"{DOMAIN}/base/update_records", headers=headers, params=params, json=payload, timeout=30)
            return self.create_json_message(res.json())
        except Exception as e:
            return self.create_json_message({
                'code': 10100,
                'msg': f'update records fail: {str(e)}'
            })