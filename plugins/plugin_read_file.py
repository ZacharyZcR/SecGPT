import os

def read_file(args):
    try:
        filename = args['filename']

        if not os.path.exists(filename):
            return f"Commands ReadFile: Failed. Error: File {filename} does not exist."

        with open(filename, 'r') as f:
            content = f.read()
            return f"Commands ReadFile: Success. Data: {content}"

    except Exception as e:
        return f"Commands ReadFile: Failed. Error: {str(e)}"

def register():
    return {
        'name': 'ReadFile',
        'description': 'Read a file and return its content.',
        'func': read_file,
        'args': [
            {'name': 'filename', 'description': 'Name of the file to be read.'},
        ]
    }