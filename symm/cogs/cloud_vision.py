from io import BytesIO
from typing import List, Optional

from PIL import Image, ImageDraw
from google.cloud import vision
from discord import File


class CloudVisionFaceDetection:
    def __init__(self):
        self.client = vision.ImageAnnotatorClient()

    def detect_from_local(self, image_content: bytes):
        # noinspection PyTypeChecker
        image = vision.Image(content=image_content)

        response = self.client.face_detection(image=image)

        if response.error.message:
            print(response.error.message)
            return []
        return response.face_annotations

    def detect_from_remote(self, image_uri: str):
        image = vision.Image()
        image.source.image_uri = image_uri

        response = self.client.face_detection(image=image)

        if response.error.message:
            print(response.error.message)
            return []
        return response.face_annotations

    @staticmethod
    def generate_left_to_right_symmetry_image(raw_image, face_coordinate: int) -> BytesIO:
        # 元画像の縦幅
        raw_image_height = raw_image.size[1]

        # 新しい画像を作成する
        new_image_width = face_coordinate * 2 + 20
        new_image_height = raw_image_height + 20
        new_image = Image.new("RGBA", (new_image_width, new_image_height), (255, 255, 255, 255))

        # 元画像から左半分を切り抜く
        left_image = raw_image.crop((0, 0, face_coordinate, raw_image_height + 20))

        # 切り抜いた左半分を新しい画像に貼り付ける
        new_image.paste(left_image, (10, 10))

        # 左半分の画像を左右反転する
        right_image = left_image.transpose(Image.FLIP_LEFT_RIGHT)

        # 反転した右半分を新しい画像に貼り付ける
        new_image.paste(right_image, (face_coordinate + 10, 10))

        fp = BytesIO()
        new_image.save(fp, raw_image.format, optimize=True)
        return fp

    @staticmethod
    def generate_right_to_left_symmetry_image(raw_image, face_coordinate: int) -> BytesIO:
        # 元画像の横幅, 縦幅
        raw_image_width, raw_image_height = raw_image.size

        # 新しい画像を作成する
        new_image_width = (raw_image_width - face_coordinate) * 2 + 20
        new_image_height = raw_image_height + 20
        new_image = Image.new("RGBA", (new_image_width, new_image_height), (255, 255, 255, 255))

        # 元画像から右半分を切り抜く
        right_image = raw_image.crop((face_coordinate, 0, raw_image_width, raw_image_height))

        # 切り抜いた右半分を新しい画像に貼り付ける
        img2_size = raw_image_width - face_coordinate
        new_image.paste(right_image, (img2_size + 10, 10))

        # 右半分の画像を左右反転する
        left_image = right_image.transpose(Image.FLIP_LEFT_RIGHT)

        # 反転した左半分を新しい画像に貼り付ける
        new_image.paste(left_image, (10, 10))

        fp2 = BytesIO()
        new_image.save(fp2, raw_image.format, optimize=True)
        return fp2

    @classmethod
    def generate_symmetry_images(cls, face, raw_image):
        print(f"Processing face: {face}")

        # 顔を囲む4点
        boxes = [
            (vertice.x, vertice.y)
            for vertice in face.fd_bounding_poly.vertices
        ]

        # 顔を四角で囲む
        draw_img = ImageDraw.Draw(raw_image)
        draw_img.line(boxes + [boxes[0]], width=1, fill="#ffffff")

        # x座標のミッドレンジを顔の分割位置とする
        x_coordinates = [x for x, _ in boxes]
        face_coordinate = int((min(x_coordinates) + max(x_coordinates)) / 2)

        return cls.generate_left_to_right_symmetry_image(raw_image, face_coordinate), cls.generate_right_to_left_symmetry_image(raw_image, face_coordinate)

    def apply_symmetry(self, image_content: bytes) -> Optional[List[File]]:
        """
        シンメトリー画像生成を行う
        :param image_content: 元画像のバイナリデータ
        :return: 画像のバイナリデータ, 元画像と同じ画像フォーマットで作成される, 呼び出し側で close() する必要がある
        """

        # 10 MB を超えた場合は無視
        if len(image_content) > 10 * 2 ** 20:
            print("Image is over 10 MB size.")
            return

        # Cloud Vision API にかける
        faces = self.detect_from_local(image_content)

        # カオナシ
        if not faces:
            return

        # 検出確度降順でソート
        faces.sort(key=lambda x: x.detection_confidence, reverse=True)

        with BytesIO(image_content) as fp:
            with Image.open(fp, "r") as raw_image:
                # 最大3個までシンメトリー生成を許可
                return sum([
                    [
                        File(fp=fp, filename=f"face_{i}_{'right_to_left' if j else 'left_to_right'}.{raw_image.format.lower()}")
                        for j, fp in enumerate(self.generate_symmetry_images(face, raw_image))
                    ]
                    for i, face in enumerate(faces)
                    if i < 4
                ], [])
