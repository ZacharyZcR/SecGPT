import subprocess


def dirsearch_scan(args):
    try:
        url = args['url']
        extensions = args.get('extensions', 'php,asp,aspx,jsp')

        command = f"dirsearch -u {url} -e {extensions}"
        print(f"Command: {command}")

        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode == 0:
            return f"Commands DirsearchScan: Success. Output: {result.stdout.decode()}"
        else:
            return f"Commands DirsearchScan: Failed. Errors: {result.stderr.decode()}"

    except Exception as e:
        return f"Commands DirsearchScan: Failed. Error: {str(e)}"


def register():
    return {
        'name': 'DirsearchScan',
        'description': 'Run a dirsearch scan on a specified URL.',
        'func': dirsearch_scan,
        'args': [
            {'name': 'url', 'description': 'URL to be scanned.'},
            {'name': 'extensions', 'description': 'File extensions to be scanned.'}
        ]
    }
