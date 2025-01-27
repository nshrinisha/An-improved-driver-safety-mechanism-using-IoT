import dlib
from scipy.spatial import distance
import cv2

EYE_AR_THRESH = 0.26
EYE_AR_CONSEC_FRAMES = 5
COUNTER = 0
dlib_facelandmark = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def calculate_EAR(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

def detect_drowsiness(frame):
    global COUNTER
    print("Analyzing frame for drowsiness...")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hog_face_detector = dlib.get_frontal_face_detector()
    faces = hog_face_detector(gray)

    for face in faces:
        face_landmarks = dlib_facelandmark(gray, face)
        left_eye = [(face_landmarks.part(n).x, face_landmarks.part(n).y) for n in range(36, 42)]
        right_eye = [(face_landmarks.part(n).x, face_landmarks.part(n).y) for n in range(42, 48)]

        left_ear = calculate_EAR(left_eye)
        right_ear = calculate_EAR(right_eye)

        ear = (left_ear + right_ear) / 2
        if ear < EYE_AR_THRESH:
            COUNTER += 1
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                print("Drowsiness detected.")
                return True
        else:
            COUNTER = 0

    return False