from slackeventsapi import SlackEventAdapter
from slack import WebClient
from zdesk import Zendesk
from zdesk import get_id_from_url
import sys
import search
from dotenv import load_dotenv
load_dotenv()
import os
import jsonify

ZENDESK_URL = "https://" + os.environ["ZENDESK_DOMAIN"] + ".zendesk.com"

# Zenpy client
zendesk = Zendesk(ZENDESK_URL, zdesk_email=os.environ["ZENDESK_CLIENT"], zdesk_password=os.environ["ZENDESK_SECRET"], zdesk_token=True)

# Our app's Slack Event Adapter for receiving actions via the Events API
slack_signing_secret = os.environ["SLACK_SIGNING_SECRET"]
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events")

# Create a SlackClient for your bot to use for Web API requests
slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
slack_client = WebClient(slack_bot_token)

# Example responder to greetings
@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]
    # If the incoming message contains "zendesk ticket", then respond with a "ticket" info
    if message.get("subtype") is None and "https://grubhub-servicedesk.zendesk.com/agent/tickets/" in message.get('text'):
        channel = message["channel"]
        lookup_val = search.find(message.get('text'))[0]
        ticket_id = int(get_id_from_url(lookup_val))
        ticket_data = zendesk.ticket_show(id=ticket_id)["ticket"]["subject"]
        message = ticket_data
        slack_client.chat_postMessage(channel=channel, text=message)

# Example reaction emoji echo
@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    event = event_data["event"]
    emoji = event["reaction"]
    channel = event["item"]["channel"]
    text = ":%s:" % emoji
    slack_client.chat_postMessage(channel=channel, text=text)

# Error events
@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))

# Once we have our event listeners configured, we can start the
# Flask server with the default `/events` endpoint on port 3000
slack_events_adapter.start(port=3000)
