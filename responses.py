from random import randint, choice
from commands import create_aquarium
from data import data

valid_commands = {
    'daily', 'start', 'shop', 'help'
}

def get_response(user_input: str, channel_id) -> str:
    lowered: str = user_input.lower()[1:]

    if lowered == 'start':
        new_aquarium = create_aquarium(data, channel_id)

        if new_aquarium:
            return f'create an aquarium in {channel_id}'
        
        return f'Aquarium already exists!'
    elif lowered == 'help':
        return 'This is guppy bot! Your very own aquarist game!'
    elif 'they call you the what' in lowered:
        return 'Ninjas call me the drink'
    elif lowered not in valid_commands:
        return 'Please enter a valid command'
