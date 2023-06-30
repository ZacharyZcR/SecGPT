import requests

def web_test(args):
    try:
        url = args['url']
        response = requests.get(url)
        return f'Commands WebTest: Success. Data: Status code for {url}: {response.status_code}'
    except Exception as e:
        return f"Commands WebTest: Failed. Error: {str(e)}"

def register():
    return {
        'name': 'WebTest',
        'description': 'Make a web request and return the status code.',
        'func': web_test,
        'args': [
            {'name': 'url', 'description': 'URL to be requested.'}
        ]
    }
