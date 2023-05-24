import os
import nbformat as nbf


NOTEBOOKS_DIR = "notebooks"
COLAB_SETUP_NOTEBOOK_FILENAME = "colab-setup.ipynb"
COLAB_SETUP_NOTEBOOK_PATH = os.path.join(NOTEBOOKS_DIR, COLAB_SETUP_NOTEBOOK_FILENAME)

# Read the setup notebook
with open(COLAB_SETUP_NOTEBOOK_PATH, "r", encoding="utf-8") as f:
    setup_notebook = nbf.read(f, as_version=4)

for root, directories, files in os.walk(NOTEBOOKS_DIR):
    for filename in files:
        if filename.endswith(".ipynb") and filename != COLAB_SETUP_NOTEBOOK_FILENAME:
            print(f"Clearing answers and merging {filename}")
            notebook_path = os.path.join(root, filename)

            with open(notebook_path, "r", encoding="utf-8") as f:
                notebook = nbf.read(f, as_version=4)

            # Iterate over the cells and clear the source of cells with the 'clear' tag
            for cell in notebook.cells:
                if "tags" in cell.metadata and "clear" in cell.metadata["tags"]:
                    cell.source = ""
            
            merged_cells = setup_notebook.cells + notebook.cells
            assert merged_cells[0] != notebook.cells[0]
            notebook.cells = merged_cells

            # Save the modified notebook
            with open(notebook_path, "w", encoding="utf-8") as f:
                nbf.write(notebook, f)
