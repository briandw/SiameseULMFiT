# SiameseULMFiT
## ULMFiT + Siamese Network for Sentence Vectors

This an attempt to add an [InferSent](https://arxiv.org/pdf/1705.02364.pdf) type Siamese network on top of the Fast.ai [ULMFiT](http://nlp.fast.ai/classification/2018/05/15/introducting-ulmfit.html) archecture.

## Running the notebook
* The fast.ai library must be installed and the fastai folder available in the root folder
* Download the [SNLI corpus](https://nlp.stanford.edu/projects/snli/snli_1.0.zip) and unzip it into the data folder.
* Download the pretrained [wikitext model](http://files.fast.ai/models/wt103/) into the data/aclImdb folder
* Run the notebooks in order:
1. ULMFiT_Tokenize 
2. ULMFiT_Pretrain
3. ULMFiT_Classify

If you want to skip the tokenizing step, [download this file](https://github.com/briandw/SiameseULMFiT/releases/download/1/data.zip) and put it into the data section.
