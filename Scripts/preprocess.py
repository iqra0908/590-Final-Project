import os

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from utility import to_pickled_df


if __name__ == '__main__':
    data_directory = 'Datasets/Amazon'
    renttherunway = pd.read_json(os.path.join(data_directory, 'reviews_Clothing_Shoes_and_Jewelry_5.json.gz'),compression='gzip',lines=True)
    
    renttherunway['valid_user'] = renttherunway.reviewerID.map(renttherunway.groupby('reviewerID')['asin'].size() > 2)
    renttherunway = renttherunway.loc[renttherunway.valid_user].drop('valid_user', axis=1)
    ##########remove items with <=2 interactions
    renttherunway['valid_item'] = renttherunway.asin.map(renttherunway.groupby('asin')['reviewerID'].size() > 2)
    renttherunway = renttherunway.loc[renttherunway.valid_item].drop('valid_item', axis=1)
    ######## transform to ids
    item_encoder = LabelEncoder()
    session_encoder= LabelEncoder()
    renttherunway['asin'] = item_encoder.fit_transform(renttherunway.asin)
    renttherunway['reviewerID'] = session_encoder.fit_transform(renttherunway.reviewerID)
    ###########sorted by user and reviewTime
    sorted_amazon = renttherunway.sort_values(by=['reviewerID', 'reviewTime'])

    to_pickled_df(data_directory, sorted_amazon=sorted_amazon)

