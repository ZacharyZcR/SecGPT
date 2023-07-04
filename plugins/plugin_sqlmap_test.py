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

        subprocess.run(command, shell=True)

        hostname = urlparse(base_url).hostname
        log_file_path = os.path.join('C:\\', 'Users', 'Administrator', 'AppData', 'Local', 'sqlmap', 'output', hostname, 'log')

        with open(log_file_path, 'r') as log_file:
            log_content = log_file.read()

        return f'Commands SqlmapTest: Success. Log content: {log_content}'

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
