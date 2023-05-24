colab:
	pip install nbformat
	nbmerge ./notebooks/colab-setup.ipynb ./notebooks/workshop-1/01-data-preprocessing.ipynb > ./notebooks/workshop-1/01-data-preprocessing.ipynb
	nbmerge ./notebooks/colab-setup.ipynb ./notebooks/workshop-1/02-model-fine-tuning.ipynb > ./notebooks/workshop-1/02-model-fine-tuning.ipynb
	nbmerge ./notebooks/colab-setup.ipynb ./notebooks/workshop-1/03-using-fine-tuned-model.ipynb > ./notebooks/workshop-1/03-using-fine-tuned-model.ipynb
	nbmerge ./notebooks/colab-setup.ipynb ./notebooks/workshop-2/01-transformer-concepts.ipynb > ./notebooks/workshop-2/01-transformer-concepts.ipynb
	nbmerge ./notebooks/colab-setup.ipynb ./notebooks/workshop-2/02-create-and-train-custom-bert.ipynb > ./notebooks/workshop-2/02-create-and-train-custom-bert.ipynb