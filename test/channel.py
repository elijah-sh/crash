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


url = 'https://finder.video.qq.com/251/20302/stodownload?encfilekey=6xykWLEnztKcKCJZcV0rWCM8ua7DibZkibPSZaIgeFjxGFcB8gQCQW4iaJojV6wIWgfVpgUMWIbggIH2JQEx7sQECxsYc1FZ6WP5oPZ92l0iczu9z3JBQDibNoGK1RAibnSEianrtmTjZicgz3qm1BNuMZDvZdicpqEYibkTm3c2ChNXB8oa4&token=AxricY7RBHdVphupOFUBGCQe6q1P1ooG09YLqZu9qicn0HVgaqaot5XBUzUzmbPuCCcx4afQZia2AE&idx=1&a=1&adaptivelytrans=943&bizid=1023&dotrans=2991&hy=SZ&m=db6d9029a986941286173d60994dd850&web=1&X-snsvideoflag=xV2&taskid=0'

r = requests.get(url)
response(r)