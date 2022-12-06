import os

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from utility import to_pickled_df


if __name__ == '__main__':
    data_directory = 'Datasets/Renttherunway'
    renttherunway = pd.read_json(os.path.join(data_directory, 'renttherunway_final_data.json.gz'),compression='gzip',lines=True)
    
    renttherunway['valid_user'] = renttherunway.user_id.map(renttherunway.groupby('user_id')['item_id'].size() > 2)
    renttherunway = renttherunway.loc[renttherunway.valid_user].drop('valid_user', axis=1)
    ##########remove items with <=2 interactions
    renttherunway['valid_item'] = renttherunway.item_id.map(renttherunway.groupby('item_id')['user_id'].size() > 2)
    renttherunway = renttherunway.loc[renttherunway.valid_item].drop('valid_item', axis=1)
    ######## transform to ids
    item_encoder = LabelEncoder()
    session_encoder= LabelEncoder()
    renttherunway['item_id'] = item_encoder.fit_transform(renttherunway.item_id)
    renttherunway['user_id'] = session_encoder.fit_transform(renttherunway.user_id)
    ###########sorted by user and review_date
    sorted_renttherunway = renttherunway.sort_values(by=['user_id', 'review_date'])

    to_pickled_df(data_directory, sorted_renttherunway=sorted_renttherunway)

