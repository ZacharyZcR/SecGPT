import subprocess

def nmap_scan(args):
    try:
        target = args['target']
        if not target:
            return "Commands NmapScan: Failed. Error: target is required."
        command = f"nmap {target}"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode == 0:
            return f"Commands NmapScan: Success. Output: {result.stdout.decode()}"
        else:
            return f"Commands NmapScan: Failed. Errors: {result.stderr.decode()}"

    except Exception as e:
        print(f"Command failed due to: {str(e)}")
        return f"Commands NmapScan: Failed. Error: {str(e)}"

def register():
    return {
        'name': 'NmapScan',
        'description': 'Run a nmap scan on a specified target.',
        'func': nmap_scan,
        'args': [
            {'name': 'target', 'description': 'Target to be scanned.'},
        ]
    }
