import cv2
import json
import numpy as np

from deepface import DeepFace

from database.database import (
    get_students,
    mark_attendance
)



# ---------------- LOAD REGISTERED FACES ----------------

def load_known_faces():

    students = get_students()

    known_faces = []


    for student in students:

        try:

            if student[6] == "":
                continue


            encoding = json.loads(
                student[6]
            )


            known_faces.append({

                "student_id": student[1],

                "name": student[2],

                "encoding": np.array(
                    encoding
                )

            })


        except Exception as e:

            print(
                "Encoding Load Error:",
                e
            )


    return known_faces





# ---------------- FACE DISTANCE ----------------


def calculate_distance(
        live_encoding,
        known_encoding
):


    distance = np.linalg.norm(

        live_encoding - known_encoding

    )


    return distance





# ---------------- COMPARE FACES ----------------


def find_best_match(
        live_encoding,
        known_faces
):


    best_name = "Unknown"

    best_id = None

    lowest_distance = 999



    for student in known_faces:


        distance = calculate_distance(

            live_encoding,

            student["encoding"]

        )


        print(
            student["name"],
            "Distance:",
            distance
        )



        if distance < lowest_distance:

            lowest_distance = distance

            best_name = student["name"]

            best_id = student["student_id"]




    # Threshold

    if lowest_distance < 10:


        return (

            best_id,

            best_name,

            lowest_distance

        )


    return (

        None,

        "Unknown",

        lowest_distance

    )






# ---------------- START CAMERA ----------------


def start_face_recognition():


    known_faces = load_known_faces()



    if len(known_faces) == 0:

        print(
            "No registered students found"
        )

        return




    camera = cv2.VideoCapture(0)



    marked_students = set()



    while True:


        ret, frame = camera.read()



        if not ret:

            break




        try:


            result = DeepFace.represent(

                frame,

                model_name="Facenet",

                enforce_detection=False

            )



            live_encoding = np.array(

                result[0]["embedding"]

            )




            student_id, name, distance = find_best_match(

                live_encoding,

                known_faces

            )




            display_text = (

                f"{name}  Distance:{distance:.2f}"

            )




            # Attendance save once

            if student_id is not None:


                if student_id not in marked_students:


                    mark_attendance(

                        student_id,

                        name

                    )


                    marked_students.add(

                        student_id

                    )


                    print(

                        "Attendance Marked:",
                        name

                    )




            cv2.putText(

                frame,

                display_text,

                (50,50),

                cv2.FONT_HERSHEY_SIMPLEX,

                0.8,

                (0,255,0),

                2

            )




        except Exception as e:


            print(

                "Recognition Error:",
                e

            )





        cv2.imshow(

            "VisionX Face Attendance",

            frame

        )




        if cv2.waitKey(1) & 0xFF == ord('q'):

            break





    camera.release()

    cv2.destroyAllWindows()