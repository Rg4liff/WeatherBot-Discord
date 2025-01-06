import discord
import os
from discord import Intents, Client, Message
from dotenv import load_dotenv
from responses import get_response

#Bot setup
load_dotenv()
bot_token = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = Client(intents=intents)

@client.event
async def send_message(message: Message, user_message: str) ->None:
    if not user_message:
        print('(MEssage was empty because intents were not enabled)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = str(message.content)
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

def main()-> None:
    client.run(token = bot_token)

if __name__ == '__main__':
    main()