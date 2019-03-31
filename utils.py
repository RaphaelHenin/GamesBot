from wit import Wit

access_token = "DQBWQ32EXR6VQFKBDK2BCQEHADZGYOCM"

client = Wit(access_token=access_token)


def bot_response(message_text):
    resp = client.message(message_text)
    entities = {}
    try:
        for entity in list(resp["entities"]):
            entities[entity] = resp["entities"][entity][0]["value"]
    except:
        pass
    return (entities)


#print(bot_response("What is the best game on XBOX360 ?"))
