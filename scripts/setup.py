import subprocess
import os
import venv

# Get the current directory
current_dir: str = os.path.dirname(os.path.abspath(__file__))

venv_dir = ".venv"  # Define your virtual environment directory

# install packages from requirements file
pip_path = os.path.join(current_dir, "..", f"{venv_dir}", "Scripts", "pip")

# pre-commit locations
pre_commit_path = os.path.join(
    current_dir, "..", f"{venv_dir}", "Scripts", "pre-commit"
)


def create_virtual_environment():
    builder = venv.EnvBuilder(
        with_pip=True
    )  # with_pip=True will ensure pip is installed in your venv
    builder.create(venv_dir)
    print(f"Virtual environment created in {venv_dir}.")


def install_packages():
    # Path to requirements.txt file
    requirements_file: str = os.path.join(current_dir, "..", "requirements.txt")

    try:
        print(pip_path)
        subprocess.check_call([pip_path, "install", "-r", requirements_file])
        print(f"Successfully installed.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install. Error: {e}")

    print("All packages installed.")


def run_pre_commit_install():
    try:
        subprocess.check_call([pre_commit_path, "install"])
        print("pre-commit installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install pre-commit. Error: {e}")


if __name__ == "__main__":
    create_virtual_environment()
    install_packages()
    run_pre_commit_install()
