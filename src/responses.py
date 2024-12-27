from aquarium import Aquarium

valid_commands = {
    'daily', 'start', 'shop', 'help'
}

def get_response(user_input: str, channel_id) -> str:
    lowered: str = user_input.lower()[1:]

    if lowered == 'start':
        does_exist = check_existence(data, channel_id)

        if does_exist:
            return 'Aquarium already exists!'

        Aquarium(channel_id)
        return f'create an aquarium in {channel_id}'
        
    elif lowered == 'help':
        return 'This is guppy bot! Your very own aquarist game!'
    elif 'they call you the what' in lowered:
        return 'Ninjas call me the drink'
    elif lowered not in valid_commands:
        return 'Please enter a valid command'
