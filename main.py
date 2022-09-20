import json
class DataClassCard:
    rank: str
    suit: str

DataClassCard.rank = '34'
DataClassCard.suit = 'Green'

class Serial:
    def __init__(self,name,age):
        self.name = name
        self.age = age

s1 = Serial('sibin','26')
json_info = json.dumps(s1.__dict__)
print(json_info)
