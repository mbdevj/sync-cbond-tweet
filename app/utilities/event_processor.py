from app.utilities import parameters_handler
from app.connections import twitter
import os


def process_create_event_and_tweet(event):
    print("executing created")
    lpt_pair = parameters_handler.get_lpt_pair(event)
    token_id = parameters_handler.get_token_id(event)
    total_value_usd = parameters_handler.get_total_value_usd(token_id)
    duration = parameters_handler.get_duration(token_id)
    interest_upon_maturity = parameters_handler.get_interest_upon_maturity(token_id)
    image = parameters_handler.get_image(token_id)
    rarity = parameters_handler.get_rarity(token_id)
    text = parameters_handler.get_created_tweet_text(rarity, lpt_pair, token_id, total_value_usd, interest_upon_maturity, duration)
    # twitter.update_status_with_media(text, image)
    os.remove(image)
    print(lpt_pair)
    print(token_id)
    print(total_value_usd)
    print(duration)


def process_mature_event_and_tweet(event):
    print("executing matured")
    lpt_pair = parameters_handler.get_lpt_pair(event)
    token_id = parameters_handler.get_token_id(event)
    total_value_usd = parameters_handler.get_total_value_usd(token_id)
    print(event)
    print(lpt_pair)
    print(total_value_usd)
    text = parameters_handler.get_matured_tweet_text(lpt_pair, token_id, total_value_usd)
    image = parameters_handler.get_image(token_id)
    # twitter.update_status_with_media(text, image)
    print(text)
