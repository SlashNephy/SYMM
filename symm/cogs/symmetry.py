import re
from io import BytesIO

from PIL import Image
from aiohttp import ClientSession
from discord import Message, File
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
            if attachment.filename.split(".")[-1].lower() in self.supported_extensions
        ]

        if image_attachments:
            print("Found image attachment...")

            attachment = image_attachments[0]
            image = await attachment.read()
            await self.execute(message, image)

        elif m := self.supported_url_pattern.match(message.content):
            print("Found image url...")

            async with ClientSession() as session:
                async with session.get(m.group(0)) as response:
                    response.raise_for_status()
                    image = await response.read()
                    await self.execute(message, image)

    async def execute(self, message: Message, image: bytes):
        # 10 MB を超えた場合は無視
        if len(image) > 10 * 2 ** 20:
            print("Image is over 10 MB size.")
            return

        # Cloud Vision API にかける
        faces = self.cloud_vision.detect_from_local(image)

        # カオナシ
        if not faces:
            print("No faces detected.")
            return

        await message.channel.trigger_typing()

        # 検出確度降順でソート
        faces.sort(key=lambda x: x.detection_confidence, reverse=True)

        with BytesIO(image) as fp:
            with Image.open(fp, "r") as raw_image:
                # 最大3個までシンメトリー生成を許可
                symmetry_images = sum([
                    [
                        File(fp=fp,
                             filename=f"face_{i}_{'right_to_left' if j else 'left_to_right'}.{raw_image.format.lower()}")
                        for j, fp in enumerate(self.cloud_vision.generate_symmetry_images(face, raw_image))
                    ]
                    for i, face in enumerate(faces)
                    if i < 4
                ], [])

        await message.reply(files=symmetry_images)
        [symmetry_image.close() for symmetry_image in symmetry_images]


def setup(bot):
    bot.add_cog(Symm(bot))
