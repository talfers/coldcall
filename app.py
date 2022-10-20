from log import logging
import pandas as pd
from config import Config
from texter import Texter

logger = logging.getLogger('app.py')
exit_code = 0

config = Config()
texter = Texter(
    config.twilio_account_sid, 
    config.twilio_auth_token, 
    config.twilio_phone_number
)

df = pd.read_csv('./data/contact_data.csv')

for r in df.itertuples():
    number = texter.cleanNumber(getattr(r, 'Phone'))
    if number:
        try:
            message = texter.sendMessage(
                '+15552001370', 
                'heyyyyyy babayyyyy', 
            )
            logger.info(message)
            # logger.info(f'sent message to: {number}')
        except Exception as e:
            logger.error(e)
            exit_code = 1
    else:
        logger.error(f"Unable to get phone number from: {getattr(r, 'Phone')}, index: {getattr(r, 'Index')}")

exit(exit_code)