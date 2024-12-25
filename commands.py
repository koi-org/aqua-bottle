from data import data

def create_aquarium(data, channel_id): 
    # check if an already existing aquarium exists
    if not data:
        add_aquarium(data, channel_id)
        return True

    aquarium_exists = check_existence(data, channel_id)

    if aquarium_exists:
        return False
    
    add_aquarium(data, channel_id)

    return True


def add_aquarium(data, channel_id):
    aquarium = {

    }
    aquarium['channel_id'] = channel_id

    data.append(aquarium)


def check_existence(data, channel_id):
    for aquarium in data:
        if aquarium['channel_id'] == channel_id:
            return True
        
    return False
