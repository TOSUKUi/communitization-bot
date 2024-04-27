# This example requires the 'message_content' intent.

import os
from . import ai
import sys
import traceback
from discord import Intents, Client, Interaction
from discord.app_commands import CommandTree


class MyClient(Client):
    def __init__(self, intents: Intents) -> None:
        super().__init__(intents=intents)
        self.tree = CommandTree(self)

    async def setup_hook(self) -> None:
        await self.tree.sync()

    async def on_ready(self):
        print(f"login as: {self.user.name} [{self.user.id}]")


intents = Intents.default()
client = MyClient(intents=intents)


@client.tree.command()
async def hello(interaction: Interaction):
    await interaction.response.send_message(f'Hello, {interaction.user.mention}')

@client.tree.command()
async def communitization(interaction: Interaction, text: str):
    try:
        base_message = await interaction.response.send_message("生成中だ、邪魔するな")
        res = ai.ai_processing(text)
        count = 0
        msg = "=>"
        for message in res:
            end_flag = False
            if message is None:
                message = ""
                end_flag = True
            msg += message
            count += 1
            if count > 10 or message == "":
                await interaction.edit_original_response(content=msg)
                count = 0
            if end_flag:
                break
    except Exception as e:
        print(traceback.print_exception(e))
        restart_bot()

def restart_bot():
  client.close()
  os.execv(sys.executable, ['python'] + sys.argv)

def run_bot():
    client.run(os.getenv("DISCORD_BOT_TOKEN"))
