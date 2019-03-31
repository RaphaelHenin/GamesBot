from wit import Wit

access_token = "DQBWQ32EXR6VQFKBDK2BCQEHADZGYOCM"

client = Wit(access_token = access_token)
message_text = "What is the best game on XBOX360 ?"
resp = client.message(message_text)
print(resp)