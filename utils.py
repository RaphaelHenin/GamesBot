from wit import Wit
import os

access_token = os.environ['WIT_ACCESS_TOKEN']

client = Wit(access_token=access_token)

def bot_response(message_text):
    resp = client.message(message_text)
    entities = {}
    try:
        for entity in list(resp["entities"]):
            print(entity)
            entities[entity] = resp["entities"][entity][0]["value"]
    except:
        pass
    return (entities)


#print(bot_response("What is the best game on XBOX360 in NA ?"))
