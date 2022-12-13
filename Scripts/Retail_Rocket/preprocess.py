import os

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from utility import to_pickled_df
import datetime 
import time
import matplotlib.pyplot as plt 
import seaborn as sns
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="calculate item popularity")

    parser.add_argument('--data', nargs='?', default='Datasets',
                        help='data directory')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()

    data_directory = args.data
    
    items1 = pd.read_csv(data_directory + "item_properties_part1.csv.zip",compression='zip')
    items2 = pd.read_csv(data_directory + "item_properties_part2.csv.zip",compression='zip')
    events = pd.read_csv(data_directory + "events.csv.zip",compression='zip')
    category_tree = pd.read_csv(data_directory + "category_tree.csv")
    items = pd.concat([items1, items2])
    
    fig, ax = plt.subplots(ncols=1, figsize=(10, 8)) # The figsize of the sample data in inches
    sns.countplot(x='event',
                data=events,
                palette="pastel")

    times =[]
    for i in items['timestamp']:
        times.append(datetime.datetime.fromtimestamp(i//1000.0)) 
    items['timestamp'] = times
    
    print(events.groupby(['event']).event.count())
    sns.countplot(x= 'event', data=events, palette="pastel")
    
    data = events.event.value_counts()
    labels = data.index
    sizes = data.values
    explode = (0, 0.15, 0.15)  # explode 1st slice
    plt.subplots(figsize=(8,8))

    # Plot
    plt.pie(sizes, explode=explode, labels=labels,autopct='%1.1f%%', shadow=False, startangle=0)
    plt.axis('equal')
    plt.show()
    
    items.loc[(items.property=='categoryid')&(items.value == '963')].sort_values('timestamp').head()
    # Show total of all visitors
    print('Total visitors:', events['visitorid'].size)
        
    # Show total of all unique visitors
    all_customers = events['visitorid'].unique()
    print("Unique visitors:", all_customers.size)
    
    # Show total of customers who purchased something

    customer_purchased = events[events.transactionid.notnull()].visitorid.unique()
    customer_purchased.size
    
    # Show total of customers who browsed but did not purchase
    customer_browsed = [x for x in all_customers if x not in customer_purchased]
    len(customer_browsed)
    
    items_new = items.loc[items.property.isin(['categoryid', 'available']), :]

    print("items with categoryid and available as property:", items_new.size)
    items_new.head(10)
    
    # Group itemid by the event type
    grouped = events.groupby('event')['itemid'].apply(list)
    grouped
    
    import operator

    views = grouped['view']
    count_view ={}
    views = np.array(views[:])
    unique, counts = np.unique(views, return_counts=True)
    count_view = dict(zip(unique, counts))

    sort_count_view = sorted(count_view.items(), key = operator.itemgetter(1), reverse = True)
    x = [i[0] for i in sort_count_view[:8]]
    y = [i[1] for i in sort_count_view[:8]]
    sns.barplot(x, y, order=x, palette="vlag")
    
    transaction = grouped['transaction']
    count_transaction ={}
    transaction = np.array(transaction[:])
    unique, counts = np.unique(transaction, return_counts=True)
    count_transaction = dict(zip(unique, counts))

    sort_count_transaction = sorted(count_transaction.items(), key = operator.itemgetter(1), reverse = True)
    x = [i[0] for i in sort_count_transaction[:8]]
    y = [i[1] for i in sort_count_transaction[:8]]
    sns.barplot(x, y, order=x, palette="pastel")
    
    addtocart = grouped['addtocart']
    count_addtocart ={}
    addtocart = np.array(addtocart[:])
    unique, counts = np.unique(addtocart, return_counts=True)
    count_addtocart = dict(zip(unique, counts))

    sort_count_addtocart = sorted(count_addtocart.items(), key = operator.itemgetter(1), reverse = True)
    x = [i[0] for i in sort_count_addtocart[:8]]
    y = [i[1] for i in sort_count_addtocart[:8]]
    sns.barplot(x, y, order=x, palette="rocket")
    
    # Create list of visitors who made a purchase and the purchased items
    customer_purchased = events[events.transactionid.notnull()].visitorid.unique()
    purchased_items = []

    for customer in customer_purchased:
        purchased_items.append(list(events.loc[(events.visitorid == customer) & (events.transactionid.notnull())].itemid.values))
    
    events = events.assign(date=pd.Series(datetime.datetime.fromtimestamp(i/1000).date() for i in events.timestamp))
    events = events.sort_values('date').reset_index(drop=True)
    events = events[['visitorid','itemid','event', 'date']]
    events.head(5)
    
    start_date = '2015-5-3'
    end_date = '2015-5-18'
    fd = lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').date()
    events = events[(events.date >= fd(start_date)) & (events.date <= fd(end_date))]

    to_pickled_df(data_directory, events_processed=events)

