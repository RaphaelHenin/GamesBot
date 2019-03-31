# Python libraries that we need to import for our bot
import random
import os
from utils import bot_response
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
bot = Bot(ACCESS_TOKEN)

# We will receive messages that Facebook sends our bot at this endpoint
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook."""
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    # if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    # Facebook Messenger ID for user so we know where to send response back to
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        #response_sent_text = get_message()
                        response_to_send = ""
                        response = bot_response(message['message'].get('text'))
                        if 'toprank' in response:
                            response_to_send += "You want the best game "
                        if 'badrank' in response:
                            response_to_send += "You want the worst game "
                        if 'genre_question' in response:
                            response_to_send += "You want the genre "
                        if 'developer' in response:
                            response_to_send += "You want the developer "
                        if 'genre' in response:
                            response_to_send += " You want a(n) {} game ".format(
                                str(response['genre']))
                        if 'Year_of_Release' in response:
                            response_to_send += 'You want to know the realeased date '
                        if 'sale' in response:
                            response_to_send += "in terms of sales "
                        if 'publisher' in response:
                            response_to_send += "of {} ".format(
                                str(response['publisher']))
                        if 'game_name' in response:
                            response_to_send += "of {} ".format(
                                str(response['game_name']))
                        if 'location' in response:
                            response_to_send += "in {} ".format(
                                str(response['location']))
                        if 'game_platform' in response:
                            response_to_send += "on the platform {}".format(
                                str(response['game_platform']))
                        send_message(recipient_id, response_to_send)
                    # if user sends us a GIF, photo,video, or any other non-text item
                    if message['message'].get('attachments'):
                        response_sent_nontext = get_message()
                        send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    # take token sent by facebook and verify it matches the verify token you sent
    # if they match, allow the request, else return an error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


# chooses a random message to send to the user
def get_message():
    sample_responses = ["You are stunning!", "We're proud of you.",
                        "Keep on being you!", "We're greatful to know you :)"]
    # return selected item to the user
    return random.choice(sample_responses)

# uses PyMessenger to send response to user


def send_message(recipient_id, response):
    # sends user the text message provided via input response parameter
    if(response == ""):
        response = "Sorry but I don't understand"
    bot.send_text_message(recipient_id, response)
    return "success"


if __name__ == "__main__":
    app.run()
