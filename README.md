# 590-Final-Project


# Authors
Iqra Imtiaz: Worked on Amazon

Simon Nyamu: Worked on RetailRocket

More details: [Authors.md](https://github.com/iqra0908/590-Final-Project/blob/main/Authors.md)

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
To use Google Colab GPU, the steps for the RetailRocket implementation are provided in the Google Colab Notebook
Additonal notes on the metrics and dataset are included in the notebook.

# Benchmarking
## Amazon

|Models |HR@5|	NG@5|	HR@10|	NG@10|	NR@20|	NG@20|
|-----|--------|----|--------|-------|-----|------|
|GRU-SA2C| 0.022896|0.013746|0.038057|0.018657|0.067141|0.025909|
|SASRec-SA2C  |0.026609|0.015464|0.042389|0.020581|0.073639|0.028346|
|Caser-SA2C|0.021040|0.011621|0.042079|0.018490|0.065903|0.024479|
|NItNet|0.025062|0.014832|0.043007|0.020603|0.073020|0.027998|

| Model    | Training Set|Testing Set|
|----------|-------------|-----------|
|LightFM   | 0.9942909   | 0.9696471|

## RetailRocket

| Model    | Training Set|Testing Set|
|----------|-------------|-----------|
|LightFM   | 0.9973406   | 0.82500917|
Note: Typically, the AUC score is between 0 and 1 and a score of 0.8 or higher is considered good.

|Models |HR@5|	NG@5|	HR@10|	NG@10|	NR@20|	NG@20|
|-----|--------|----|--------|-------|-----|------|
|GRU-SA2C| 0.141509|0.116969|0.160377|0.122841|0.188679|0.130190|