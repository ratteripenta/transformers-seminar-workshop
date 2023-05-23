# Transformers seminar workshop

Initially created for [PhD Seminar on AI-Assisted Software Engineering](https://inforte.jyu.fi/events/phd-seminar-on-ai-assisted-software-engineering) workshop, Track 3:
 - Fine-tuning a transformer model based on a text corpus (Day 1)
 - Developing custom transformer architecture (Day 2)

## General setup

The repository comes bundled with an already fine-tuned BERT for the data to help all get on board even when they don't have sufficient resources for performing the fine-tuning a) themself or b) in a timely manner. 

To get the fine-tuned model:

 1. Download the the already trained models used in the notebooks from [Google Drive](https://drive.google.com/drive/folders/1_4-H5pz2v5tgWp6xZLMnpS-gSomBQpRN?usp=sharing) (too bi for Github):
  - Fine-tuned MLM BERT: `bert-base-uncased-finetuned.zip`
  - Fine-tuned MLM BERT with classification head: `classifier-fine.zip` 
  - Pre-trained MLM BERT with classification head: `classifier-pre.zip`
   
 2. Extract the models under `model` under respective folders (correct structure in archive)

## Local setup

 1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
 2. Create a `conda` environment:

        conda env create -f environment.yml

 3. Install [Pytorch](https://pytorch.org/) (prefer `pip` over `conda`):

        pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

 4. Use correct `conda` environment with notebooks.

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

More code hints to the code blocks as comments

Better introductions to the notebook re: structure

More deliberate hands-on codiong with attendees (show dont tell)

The custom BERT of workshop 2 does not incorporate MLM pre-training, but is essentially a transformer-based classifier
 - For learning about transformers, this suffices
 - For learning about BERT and how a fine-tunable and transfer learnable models, this this lacks a bit

WS1/NB1
 - "Describe numeric columns" -> No numeric columns in the 
 
WS2/NB1
 - Multi-haed description: where does the 64 come from?

WS2/NB2
 - BE MORE EXPLICIT WITH COLAB DATA USAGE (no need to preprocess again and again)
 - Add general image descriptions for the steps that are taken