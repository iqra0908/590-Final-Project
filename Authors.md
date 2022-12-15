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

* Created the non-DRL notebook RetailRocket_final_project.ipynb
* Included documentation and step-by-step instructions on completing the project
* Contributed in the README.md. and overall project documentation
* Provided relevant references for the dataset, model, metrics and project implementations

**Dataset**
The RetailRocket include the three dataset files:
i)File with behaviour data (events.csv)
(ii)File with item properties (itemproperties.сsv)
(iii)File describing the category tree (categorytree.сsv).

**Running the Model
* Worked on the pre-processing of the RetailRocket data
* Researched on session/context-based recommenders and consulted with TA on different models.
* After discussion with TA, I chose the Non-DRL model (LightFM)
* Chose the metrics(AUC-ROC) for the non-DRL part of the project

**Modeling**
* Installed LightFM and used it for modeling of the dataset
* Determined the choice of metrics, ran the model and collected the metrics.
* After Iqra created the scripts, I ran through both the RetailRocket and the Amazon recommenders to validate the scores with the scripts.

**Benchmarking**
* Chose AUC as the metric because it a simple measure that offers an uncomplicated way to summarize a model’s overall performance. It helps to measure the likelihood that a random relevant item will be ranked higher than a random irrelevant item.

**Additional information is included in the RetailRocket notebook.
