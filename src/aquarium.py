from data import data

class Aquarium:
    def __init__(self, channel_id):
        self.channel_id = channel_id
        self.create_aquarium(data, channel_id)

    
    def create_aquarium(self, data, channel_id):
        aquarium = {
            'channel_id': channel_id
        }
        data.append(aquarium)


def check_existence(data, channel_id):
    for aquarium in data:
        if aquarium['channel_id'] == channel_id:
            return True
        
    return False