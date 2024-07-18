from typing import Any, Union

import httpx

from core.tools.entities.tool_entities import ToolInvokeMessage
from core.tools.tool.builtin_tool import BuiltinTool

DOMAIN = "https://lark-plugin-api.solutionsuite.cn/lark-plugin"

class GetDocumentRawContentTool(BuiltinTool):
    def _invoke(self, user_id: str, tool_parameters: dict[str, Any]
                ) -> Union[ToolInvokeMessage, list[ToolInvokeMessage]]:
        tenant_access_token = tool_parameters.get('tenant_access_token', '')
        document_id = tool_parameters.get('document_id', '')

        headers = {
            'Content-Type': 'application/json',
            'tenant-access-token': tenant_access_token,
        }
        params = {
            "document_id": document_id
        }

        try:
            res = httpx.get(f"{DOMAIN}/document/get_document_raw_content", headers=headers, params=params,
                             timeout=30)
            return self.create_json_message(res.json())
        except Exception as e:
            return self.create_json_message({
                'code': 10101,
                'msg': f'get document raw content fail: {str(e)}'
            })
