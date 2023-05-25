# Transformers seminar workshop

Initially created for [PhD Seminar on AI-Assisted Software Engineering](https://inforte.jyu.fi/events/phd-seminar-on-ai-assisted-software-engineering) workshop, Track 3:
 - Fine-tuning a transformer model based on a text corpus (Day 1)
 - Developing custom transformer architecture (Day 2)

The `main` branch contains all the code necessary to run the notebooks (e.g. correct answers for the students).

The `google-colab` branch is intended for students and requires manually coding some parts of the notebooks. To use the notebook in Google Colab:
 - Go to *https://colab.research.google.com/*
 - Open a new notebook and select the *Github* tab
   - For username, enter *karmus89*
   - For repository, select *transformers-seminar-workshop*
   - For branch, select *google-colab*
   - Remember to change the runtime to *GPU* for training
 - The repository is always up to date with respect to the *main* branch
   - Some of the code cells have been omitted, though

## General setup

The repository comes bundled with an already fine-tuned BERT for the data to help all get on board even when they don't have sufficient resources for performing the fine-tuning a) themself or b) in a timely manner. 

To get the fine-tuned model:

 1. Download the the already trained models used in the notebooks from thei corresponding Hugging Face repositories and persist them in the `model` folder:
  - Fine-tuned MLM BERT: `git clone https://huggingface.co/karmus89/bert-base-uncased-finetuned`
  - Fine-tuned MLM BERT with classification head: `git clone https://huggingface.co/karmus89/classifier-fine`
  - Pre-trained MLM BERT with classification head: `git clone https://huggingface.co/karmus89/classifier-pre`

## Local setup

 1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
 2. Create a `conda` environment:

        conda env create -f environment.yml

 3. Install [Pytorch](https://pytorch.org/) (prefer `pip` over `conda`):

        pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

 4. Use correct `conda` environment with notebooks.

## Notes

The custom BERT of workshop 2 does not incorporate MLM pre-training, but is essentially a transformer-based classifier
 - For learning about transformers, this suffices
 - For learning about BERT and how a fine-tunable and transfer learnable models, this this lacks a bit

## Additional resources for learning

Attention is all you need (2017)
 - [arXiv](https://arxiv.org/pdf/1706.03762.pdf)
 - [The Annotated Transformer: notebook of paper with code](http://nlp.seas.harvard.edu/annotated-transformer/)
 - [Stanford CS224N: NLP with Deep Learning | Winter 2019 | Lecture 14 – Transformers and Self-Attention](https://youtu.be/5vcj8kSwBCY)

BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (2018)
 - [arXiv](https://arxiv.org/pdf/1810.04805.pdf)
 - [Github repo](https://github.com/google-research/bert)

HuggingFace Course
 - [YouTube playlist](https://www.youtube.com/playlist?list=PLo2EIpI_JMQvWfQndUesu0nPBAtZ9gP1o)

Jay Alammar's blog posts about core concepts
 - [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
 - [The Illustrated BERT](https://jalammar.github.io/illustrated-bert/)
 - [The Illustrated GPT-2 (Visualizing Transformer Language Models)](https://jalammar.github.io/illustrated-gpt2/)
 - [Visualizing A Neural Machine Translation Model (Mechanics of Seq2seq Models With Attention)](https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/)

Udemy course "Natural Language Processing: NLP With Transformers in Python"
 - [Github repo](https://github.com/jamescalam/transformers)

Peter Bloems blog "Transformers from scratch"
 - [Link](https://peterbloem.nl/blog/transformers)

Neptune.ai's blog on creating BERT in Pytorch
 - [Link](https://neptune.ai/blog/how-to-code-bert-using-pytorch-tutorial)
 
## Ideas for development

Better introductions to the notebook re: structure
 - Add general image descriptions for the steps that are taken
