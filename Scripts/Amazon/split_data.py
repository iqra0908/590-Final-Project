import os
import numpy as np
import pandas as pd
from utility import to_pickled_df


if __name__ == '__main__':
    data_directory = 'Datasets/Amazon'
    
    renttherunway = pd.read_pickle(os.path.join(data_directory, 'sorted_amazon.df'))

    total_sessions=renttherunway.reviewerID.unique()
    np.random.shuffle(total_sessions)

    fractions = np.array([0.8, 0.1, 0.1])
    # split into 3 parts
    train_ids, val_ids, test_ids = np.array_split(
        total_sessions, (fractions[:-1].cumsum() * len(total_sessions)).astype(int))

    train_sessions=renttherunway[renttherunway.index.isin(train_ids)]
    val_sessions=renttherunway[renttherunway.index.isin(val_ids)]
    test_sessions=renttherunway[renttherunway.index.isin(test_ids)]

    to_pickled_df(data_directory, sampled_train=train_sessions)
    to_pickled_df(data_directory, sampled_val=val_sessions)
    to_pickled_df(data_directory,sampled_test=test_sessions)