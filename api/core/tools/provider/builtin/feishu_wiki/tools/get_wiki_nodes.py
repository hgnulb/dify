from typing import Any, Union

import httpx

from core.tools.entities.tool_entities import ToolInvokeMessage
from core.tools.tool.builtin_tool import BuiltinTool

DOMAIN = "https://lark-plugin-api.solutionsuite.cn/lark-plugin"


class GetWikiNodesTool(BuiltinTool):
    def _invoke(self, user_id: str, tool_parameters: dict[str, Any]
                ) -> Union[ToolInvokeMessage, list[ToolInvokeMessage]]:
        space_id = tool_parameters.get('space_id', '')
        page_size = tool_parameters.get('page_size', '')
        page_token = tool_parameters.get('page_token', '')
        parent_node_token = tool_parameters.get('parent_node_token', '')

        headers = {
            'Content-Type': 'application/json',
        }
        params = {
            'page_size': page_size,
            'page_token': page_token,
            'parent_node_token': parent_node_token
        }
        payload = {}

        try:
            res = httpx.post(f"{DOMAIN}/wiki/get_wiki_nodes/{space_id}", headers=headers, params=params, json=payload,
                             timeout=30)
            return self.create_json_message(res.json())
        except Exception as e:
            return self.create_json_message({
                'code': 10100,
                'msg': f'get wiki nodes fail: {str(e)}'
            })
