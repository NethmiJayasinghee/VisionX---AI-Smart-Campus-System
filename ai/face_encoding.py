from deepface import DeepFace



def create_face_embedding(image_path):

    try:

        result = DeepFace.represent(
            img_path=image_path,
            model_name="Facenet"
        )


        if result:

            embedding = result[0]["embedding"]

            return embedding


        return None


    except Exception as e:

        print("Face Encoding Error:", e)

        return None