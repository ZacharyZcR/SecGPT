LOG_COLORS_FORMAT = "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_FILE = 'SecGPT.log'
LOG_DIR = 'logs/'
LOG_COLORS = {
    'DEBUG': 'red',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red,bg_white',
}

# File Paths
CHARACTER_STORE_FILE_PATH = 'config/character.yaml'

# Regular Expressions
NAME_REGEX = r"Name(?:\s*):(?:\s*)(.*)"
DESCRIPTION_REGEX = r"Description(?:\s*):(?:\s*)(.*?)(?:(?:\n)|Goals)"
GOALS_REGEX = r"(?<=\n)-\s*(.*)"

# Directory
PLUGIN_DIRECTORY = "plugins"

# File Extensions
PYTHON_FILE_EXTENSION = ".py"

# Prompts
COMMANDS_PROMPT = 'Commands:\n'

# Directories
PROMPT_DIRECTORY = './prompts/'

# JSON Schema Prompt
JSON_SCHEMA_PROMPT = "Respond with only valid JSON conforming to the following schema: \n"

# Prompt Section Names
GOALS = 'Goals'
CONSTRAINTS = 'Constraints'
COMMANDS = 'Commands'
RESOURCES = 'Resources'
PERFORMANCE_EVALUATION = 'Performance Evaluation'
PROMPT_SECTIONS = [GOALS, CONSTRAINTS, COMMANDS, RESOURCES, PERFORMANCE_EVALUATION]

# User Prompt
USER_PROMPT = "Determine exactly one command to use, and respond using the JSON schema specified previously, only JSON data, not JSON schema:"
