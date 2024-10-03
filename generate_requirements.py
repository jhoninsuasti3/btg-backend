import os
import sys


def search_folders(token, branch):
    root_path = "modules"
    for foldername in os.listdir(root_path):
        subfolder = os.path.join(root_path, foldername)
        if os.path.isdir(subfolder):
            requirements_path = os.path.join(subfolder, "requirements.txt")
            with open(requirements_path, "a") as file:
                file.write("\n")
                req = f"git+https://{token}@github.com/jhoninsuasti3/btg-backend.git@{branch}"
                print("ADD : ", req)
                file.write(req)


if len(sys.argv) < 3:
    print("Debe proporcionar el token y la rama")
    print("Ejemplo: python script.py <token> <rama>")
    sys.exit(1)

token = sys.argv[1]
branch = sys.argv[2]


search_folders(token, branch)
