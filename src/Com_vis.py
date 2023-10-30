import cv2
import face_recognition
import os

class FaceRecognitionModule:
    def __init__(self, known_faces_folder):
        self.known_face_encodings = []
        self.known_face_names = []
        self.known_faces_folder = known_faces_folder
        self.process_this_frame = True
        self.video_capture = cv2.VideoCapture(0)
        # self.gender_model = cv2.dnn.readNetFromCaffe("deploy_gender.prototxt", "gender_net.caffemodel")


    def load_known_faces(self):
        for file_name in os.listdir(self.known_faces_folder):
            if file_name.endswith(".jpg"):
                image_path = os.path.join(self.known_faces_folder, file_name)
                image = face_recognition.load_image_file(image_path)
                face_encoding = face_recognition.face_encodings(image)[0]
                name = os.path.splitext(file_name)[0]
                self.known_face_encodings.append(face_encoding)
                self.known_face_names.append(name)

    def recognize_faces(self):
        self.video_capture = cv2.VideoCapture(0)
        self.load_known_faces()
        while True:
            ret, frame = self.video_capture.read()
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            if self.process_this_frame:
                face_locations = face_recognition.face_locations(small_frame)
                face_encodings = face_recognition.face_encodings(small_frame, face_locations)
                face_names = []

                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                    name = "Unknown"

                    if True in matches:
                        first_match_index = matches.index(True)
                        name = self.known_face_names[first_match_index]

                    face_names.append(name)

            self.process_this_frame = not self.process_this_frame

            for (top, right, bottom, left), name in zip(face_locations, face_names): #type: ignore
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.release()

    def release(self):
        self.video_capture.release()
        cv2.destroyAllWindows()

    def recognize_user(self):
        self.video_capture = cv2.VideoCapture(0)
        self.load_known_faces()
        ret, frame = self.video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)
        face_names = []

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = self.known_face_names[first_match_index]

            face_names.append(name)
        self.release()
        if "Unknown" in face_names:
            return None
        else:
            return ", ".join(face_names)

    def add_new_face(self, name, gesture_key='c', quit='q'):
        self.video_capture = cv2.VideoCapture(0)
        while True:
            ret, frame = self.video_capture.read()

            if not ret or frame is None:
                print("Error: Cannot capture a frame from the camera.")
                return

            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            face_locations = face_recognition.face_locations(small_frame)

            if not face_locations:
                print("No face detected for recognition.")
                continue

            cv2.imshow('Video', frame)

            # Check for the specific gesture key press (e.g., 'c' for capture)
            key = cv2.waitKey(1) & 0xFF
            if key == ord(gesture_key):
                # Save the face image with the provided name
                for i, (top, right, bottom, left) in enumerate(face_locations):
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4
                    face_image = frame[top:bottom, left:right]
                    image_path = os.path.join(self.known_faces_folder, f"{name}.jpg")
                    cv2.imwrite(image_path, face_image)
                print(f"Face image for {name} captured.")
                break
            elif key == ord(quit):
                break
        self.release()

    def remove_user_images(self, username):
        user_images_folder = os.path.join(self.known_faces_folder, username)
        if os.path.exists(user_images_folder):
            for file_name in os.listdir(user_images_folder):
                file_path = os.path.join(user_images_folder, file_name)
                os.remove(file_path)
            os.rmdir(user_images_folder)
            return f"Images for user '{username}' removed."
        else:
            return f"No images found for user '{username}'."

