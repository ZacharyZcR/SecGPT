import subprocess

def sqlmap_test(args):
    try:
        base_url = args['url']
        params = args.get('params')
        method = args.get('method', 'GET')
        data = args.get('data')
        cookie = args.get('cookie')

        url = f"{base_url}?{params}" if params else base_url
        command = f"sqlmap -u \"{url}\" --method={method} --batch --dump"

        if data:
            command += f" --data={data}"
        if cookie:
            command += f" --cookie={cookie}"

        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode == 0:
            return f'Commands SqlmapTest: Success. Data: {result.stdout.decode()}'
        else:
            return f'Commands SqlmapTest: Failed. Error: {result.stderr.decode()}'

    except Exception as e:
        return f"Commands SqlmapTest: Failed. Error: {str(e)}"

def register():
    return {
        'name': 'SqlmapTest',
        'description': 'Run a sqlmap test on a specified URL and dump database data.',
        'func': sqlmap_test,
        'args': [
            {'name': 'url', 'description': 'Base URL to be tested.'},
            {'name': 'method', 'description': 'HTTP method to be used (GET, POST, etc.).', 'optional': True},
            {'name': 'params', 'description': 'URL parameters must to be like (id=1, etc.).', 'optional': True},
            {'name': 'data', 'description': 'Data to be sent in a POST request.', 'optional': True},
            {'name': 'cookie', 'description': 'HTTP Cookie header value.', 'optional': True},
        ]
    }
