import requests

from os import getenv
from config import contract_collection


def contract_list():
    """
    Creates a list of all NFT contracts
    """
    contracts = contract_collection()
    contract_list = []
    for item in contracts.find():
        contract_list.append(item['collection_id'])
    return contract_list


def get_collection_activity(metadata, limit, collection=None, collectionssetid=None, community=None, continuation=None):
    url = 'https://api.reservoir.tools/'
    end_point = 'collections/activity/v5'
    headers = {'accept': '*/*', 'x-api-key': f"{getenv('RESERVOIR')}"}
    if community == None:
        r = requests.get(url + end_point, params=f'?sortBy=eventTimestamp&includeMetadata={metadata}&limit={limit}', headers=headers)
    else:
        r = requests.get(url + end_point, params=f'?sortBy=eventTimestamp&includeMetadata={metadata}&limit={limit}&community={community}', headers=headers)
    data = r.json()
    return data


def get_collection_info(limit, topbid, normalize, c_id=None):
    url = 'https://api.reservoir.tools/'
    end_point = 'collections/v5'
    headers = {'accept': '*/*', 'x-api-key': f"{getenv('RESERVOIR')}"}
    r = requests.get(url + end_point, params=f'id={c_id}&includeTopBid={topbid}&normalizeRoyalties={normalize}&sortBy=allTimeVolume&limit={limit}', headers=headers)
    data = r.json()
    return data