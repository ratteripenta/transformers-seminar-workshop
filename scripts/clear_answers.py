import os
import nbformat as nbf

# Specify the directory path where the notebooks are located
notebooks_directory = 'notebooks/'

# Iterate over the root, directories, and files in the notebooks directory
for root, directories, files in os.walk(notebooks_directory):
    for filename in files:
        if filename.endswith('.ipynb'):
            print(f"Clearing answers from {filename} - ")
            notebook_path = os.path.join(root, filename)

            # Read the notebook
            with open(notebook_path, 'r', encoding='utf-8') as f:
                notebook = nbf.read(f, as_version=4)

            # Iterate over the cells and clear the source of cells with the 'clear' tag
            for cell in notebook.cells:
                if 'tags' in cell.metadata and 'clear' in cell.metadata['tags']:
                    cell.source = ""

            # Save the modified notebook
            with open(notebook_path, 'w', encoding='utf-8') as f:
                nbf.write(notebook, f)
