import os
import traceback

import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.all()
cogs = [
    "cogs.help",
    "cogs.symmetry",
]

# cogs.help = ヘルプコマンド
# cogs.symmetry = シンメトリー処理の実行


class SymmBot(commands.Bot):
    async def on_ready(self):
        print("-----")
        print(self.user.name)
        print(self.user.id)
        print("-----")


if __name__ == "__main__":
    load_dotenv()
    try:
        BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]
    except KeyError:
        raise ValueError("`DISCORD_BOT_TOKEN` is not defined in your env.")

    # command_prefix='s!'でコマンドの開始文字を指定
    bot = SymmBot(command_prefix="s!", help_command=None, intents=intents)

    for cog in cogs:
        try:
            bot.load_extension(cog)
        except Exception:
            traceback.print_exc()

    bot.run(BOT_TOKEN)  # Botのトークン
