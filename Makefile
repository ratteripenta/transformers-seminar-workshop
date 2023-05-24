install-nbformat:
	pip install --upgrade pip -q
	pip install nbformat -q

setup-for-colab: install-nbformat
	python scripts/setup_for_colab.py