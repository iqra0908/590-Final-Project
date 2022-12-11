# 590-Final-Project


# Authors
Iqra Imtiaz

Simon Nyamu

# Introduction
 In this repository we have two contextual and sequential based recommender systems for E-commerce use case. 
 Here is an overview of what the repository contains.

 ## Datasets
 * RetialRocket
 * Renttherunway

## Models
* LightFM
* Self-Supervised Reinforcement Learning for Recommender Systems

## Benchmarking
* AUC score
* NDCG

Further detailed explanation is also added in the following notebooks.

***RentTheRunway_final_project.ipynb***
***RetailRocket_Final_Project.ipynb***

# How to Run

Renttherunway model can be run using following command

```
!python 'Scripts/SA2C.py' --model=SASRec --data='Datasets/Renttherunway' --epoch=100
```