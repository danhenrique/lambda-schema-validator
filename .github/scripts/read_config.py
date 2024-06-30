import yaml
import os


def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


config = load_config('config.yaml')

python_version = config['python_version']
test_folder = config['test_folder']
requirements_prod = config['requirements']['production']
requirements_test = config['requirements']['test']

# Salvar as variáveis de ambiente em um arquivo
github_env = os.getenv('GITHUB_ENV')
if github_env:
    with open(github_env, 'a') as env_file:
        env_file.write(f"PYTHON_VERSION={python_version}\n")
        env_file.write(f"TEST_FOLDER={test_folder}\n")
        env_file.write(f"REQUIREMENTS_PROD={requirements_prod}\n")
        env_file.write(f"REQUIREMENTS_TEST={requirements_test}\n")
else:
    print(f"PYTHON_VERSION={python_version}")
    print(f"TEST_FOLDER={test_folder}")
    print(f"REQUIREMENTS_PROD={requirements_prod}")
    print(f"REQUIREMENTS_TEST={requirements_test}")
