import boto3
import io
from PIL import Image, ImageDraw, ImageFont

example_image = 'dev/example.jpg'

rekognition_client = boto3.client('rekognition')

with open(example_image, 'rb') as image:
    image_bytes = image.read()

    response = rekognition_client.detect_labels(Image={'Bytes': image_bytes})

    image = Image.open(io.BytesIO(image_bytes))

    font = ImageFont.truetype('dev/fonts/arial.ttf', size=32)

    draw = ImageDraw.Draw(image)

    width, height = image.size

    for label in response['Labels']:
        name = label['Name']

        for instance in label['Instances']:
            bounding_box = instance['BoundingBox']

            x0 = int(bounding_box['Left'] * width)
            y0 = int(bounding_box['Top'] * height)
            x1 = x0 + int(bounding_box['Width'] * width)
            y1 = y0 + int(bounding_box['Height'] * height)

            draw.rectangle([x0, y0, x1, y1], outline=(255, 0, 0), width=10)
            draw.text((x0, y1), name, font=font, fill=(255, 0, 0))

    image.save('dev/output.jpg')