import tomllib
import re
from pathlib import Path

path = Path("xmake.lua")

config_path = Path("moddata.toml")
with open(config_path, "rb") as file:
    config = tomllib.load(file)

def change_modname(text, config):
    return text.replace(
        'local MOD_NAME = "PlaceHolder"',
        f'local MOD_NAME = "{config["name"]}"'
    )


def change_description(text, config):
    return text.replace(
        'local MOD_DESC = "PlaceHolder"',
        f'local MOD_DESC = "{config["description"]}"'
    )

def change_version(text, config):
    return re.sub(r'local MOD_VERSION = "[^"]*"',
    f'local MOD_VERSION = "{config["modversion"]}"', 
    text, 
    count=1
    )

def xmake_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, str):
        return f'"{value}"'
    return str(value)


def add_configs(text, config):
    configs = config.get("configs", {})

    lines = [
        f'set_config("{name}", {xmake_value(value)})'
        for name, value in configs.items()
    ]

    return text.replace(
        "--{{ADDITIONAL CONFIGS}}--",
        "\n".join(lines) + ("\n" if lines else "")
    )


def change_xmakefile(text, config):
    text = change_modname(text, config)
    text = change_version(text, config)
    text = change_description(text, config)
    text = add_configs(text, config)    
    return text

def setup_structure(config):
    folders = config.get("structure", {})
    folders_to_mk = folders.get("folders", [])
    files_to_tch = folders.get("files",[])

    for folderName in folders_to_mk:
        f_path = Path(folderName)
        f_path.mkdir(parents=True, exist_ok=True)

    for fileName in files_to_tch:
        fileP = Path(fileName)
        fileP.parent.mkdir(parents=True, exist_ok=True)
        if not fileP.exists():
            fileP.touch()
        else:
            print(f"skipped existing file: {fileName}")


def main():

    setup_structure(config)

    text = path.read_text(encoding="utf-8")
    text = change_xmakefile(text, config)

    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
