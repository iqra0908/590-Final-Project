# 590-Final-Project


# Authors
Iqra Imtiaz: Worked on Amazon

Simon Nyamu: Worked on RetailRocket

# Introduction
 In this repository we have two contextual and sequential based recommender systems for E-commerce use case. 
 Here is an overview of what the repository contains.

 ## Datasets
 * RetialRocket
 * Amazon Clothing and Jewelery

## Models
* LightFM
* Self-Supervised Reinforcement Learning for Recommender Systems

## Benchmarking
* AUC score
* NDCG



# How to Run

Full detailed explanation is added in the following notebooks.

[*Amazon_final_project.ipynb*](https://github.com/iqra0908/590-Final-Project/blob/main/Amazon_final_project.ipynb)

[*RetailRocket_Final_Project.ipynb*](https://github.com/iqra0908/590-Final-Project/blob/main/RetailRocket_Final_Project.ipynb)

Amazon model can be run using following command

```
!python 'Scripts/SA2C.py' --model=SASRec --data='Datasets/Amazon' --epoch=100
```

# Benchmarking
## Amazon

|Models |HR@5|	NG@5|	HR@10|	NG@10|	NR@20|	NG@20|
|-----|--------|----|--------|-------|-----|------|
|GRU-SA2C| 0.021658|0.012944|0.043936|0.020088|0.073329|0.027523
|SASRec-SA2C  |      |