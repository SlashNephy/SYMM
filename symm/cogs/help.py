import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="help")
    async def _help(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title="HELP SYMM",
                                  description="コマンド一覧",
                                  color=0x00FFFF)
            embed.add_field(name="**s!help sym**",
                            value="コマンドの一覧と説明を表示",
                            inline=False)
            embed.add_field(name="**s!syml**",
                            value="チャンネル内の直近の画像の左側を使用したシンメトリー画像の送信",
                            inline=False)
            embed.add_field(name="**s!symr**",
                            value="チャンネル内の直近の画像の左側を使用したシンメトリー画像の送信",
                            inline=False)
            embed.add_field(name="**s!sym**",
                            value="s!syml、s!symrの両方の実行結果を送信",
                            inline=False)
            embed.add_field(
                name="**s!sym 1-10\n/syml 1-10\ns!symr 1-10\n**",
                value="1から10の範囲で画像の変化量を指定\nデフォルトは5",
                inline=False,
            )
            await ctx.send(embed=embed)


def setup(bot):
    bot.remove_command("help")
    bot.add_cog(Help(bot))
