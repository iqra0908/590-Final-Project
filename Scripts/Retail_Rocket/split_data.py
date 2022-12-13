import os
import numpy as np
import pandas as pd
from utility import to_pickled_df
from sklearn import preprocessing


if __name__ == '__main__':
    data_directory = 'Datasets/RetailRocket'
    
    events = pd.read_pickle(os.path.join(data_directory, 'events_processed.df'))

    split_point = int(np.round(events.shape[0]*0.8))
    events_train = events.iloc[0:split_point]
    events_test = events.iloc[split_point::]
    events_test = events_test[(events_test['visitorid'].isin(events_train['visitorid'])) & (events_test['itemid'].isin(events_train['itemid']))]
        
    id_cols=['visitorid','itemid']
    trans_cat_train=dict()
    trans_cat_test=dict()

    for k in id_cols:
        cate_enc=preprocessing.LabelEncoder()
        trans_cat_train[k]=cate_enc.fit_transform(events_train[k].values)
        trans_cat_test[k]=cate_enc.transform(events_test[k].values)
        
    ratings = dict()

    cate_enc=preprocessing.LabelEncoder()
    events_train['rating'] = cate_enc.fit_transform(events_train.event)
    events_test['rating'] = cate_enc.transform(events_test.event)

    events_train['visitorid'] = trans_cat_train['visitorid']
    events_test['visitorid'] = trans_cat_test['visitorid']
    events_train['itemid'] = trans_cat_train['itemid']
    events_test['itemid'] = trans_cat_test['itemid']
    
    to_pickled_df(data_directory, events_train=events_train)
    to_pickled_df(data_directory, events_test=events_test)