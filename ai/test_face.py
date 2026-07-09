import os
from PIL import Image

from face_encoding import create_face_embedding


current_dir = os.path.dirname(__file__)

image_path = os.path.join(
    current_dir,
    "newphtkushan.jpeg"
)


print("Path:", image_path)

print("Exists:", os.path.exists(image_path))


# Test image open
try:

    img = Image.open(image_path)

    print("Image opened successfully")
    print("Image size:", img.size)


except Exception as e:

    print("Image open error:", e)



encoding = create_face_embedding(image_path)


if encoding:

    print("✅ Face detected successfully")
    print("Embedding length:", len(encoding))

else:

    print("❌ No face detected")