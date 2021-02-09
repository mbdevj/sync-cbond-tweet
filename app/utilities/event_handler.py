#!/usr/bin/python3


def handle_transfer_event(event):
    token_id = int((event['topics'][3].hex()), 16)
    return token_id


def handle_create_event(event):
    token_id = int((event['data'][-10:]), 16)
    return token_id

# Might need to hold off for now until we have this event occur
# def handle_mature_event(event):
#     token_id = int(event['data'][-10:], 16)
#     return token_id
