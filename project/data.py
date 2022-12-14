import schedule 
import time 

import pandas as pd

from dotenv import load_dotenv

from config import contract_collection
from helper import contract_list, get_collection_activity, get_collection_info


load_dotenv()

def func():
    contract_db = contract_list()
    print('Running...')

    test = get_collection_activity(True, 20, community='artblocks')
    new_bids = []
    for item in test['activities']:
        if item['type'] == 'bid':
            if item['order']['criteria']['kind'] == 'collection':
                actions = {}
                actions['contract'] = item['contract']
                actions['collection_name'] = item['collection']['collectionName']
                actions['collection_id'] = item['order']['criteria']['data']['collection']['id']
                if item['order']['criteria']['data']['collection']['id'] not in contract_db:
                    new_bids.append(actions)

    if new_bids:   
        print(f'New Contracts: {len(new_bids)}')            
        contract_collection().insert_many(new_bids)

    contract_db = contract_list()

    new_bids = []
    for c in contract_db:
        collections = get_collection_info(1, True, False, c_id=c)
        for collection in collections['collections']:
            project = {}
            project['Collection'] = collection['name']
            project['7day Volume'] = round(collection['volume']['7day'], 2)
            project['Lowest Floor Price'] = f"{str(collection['floorAsk']['sourceDomain'])} : {round(collection['floorAsk']['price']['amount']['decimal'], 3)}"
            try:
                project['Highest Collection Offer'] = f"{str(collection['topBid']['sourceDomain'])} : {round(collection['topBid']['price']['amount']['decimal'], 3)}"
                project['Spread'] = round(float((collection['floorAsk']['price']['amount']['decimal']) - float(collection['topBid']['price']['amount']['decimal'])) / float(collection['floorAsk']['price']['amount']['decimal']), 2)
            except TypeError:
                project['Highest Collection Offer'] = 'None'
                project['Spread'] = 'None'
            new_bids.append(project)
        

    df = pd.DataFrame(new_bids)    

    return df[~df['Spread'].isin(['None'])].sort_values(by='Collection', ascending=True).to_csv('spread.csv', index=False)


schedule.every(5).minutes.do(func)

while True:
    schedule.run_pending()
    print('Waiting...')
    time.sleep(1)