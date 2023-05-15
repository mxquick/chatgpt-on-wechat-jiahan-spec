

import requests

from common.log import logger
from config import user_name

class GptAdminUtil(object):

    @staticmethod
    def save_chat_msg(role, content, group_name):
        logger.info(1)
        url = "http://156.236.74.239:2077/noauth/client/gpt/wechat/message/batch/save"
        post_data = (
            '[{"role":"' + role + '","content":"' + content + '","msgType":1' + ',"userName":"' + user_name() +'","groupName":"' + group_name + '"}]'
        )
        logger.info(post_data)
        headers = {"content-type": "application/json"}
        res = requests.post(url, data=post_data.encode(), headers=headers)
        logger.info(res.json())