import os

def write_file(args):
    try:
        filename = args['filename']
        data = args['data']

        with open(filename, 'w') as f:
            f.write(data)
            return f"Commands WriteFile: Success. Data: File {filename} has been written successfully."

    except Exception as e:
        return f"Commands WriteFile: Failed. Error: {str(e)}"

def register():
    return {
        'name': 'WriteFile',
        'description': 'Write data to a file.',
        'func': write_file,
        'args': [
            {'name': 'filename', 'description': 'Name of the file to be written to.'},
            {'name': 'data', 'description': 'Data to be written to the file.'}
        ]
    }