import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Hello from Lambda")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from GitHub Actions Lambda!')
    }