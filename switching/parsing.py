HOST = 'https://img-api.neople.co.kr/df/items/'
def extract_item(dataset, name):
    rdata = []
    # print(dataset)
    if dataset['skill']['buff'][name] !=  None:
        for data in dataset['skill']['buff'][name]:
            ret = {}
            ret['slotId'] = data['slotId']
            itemId = data['itemId']
            ret['url'] = HOST + itemId
            ret['itemName'] = data['itemName']
            rdata.append(ret)
            # print(ret)
        return rdata
    else:
        return None

def extract_creature(dataset, name):
    rdata = []
    if dataset['skill']['buff'][name] !=  None:
        ret = {}
        data = dataset['skill']['buff'][name][0]
        itemId = data['itemId']
        ret['url'] = HOST + itemId
        ret['itemName'] = data['itemName']
        rdata.append(ret)
        # print(ret)
        return rdata
    else:
        return None
def extract_skillName(dataset):
    rdata = []
    if dataset['skill']['buff']['skillName'] !=  None:
        ret = {}
        ret['skillName'] = dataset['skill']['buff']['skillName']
        rdata.append(ret)
        return rdata
    else:
        return None
