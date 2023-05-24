import os
import nbformat as nbf


NOTEBOOKS_DIR = "notebooks"
COLAB_STEUP_NOTEBOOK_FILENAME = "colab-setup.ipynb"
COLAB_SETUP_NOTEBOOK_PATH = os.path.join(NOTEBOOKS_DIR, COLAB_STEUP_NOTEBOOK_FILENAME)


def merge_notebooks(notebook_paths):
    combined_nb = nbf.v4.new_notebook()

    for path in notebook_paths:
        with open(path, "r", encoding="utf-8") as f:
            nb = nbf.read(f, as_version=4)

        combined_nb.cells.extend(nb.cells)

    return combined_nb


# Iterate over the root, directories, and files in the notebooks directory
for root, directories, files in os.walk(NOTEBOOKS_DIR):
    for filename in files:
        if filename.endswith(".ipynb") and "colab-setup" not in filename:
            print(f"Clearing answers and merging {filename}")
            notebook_path = os.path.join(root, filename)

            # Read the notebook
            with open(notebook_path, "r", encoding="utf-8") as f:
                notebook = nbf.read(f, as_version=4)

            # Iterate over the cells and clear the source of cells with the 'clear' tag
            for cell in notebook.cells:
                if "tags" in cell.metadata and "clear" in cell.metadata["tags"]:
                    cell.source = ""

            # Merge with the specific notebook
            setup_notebook = nbf.read(COLAB_SETUP_NOTEBOOK_PATH, as_version=4)
            setup_notebook.cells.extend(notebook.cells)

            # Save the modified notebook
            with open(notebook_path, "w", encoding="utf-8") as f:
                nbf.write(notebook, f)
