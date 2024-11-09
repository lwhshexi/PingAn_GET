from mitmproxy import ctx


def request(flow):
    flow.request.headers['User-Agent'] = 'MitmProxy'
    ctx.log.info(str(flow.request.headers))     # 白色
    ctx.log.warn(str(flow.request.headers))     # 黄色
    ctx.log.error(str(flow.request.headers))    # 红色
