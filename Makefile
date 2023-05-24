install-nbformat:
	pip install --upgrade pip -q
	pip install nbformat -q

clear-answers: install-nbformat
	python scripts/setup_for_colab.py