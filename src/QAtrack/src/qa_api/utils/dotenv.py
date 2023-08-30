def load_dotenv_to_config(dotenv_path):
    """Load .env file at path to config dictionary."""
    config = {}
    with open(dotenv_path) as dotenv:
        for line in dotenv:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            v = v.strip("'").strip('"')
            config[k] = v
    return config
