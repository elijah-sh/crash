"""
======================
@title: wechat_v'ideo
@description:
@author: elijah
@date: 2022/9/13 22:44
=====================
"""
from asyncio.log import logger

import requests

def response(flow):
    url = flow.request.url
    content_type = flow.headers.get('Content-Type', default=None)
    logger.info(content_type)
    if "finder.video.qq.com" in url:
        content_type = flow.headers.get('Content-Type', default=None)
        if content_type is not None and content_type == 'video/mp4':
            logger.info(url)
            file_name = './urls.txt'
            with open(file_name, mode='a', encoding='utf-8') as f:
                f.write(url)
                f.write('\n')
                f.close()


url = ''

r = requests.get(url)
response(r)