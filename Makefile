install-nbformat:
	pip install --upgrade pip -q
	pip install nbformat -q

setup-for-colab: install-nbformat
	git checkout main
	git push origin --delete google-colab || true
	git branch -D google-colab || true
	git fetch -p
	python scripts/setup_for_colab.py
	git checkout -b google-colab
	git commit -am "Clear and prefix with setup"
	git push -u origin google-colab
	git checkout main

