import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands #type: ignore
hands = mp_hands.Hands()

# Initialize the frame size and step size for scrolling
frame_width, frame_height = 640, 480
scroll_step = 100  # You can adjust this value

# Initialize the previous hand position and finger states
prev_hand_y = frame_height // 2
cursor_x, cursor_y = frame_width // 2, frame_height // 2

cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        # Mirror the video
        frame = cv2.flip(frame, 1)

        # Set the frame size
        frame = cv2.resize(frame, (frame_width, frame_height))

        # Convert the frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        extended_fingers = []

        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]

            # Calculate finger states
            extended_fingers = [hand_landmarks.landmark[i].y < hand_landmarks.landmark[i - 2].y for i in range(4, 21, 4)]

            # Count the number of open fingers (except thumb)
            open_fingers = sum(1 for finger_id, extended in enumerate(extended_fingers) if extended)
            cv2.putText(frame, f'Open Fingers: {open_fingers}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Check if one finger (index) is open
            if extended_fingers[1]:
                # Move the cursor
                hand_x = int(hand_landmarks.landmark[0].x * 1980)
                hand_y = int(hand_landmarks.landmark[0].y * 1200)
                pyautogui.moveTo(hand_x, hand_y, duration=0.1)

            # Check if two fingers (index and middle) are open
            if extended_fingers[1] and extended_fingers[2]:
                hand_y = int(hand_landmarks.landmark[0].y * frame_height)

                # Check if hand moved up
                if hand_y < prev_hand_y - 10:
                    pyautogui.scroll(-scroll_step)  # Scroll up

                # Check if hand moved down
                elif hand_y > prev_hand_y + 10:
                    pyautogui.scroll(scroll_step)  # Scroll down

                prev_hand_y = hand_y

            finger_tips = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
            for tip_id in finger_tips:
                height, width, _ = frame.shape
                tip_landmark = hand_landmarks.landmark[tip_id]
                tip_x, tip_y = int(tip_landmark.x * width), int(tip_landmark.y * height)
                cv2.circle(frame, (tip_x, tip_y), 10, (0, 0, 255), -1)

        cv2.imshow('Hand Gesture Scrolling', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
