
def exit_program(args):
    try:
        exit()
        return "Commands Exit: Success. Program has exited."
    except Exception as e:
        return f"Commands Exit: Failed. Error: {str(e)}"

def register():
    return {
        'name': 'Exit',
        'description': 'Exits the program',
        'func': exit_program,
        'args': []
    }
