import requests

def web_request(args):
    try:
        # 实现主要功能，args是一个包含所有参数的字典
        url = args['url']
        response = requests.get(url)
        return f'Commands WebRequest: Success. Data: Status code for {url}: {response.status_code}'
    except Exception as e:
        return f"Commands WebRequest: Failed. Error: {str(e)}"

def register():
    return {
        'name': 'WebRequest',
        'description': 'Make a web request and return the status code.',
        'func': web_request,
        'args': [
            {'name': 'url', 'description': 'URL to be requested.'}
        ]
    }
