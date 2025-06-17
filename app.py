import os
import json
import logging
import urllib.parse
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from utils.jira_handler import JiraHandler
from utils.yaml_utils import YamlHandler
from utils.payload_builder import PayloadBuilder

# Setup logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
client = WebClient(token=SLACK_BOT_TOKEN)

yaml_loader = YamlHandler()
team_data_yaml = yaml_loader.load_team_data()
team_data = team_data_yaml["team"]
ticket_details_data = yaml_loader.load_bvt_yaml_data()

payload_builder = PayloadBuilder()
jira_handler = JiraHandler()
