import os
import subprocess


def save_environment_to_requirements():
    # Get the current directory
    current_dir: str = os.path.dirname(os.path.abspath(__file__))

    # Path to requirements.txt file
    requirements_file: str = os.path.join(current_dir, "..", "dep", "requirements.txt")

    # Save the current environment to requirements.txt
    try:
        subprocess.check_call(
            ["pip", "freeze", ">{}".format(requirements_file)], shell=True
        )
        print("Environment saved to requirements.txt")
    except subprocess.CalledProcessError as e:
        print(f"Failed to save environment. Error: {e}")


if __name__ == "__main__":
    save_environment_to_requirements()
