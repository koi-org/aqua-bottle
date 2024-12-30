from user import User
from user_manager import UserManager

valid_commands = {"daily", "start", "shop", "help"}


def get_response(user_input: str, message) -> str:
    lowered: str = user_input.lower()[1:]

    command_message = lowered.split(" ")

    channel_id = message.channel.id
    author_id = message.author.id
    author_name = ""

    if lowered == "register":
        ret_string = ""

        if len(command_message) == 1:
            author_name = message.author.name
        else:
            author_name = command_message[1]

        new_user = User(author_name, int(author_id), 100)

        if not new_user:
            ret_string = "User already registered!"
        else:
            UserManager.add_user(new_user)
            ret_string = f"Welcome {author_name}!"

        return ret_string
    elif lowered == "help":
        return "This is guppy bot! Your very own aquarist game!"
    elif "they call you the what" in lowered:
        return "Ninjas call me the drink"
    elif lowered not in valid_commands:
        return "Please enter a valid command"
