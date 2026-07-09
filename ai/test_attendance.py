import sys
import os


# Add project root path
sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


from ai.face_recognition import start_face_recognition



start_face_recognition()