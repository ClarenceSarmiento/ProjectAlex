import face_recognition
import cv2
from service import Alex_voice
import time
import Alex

video_capture = cv2.VideoCapture(0)

clarence_image = face_recognition.load_image_file('clarence.jpg')
clarence_facial_encoding = face_recognition.face_encodings(clarence_image)[0]

known_face_encoding = [
    clarence_facial_encoding
]
known_face_names = [
    'Clarence'
]

while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]

    face_location = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_location)
    for (top, right, bottom, left), face_encodings in zip(face_location, face_encodings):
        matches = face_recognition.compare_faces(known_face_encoding, face_encodings)
        Alex_voice.speak('Scanning face...')
        time.sleep(3)
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            Alex_voice.speak('Face scanning completed.')
            Alex_voice.speak(f'Welcome back {name}.')
            Alex.alex()
        else:
            Alex_voice.speak('Unauthorized person')
            Alex_voice.speak('Going Offline.')
            exit()
        video_capture.release()
        cv2.destroyAllWindows()
