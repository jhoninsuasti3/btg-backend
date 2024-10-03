"""
Change name
"""

import os
import sys


def update_name(path_name, line_new, line_to_replace):
    """
    Update a specific line in a file with new text.

    Args:
        path_name (str): The path to the file to be updated.
        line_new (str): The new text to replace the old text with.
        line_to_replace (str): The text to be replaced in the file.
    """
    try:
        with open(path_name, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace(line_to_replace, line_new)
        with open(path_name, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Se ha actualizado el puerto en {path_name} a {line_new}")
    except FileNotFoundError:
        print(f"Error: El archivo {path_name} no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <name_stack_and_env>")
        sys.exit(1)

    name_stack_and_env = sys.argv[1]
    print("environment", name_stack_and_env)
    supervisor_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "template_master.yaml"
    )
    update_name(supervisor_path, f"BtgPactual{name_stack_and_env}", "BtgPactual")
