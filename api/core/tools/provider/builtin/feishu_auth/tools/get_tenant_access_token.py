from typing import Any, Union

import httpx

from core.tools.entities.tool_entities import ToolInvokeMessage
from core.tools.tool.builtin_tool import BuiltinTool

DOMAIN = "https://lark-plugin-api.solutionsuite.cn/lark-plugin"

class GetTenantAccessTokenTool(BuiltinTool):
    def _invoke(self, user_id: str, tool_parameters: dict[str, Any]
                ) -> Union[ToolInvokeMessage, list[ToolInvokeMessage]]:

        app_id = tool_parameters.get('app_id', '')
        app_secret = tool_parameters.get('app_secret', '')
        if not app_id or not app_secret:
            return self.create_json_message({
                'code': 10100,
                'msg': 'invalid parameter app_id or app_secret'
            })

        headers = {
            'Content-Type': 'application/json',
        }
        params = {}
        payload = {
            "app_id": app_id,
            "app_secret": app_secret
        }

        """
        {
            "code": 0,
            "msg": "ok",
            "tenant_access_token": "t-caecc734c2e3328a62489fe0648c4b98779515d3",
            "expire": 7200
        }
        """
        try:
            res = httpx.post(f"{DOMAIN}/access_token/get_tenant_access_token", headers=headers, params=params, json=payload,
                             timeout=30)
            return self.create_json_message(res.json())
        except Exception as e:
            return self.create_json_message({
                'code': 10101,
                'msg': f'get tenant access token fail: {str(e)}'
            })
