import subprocess
import os


def installPackages():
    # Get the current directory
    current_dir: str = os.path.dirname(os.path.abspath(__file__))

    # Path to requirements.txt file
    requirements_file: str = os.path.join(current_dir, "..", "requirements.txt")

    try:
        subprocess.check_call(["pip", "install", "-r", requirements_file])
        print(f"Successfully installed.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install. Error: {e}")

    print("All packages installed.")


def run_pre_commit_install():
    try:
        subprocess.check_call(["pre-commit", "install"])
        print("pre-commit installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install pre-commit. Error: {e}")


if __name__ == "__main__":
    installPackages()
    run_pre_commit_install()
