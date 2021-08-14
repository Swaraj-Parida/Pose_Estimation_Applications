import cv2
import numpy as np
import mediapipe as mp
from helper import *

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
hands = []

print("Choose:-\n1.Basic Hand Signs")
menu = int(input())
print("Your choice:- "+ str(menu))

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        success, image = cap.read()
        # if not success:
        #   print("Ignoring empty camera frame.")
        #   # If loading a video, use 'break' instead of 'continue'.
        #   continue
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        results = holistic.process(image)

        image_height, image_width, _ = image.shape
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if menu == 1:
            # Extract landmarks
            try:
                landmarks = results.right_hand_landmarks.landmark

                ## Get coordinates
                # Get wrist
                wrist = [landmarks[mp_holistic.HandLandmark.WRIST.value].x,
                         landmarks[mp_holistic.HandLandmark.WRIST.value].y]
                # Get Tips
                thumb_tip = [landmarks[mp_holistic.HandLandmark.THUMB_TIP.value].x,
                             landmarks[mp_holistic.HandLandmark.THUMB_TIP.value].y]
                index_tip = [landmarks[mp_holistic.HandLandmark.INDEX_FINGER_TIP.value].x,
                             landmarks[mp_holistic.HandLandmark.INDEX_FINGER_TIP.value].y]
                middle_tip = [landmarks[mp_holistic.HandLandmark.MIDDLE_FINGER_TIP.value].x,
                              landmarks[mp_holistic.HandLandmark.MIDDLE_FINGER_TIP.value].y]
                ring_tip = [landmarks[mp_holistic.HandLandmark.RING_FINGER_TIP.value].x,
                            landmarks[mp_holistic.HandLandmark.RING_FINGER_TIP.value].y]
                pinky_tip = [landmarks[mp_holistic.HandLandmark.PINKY_TIP.value].x,
                             landmarks[mp_holistic.HandLandmark.PINKY_TIP.value].y]
                # Get MCP points
                thumb_mcp = [landmarks[mp_holistic.HandLandmark.THUMB_MCP.value].x,
                             landmarks[mp_holistic.HandLandmark.THUMB_MCP.value].y]
                index_mcp = [landmarks[mp_holistic.HandLandmark.INDEX_FINGER_MCP.value].x,
                             landmarks[mp_holistic.HandLandmark.INDEX_FINGER_MCP.value].y]
                middle_mcp = [landmarks[mp_holistic.HandLandmark.MIDDLE_FINGER_MCP.value].x,
                              landmarks[mp_holistic.HandLandmark.MIDDLE_FINGER_MCP.value].y]
                ring_mcp = [landmarks[mp_holistic.HandLandmark.RING_FINGER_MCP.value].x,
                            landmarks[mp_holistic.HandLandmark.RING_FINGER_MCP.value].y]
                pinky_mcp = [landmarks[mp_holistic.HandLandmark.PINKY_MCP.value].x,
                             landmarks[mp_holistic.HandLandmark.PINKY_MCP.value].y]

                # Identify sign
                hand_sign, text_origin = calculate_hand_sign(wrist, thumb_tip, index_tip, middle_tip, ring_tip, pinky_tip, thumb_mcp, index_mcp, middle_mcp, ring_mcp, pinky_mcp)
                # Visualize sign
                cv2.putText(image, str(hand_sign), (int(text_origin[0]*640)+40, int(text_origin[1]*480)-40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2, cv2.LINE_AA)
            except:
                pass
            mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2))
            cv2.imshow('MediaPipe Holistic', image)


            if cv2.waitKey(5) & 0xFF == 27:
                break
    cap.release()

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        success, image = cap.read()
        # if not success:
        #   print("Ignoring empty camera frame.")
        #   # If loading a video, use 'break' instead of 'continue'.
        #   continue
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        results = holistic.process(image)

        image_height, image_width, _ = image.shape
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if menu == 1:
            # Extract landmarks
            try:
                landmarks = results.right_hand_landmarks.landmark

                ## Get coordinates
                # Get wrist
                wrist = [landmarks[mp_holistic.HandLandmark.WRIST.value].x,
                         landmarks[mp_holistic.HandLandmark.WRIST.value].y]
                # Get Tips
                thumb_tip = [landmarks[mp_holistic.HandLandmark.THUMB_TIP.value].x,
                             landmarks[mp_holistic.HandLandmark.THUMB_TIP.value].y]
                index_tip = [landmarks[mp_holistic.HandLandmark.INDEX_FINGER_TIP.value].x,
                             landmarks[mp_holistic.HandLandmark.INDEX_FINGER_TIP.value].y]
                middle_tip = [landmarks[mp_holistic.HandLandmark.MIDDLE_FINGER_TIP.value].x,
                              landmarks[mp_holistic.HandLandmark.MIDDLE_FINGER_TIP.value].y]
                ring_tip = [landmarks[mp_holistic.HandLandmark.RING_FINGER_TIP.value].x,
                            landmarks[mp_holistic.HandLandmark.RING_FINGER_TIP.value].y]
                pinky_tip = [landmarks[mp_holistic.HandLandmark.PINKY_TIP.value].x,
                             landmarks[mp_holistic.HandLandmark.PINKY_TIP.value].y]
                # Get MCP points
                thumb_mcp = [landmarks[mp_holistic.HandLandmark.THUMB_MCP.value].x,
                             landmarks[mp_holistic.HandLandmark.THUMB_MCP.value].y]
                index_mcp = [landmarks[mp_holistic.HandLandmark.INDEX_FINGER_MCP.value].x,
                             landmarks[mp_holistic.HandLandmark.INDEX_FINGER_MCP.value].y]
                middle_mcp = [landmarks[mp_holistic.HandLandmark.MIDDLE_FINGER_MCP.value].x,
                              landmarks[mp_holistic.HandLandmark.MIDDLE_FINGER_MCP.value].y]
                ring_mcp = [landmarks[mp_holistic.HandLandmark.RING_FINGER_MCP.value].x,
                            landmarks[mp_holistic.HandLandmark.RING_FINGER_MCP.value].y]
                pinky_mcp = [landmarks[mp_holistic.HandLandmark.PINKY_MCP.value].x,
                             landmarks[mp_holistic.HandLandmark.PINKY_MCP.value].y]

                # Identify sign
                hand_sign, text_origin = calculate_hand_sign(wrist, thumb_tip, index_tip, middle_tip, ring_tip, pinky_tip, thumb_mcp, index_mcp, middle_mcp, ring_mcp, pinky_mcp)
                # Visualize sign
                cv2.putText(image, str(hand_sign), (int(text_origin[0]*640)+40, int(text_origin[1]*480)-40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2, cv2.LINE_AA)
            except:
                pass
            mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2))
            cv2.imshow('MediaPipe Holistic', image)


            if cv2.waitKey(5) & 0xFF == 27:
                break
    cap.release()

