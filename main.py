import cv2
import mediapipe as mp
import time
import pydirectinput
import pyautogui


pyautogui.FAILSAFE = False

capture = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1,
                       min_detection_confidence=0.5, min_tracking_confidence=0.5)

mp_drawing = mp.solutions.drawing_utils

while True:
    success, frame = capture.read()
    if not success:
        break

    image_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(image_RGB)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            hand_center_x = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * frame.shape[1])
            hand_center_y = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * frame.shape[0])

            
            pyautogui.moveTo(hand_center_x, hand_center_y)

            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
            pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
            middle_finger_mcp  = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]

            cv2.putText(frame, f"Thumb tip y: {round(thumb_tip.y, 2)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 255, 0), 2)
            cv2.putText(frame, f"Index tip y: {round(index_finger_tip.y, 2)}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 255, 0), 2)
            cv2.putText(frame, f"Middle tip y: {round(middle_finger_tip.y, 2)}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 255, 0), 2)
            cv2.putText(frame, f"Ring tip y: {round(ring_finger_tip.y, 2)}", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 255, 0), 2)
            cv2.putText(frame, f"Pinky tip y: {round(pinky_tip.y, 2)}", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 255, 0), 2)
            cv2.putText(frame, f"Middle mcp y: {round(middle_finger_mcp.y, 2)}", (10, 180), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 255, 0), 2)

            is_hand_closed = False
            if (middle_finger_mcp.y < middle_finger_tip.y):
                is_hand_closed = True

            if is_hand_closed:
                pyautogui.rightClick()  

    cv2.imshow('Game', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
