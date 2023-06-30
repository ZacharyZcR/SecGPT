import requests

def http_request(args):
    try:
        http_method = args['http_method'].lower()
        url = args['url']
        params = args.get('params')

        if http_method == 'get':
            response = requests.get(url, params=params)
        elif http_method == 'post':
            response = requests.post(url, data=params)
        else:
            return f"Commands HttpRequest: Failed. Error: HTTP method {http_method} not supported."

        return f"Commands HttpRequest: Success. Data: {response.text}"

    except Exception as e:
        return f"Commands HttpRequest: Failed. Error: {str(e)}"

def register():
    return {
        'name': 'HttpRequest',
        'description': 'Make a HTTP request and return the response.',
        'func': http_request,
        'args': [
            {'name': 'http_method', 'description': 'HTTP method to be used: GET or POST.'},
            {'name': 'url', 'description': 'URL to be requested.'},
            {'name': 'params', 'description': 'Parameters to be sent with the request.', 'optional': True}
        ]
    }
