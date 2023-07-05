import subprocess
import os
from urllib.parse import urlparse

def sqlmap_test(args):
    try:
        base_url = args['url']
        params = args.get('params')
        if not params:
            return "Commands SqlmapTest: Failed. Error: params is required."

        url = f"{base_url}?{params}" if params else base_url
        command = f"sqlmap -u \"{url}\" --batch"

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
        'description': 'Run the sqlmap test against the specified URL, params must be provided',
        'func': sqlmap_test,
        'args': [
            {'name': 'url', 'description': 'Base URL to be tested.'},
            {'name': 'params', 'description': 'URL parameters must to be like (arg1=1&arg2=2, etc.).'},
        ]
    }
