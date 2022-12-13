# Contribution for Recommendors

## *Iqra Imtiaz*

Created repository structure and initial files.\
Created notebook [*Amazon_final_project.ipynb*](https://github.com/iqra0908/590-Final-Project/blob/main/Amazon_final_project.ipynb)\
Created [*README.md*](https://github.com/iqra0908/590-Final-Project/blob/main/README.md).

**Dataset**
* Chose 5-core [Amazon Clothing and Jewelry](http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Clothing_Shoes_and_Jewelry_5.json.gz) dataset.
* Unzipped and loaded dataset into the notebook.
* Computed dataset statistics and listed meaning of each column.


**Data Preparation**
* Extracted [**Self-Supervised Reinforcement Learning for Recommender Systems**](https://arxiv.org/abs/2006.05779) from papers given.
* Understood SA2C deep RL modeling and code structure.
* Managed to run the files after trying many methods such as downgrading tensorflow to 1.14, pandas, and others. Finally, made it work by converting the following files to use tensorflow version 2.
  * NextItNetModules.py
  * SA2C.py
  * SASRecModules.py
  * pop.py
  * preprocess.py
  * replay_buffer.py
  * split_data.py
  * utility.py
* Updated these files to use columns from amazon dataset and removed irrelevant code from them. 
* Ran the updated files to create following sub datasets from amazon to run model.
  * sorted_amazon.df
  * data_ststis.df
  * pop_dict.df
  * replay_buffer.df
  * sampled_train.df
  * sampled_val.df
* Performed all the above steps for RetailRocket dataset as well.
* Separated files for each dataset, created scripts and organized code structure before uploading into github repo.

**Modeling**
* Ran following models on amazon training data created before, each with 6000 batches.
  * GRU
  * SASRec
  * Caser
  * NItNet
* Created deep RL model for retail rocket as well and ran on training data.
* Added non-Deep RL for Amazon training data and calculated AUC score.
  
**Benchmarking**
* Chose NDCG metric because it is a measure of ranking quality which works great checking rating on Amazon products.
* Choosen AUC score for non-Deep RL on amazon data.
* Collected results from above models and reported in Readme.

## *Simon Nyamu*

**Dataset**

**Modeling**

**Benchmarking**