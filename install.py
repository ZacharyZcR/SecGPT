import os
import pkg_resources

REQUIRED_PACKAGES = [
    "openai",
    "colorlog",
    "pyyaml",
]

CONFIG_DIRECTORY = "config"
CONFIG_FILE = "config.yaml"

class Installer:
    def __init__(self, requirements_file):

        self.requirements_file = requirements_file

    def check_packages(self):
        with open(self.requirements_file, 'r') as f:
            required_packages = [line.strip().lower() for line in f]

        installed_packages = pkg_resources.working_set
        installed_packages_list = sorted([f"{i.key.lower()}=={i.version}" for i in installed_packages])
        missing_packages = [pkg for pkg in required_packages if pkg not in installed_packages_list]

        if missing_packages:
            print(f"The following required packages are missing: {missing_packages}")
            print("Please install the missing packages and try again.")
            return False
        else:
            print("All required packages are installed.")
            return True

    def check_config(self):
        if not os.path.exists(CONFIG_DIRECTORY):
            os.makedirs(CONFIG_DIRECTORY)
            print(f"Created directory: {CONFIG_DIRECTORY}")

        config_path = os.path.join(CONFIG_DIRECTORY, CONFIG_FILE)
        if not os.path.exists(config_path):
            with open(config_path, 'w') as config_file:
                config_file.write("# Config file\n")
                config_file.write("openai_key: ******************************************")
            print(f"Created file: {config_path}")

        return True

if __name__ == "__main__":
    installer = Installer("requirements.txt")
    if installer.check_packages() and installer.check_config():
        print("Installation complete.")