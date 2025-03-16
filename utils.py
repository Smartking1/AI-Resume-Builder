def load_template(template_path):
    with open(template_path, "r") as file:
        return file.read()

def load_file(file_path):
    with open(file_path, "r") as file:
        return file.read()