import re

from aiohttp import ClientSession
from discord import Message
from discord.ext import commands

from symm.cogs.cloud_vision import CloudVisionFaceDetection


class Symm(commands.Cog):
    supported_extensions = ("png", "jpg", "jpeg", "bmp", "gif")
    supported_url_pattern = re.compile(rf"https?://[\w/:%#$&?()~.=+\-]+\.({'|'.join(supported_extensions)})")

    def __init__(self, bot):
        self.bot = bot
        self.cloud_vision = CloudVisionFaceDetection()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        image_attachments = [
            attachment
            for attachment in message.attachments
            if attachment.filename.split(".")[-1] in self.supported_extensions
        ]

        if image_attachments:
            attachment = image_attachments[0]
            image = await attachment.read()
            await self.execute(message, image)

        elif m := self.supported_url_pattern.match(message.content):
            async with ClientSession() as session:
                async with session.get(m.group(0)) as response:
                    response.raise_for_status()
                    image = await response.read()
                    await self.execute(message, image)

    async def execute(self, message: Message, image: bytes):
        await message.channel.trigger_typing()

        symmetry_images = self.cloud_vision.apply_symmetry(image)
        await message.reply(files=symmetry_images)


def setup(bot):
    bot.add_cog(Symm(bot))
