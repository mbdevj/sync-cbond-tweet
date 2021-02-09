from app.utilities import parameters_handler
from app.connections import twitter


def process_create_event_and_tweet(event):
    token_id = parameters_handler.get_token_id(event)
    lpt_pair = parameters_handler.get_lpt_pair(event)
    lpt_value = parameters_handler.get_lpt_value(token_id)
    duration = parameters_handler.get_duration(token_id)
    total_value_of_bonded_sync = parameters_handler.get_total_value_of_bonded_sync(token_id)
    apr = parameters_handler.get_apr(token_id)
    image = parameters_handler.get_image(token_id)
    text = parameters_handler.get_tweet_text(token_id,duration, total_value_of_bonded_sync, lpt_value, lpt_pair, apr)
    return twitter.update_status_with_media(text, image)
