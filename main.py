import mediapipe as mp
import cv2
import numpy as np
from mediapipe.framework.formats import landmark_pb2
import time
from math import sqrt
import win32api
import pyautogui
from pynput.mouse import Button, Controller  # Contains Mouse Operations

mouse = Controller()
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
click = 0
double_click = 0

video = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while video.isOpened():
        _, frame = video.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        image = cv2.flip(image, 1)

        imageHeight, imageWidth, _ = image.shape

        results = hands.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                          )
        if results.multi_hand_landmarks != None:
            for handLandmarks in results.multi_hand_landmarks:
                for point in mp_hands.HandLandmark:

                    normalizedLandmark = handLandmarks.landmark[point]
                    pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                           normalizedLandmark.y,
                                                                                           imageWidth, imageHeight)

                    point = str(point)

                    # Set Cursor For Index Finger Tip
                    if point == 'HandLandmark.INDEX_FINGER_TIP':
                        try:
                            indexfingertip_x = pixelCoordinatesLandmark[0]
                            indexfingertip_y = pixelCoordinatesLandmark[1]
                            win32api.SetCursorPos((indexfingertip_x * 4, indexfingertip_y * 5))

                        except:
                            pass

                        # For Wrist
                    elif point == 'HandLandmark.WRIST':
                        try:
                            pinkyfingertip_x = pixelCoordinatesLandmark[0]
                            pinkyfingertip_y = pixelCoordinatesLandmark[1]
                        except:
                            pass

                        # For Thumb
                    elif point == 'HandLandmark.THUMB_TIP':
                        try:
                            thumbfingertip_x = pixelCoordinatesLandmark[0]
                            thumbfingertip_y = pixelCoordinatesLandmark[1]
                            # print('thumb',thumfingercmc_x)
                        except:
                            pass

                    elif point == 'HandLandmark.THUMB_CMC':
                        try:
                            thumbfingercmc_x = pixelCoordinatesLandmark[0]
                            thumbfingercmc_y = pixelCoordinatesLandmark[1]
                            # print('thumb',thumfingercmc_x)
                        except:
                            pass

                    elif point == 'HandLandmark.THUMB_MCP':
                        try:
                            thumbfingermcp_x = pixelCoordinatesLandmark[0]
                            thumbfingermcp_y = pixelCoordinatesLandmark[1]
                            # print('thumb',thumfingermcp_x)
                        except:
                            pass

                    elif point == 'HandLandmark.THUMB_IP':
                        try:
                            thumbfingerip_x = pixelCoordinatesLandmark[0]
                            thumbfingerip_y = pixelCoordinatesLandmark[1]
                            # print('thumb',thumfingerip_x)
                        except:
                            pass

                        # For Index Finger
                    elif point == 'HandLandmark.INDEX_FINGER_MCP':
                        try:
                            indexfingermcp_x = pixelCoordinatesLandmark[0]
                            indexfingermcp_y = pixelCoordinatesLandmark[1]

                        except:
                            pass

                    elif point == 'HandLandmark.INDEX_FINGER_PIP':
                        try:
                            indexfingerpip_x = pixelCoordinatesLandmark[0]
                            indexfingerpip_y = pixelCoordinatesLandmark[1]

                        except:
                            pass

                    elif point == 'HandLandmark.INDEX_FINGER_DIP':
                        try:
                            indexfingerdip_x = pixelCoordinatesLandmark[0]
                            indexfingerdip_y = pixelCoordinatesLandmark[1]

                        except:
                            pass

                        # For Middle Finger
                    elif point == 'HandLandmark.MIDDLE_FINGER_MCP':
                        try:
                            middlefingermcp_x = pixelCoordinatesLandmark[0]
                            middlefingermcp_y = pixelCoordinatesLandmark[1]
                        except:
                            pass

                    elif point == 'HandLandmark.MIDDLE_FINGER_PIP':
                        try:
                            middlefingerpip_x = pixelCoordinatesLandmark[0]
                            middlefingerpip_y = pixelCoordinatesLandmark[1]
                        except:
                            pass

                    elif point == 'HandLandmark.MIDDLE_FINGER_DIP':
                        try:
                            middlefingerdip_x = pixelCoordinatesLandmark[0]
                            middlefingerdip_y = pixelCoordinatesLandmark[1]
                        except:
                            pass

                    elif point == 'HandLandmark.MIDDLE_FINGER_TIP':
                        try:
                            middlefingertip_x = pixelCoordinatesLandmark[0]
                            middlefingertip_y = pixelCoordinatesLandmark[1]

                        except:
                            pass

                        # For Ring Finger
                    elif point == 'HandLandmark.RING_FINGER_MCP':
                        try:
                            ringfingermcp_x = pixelCoordinatesLandmark[0]
                            ringfingermcp_y = pixelCoordinatesLandmark[1]

                        except:
                            pass

                    elif point == 'HandLandmark.RING_FINGER_PIP':
                        try:
                            ringfingerpip_x = pixelCoordinatesLandmark[0]
                            ringfingerpip_y = pixelCoordinatesLandmark[1]

                        except:
                            pass

                    elif point == 'HandLandmark.RING_FINGER_DIP':
                        try:
                            ringfingerdip_x = pixelCoordinatesLandmark[0]
                            ringfingerdip_y = pixelCoordinatesLandmark[1]

                        except:
                            pass

                    elif point == 'HandLandmark.RING_FINGER_TIP':
                        try:
                            ringfingertip_x = pixelCoordinatesLandmark[0]
                            ringfingertip_y = pixelCoordinatesLandmark[1]

                        except:
                            pass

                        # For Pinky Finger
                    elif point == 'HandLandmark.PINKY_MCP':
                        try:
                            pinkyfingermcp_x = pixelCoordinatesLandmark[0]
                            pinkyfingermcp_y = pixelCoordinatesLandmark[1]

                        except:
                            pass

                    elif point == 'HandLandmark.PINKY_PIP':
                        try:
                            pinkyfingerpip_x = pixelCoordinatesLandmark[0]
                            pinkyfingerpip_y = pixelCoordinatesLandmark[1]

                        except:
                            pass

                    elif point == 'HandLandmark.PINKY_DIP':
                        try:
                            pinkyfingerdip_x = pixelCoordinatesLandmark[0]
                            pinkyfingerdip_y = pixelCoordinatesLandmark[1]

                        except:
                            pass

                    elif point == 'HandLandmark.PINKY_TIP':
                        try:
                            pinkyfingertip_x = pixelCoordinatesLandmark[0]
                            pinkyfingertip_y = pixelCoordinatesLandmark[1]

                        except:
                            pass

                        # To Click
                        try:
                            # pyautogui.moveTo(indexfingertip_x,indexfingertip_y)
                            Distance_x1 = sqrt(
                                (indexfingertip_x - thumbfingertip_x) ** 2 + (indexfingertip_x - thumbfingertip_x) ** 2)
                            Distance_y1 = sqrt(
                                (indexfingertip_y - thumbfingertip_y) ** 2 + (indexfingertip_y - thumbfingertip_y) ** 2)
                            if Distance_x1 < 5 or Distance_x1 < -5:
                                if Distance_y1 < 5 or Distance_y1 < -5:
                                    click = click + 1
                                    if click % 5 == 0:
                                        print("Click")
                                        pyautogui.click()

                            # To Double Click
                            Distance_x2 = sqrt(
                                (indexfingermcp_x - thumbfingertip_x) ** 2 + (
                                        indexfingermcp_x - thumbfingertip_x) ** 2)
                            Distance_y2 = sqrt(
                                (indexfingermcp_y - thumbfingertip_y) ** 2 + (
                                        indexfingermcp_y - thumbfingertip_y) ** 2)
                            if Distance_x2 < 5 or Distance_x2 < -5:
                                if Distance_y2 < 5 or Distance_y2 < -5:
                                    double_click = double_click + 1
                                    if double_click % 5 == 0:
                                        print("Double Click")
                                        pyautogui.doubleClick()

                            # To Scroll-Up
                            Distance_x3 = sqrt(
                                (indexfingertip_x - middlefingertip_x) ** 2 + (
                                        indexfingertip_x - middlefingertip_x) ** 2)
                            Distance_y3 = sqrt(
                                (indexfingertip_y - middlefingertip_y) ** 2 + (
                                        indexfingertip_y - middlefingertip_y) ** 2)
                            if Distance_x3 == 0 or Distance_x3 < 10:
                                if Distance_y3 == 0 or Distance_y3 < 10:
                                    print("Scroll-Up")
                                    pyautogui.scroll(30)

                            # To Scroll-Down
                            Distance_x4 = sqrt(
                                (thumbfingertip_x - ringfingermcp_x) ** 2 + (
                                    thumbfingertip_x - ringfingermcp_x) ** 2)
                            Distance_y4 = sqrt(
                                (thumbfingertip_y - ringfingermcp_y) ** 2 + (
                                    thumbfingertip_y - ringfingermcp_y) ** 2)
                            if Distance_x4 == 0 or Distance_x4 < 10:
                                if Distance_y4 == 0 or Distance_y4 < 10:
                                    print("Scroll-Down")
                                    pyautogui.scroll(-30)

                            '''
                            # To Horizontal-Scroll
                            Distance_x5 = sqrt(
                                (thumbfingertip_x - indexfingertip_x) ** 2 + (
                                    thumbfingertip_x - indexfingertip_x) ** 2)
                            Distance_y5 = sqrt(
                                (thumbfingertip_y - indexfingertip_y) ** 2 + (
                                    thumbfingertip_y - indexfingertip_y) ** 2)
                            if 10 < Distance_x5 < 100:
                                if 10 < Distance_y5 < 100:
                                    print("Horizontal-Scroll")
                                    pyautogui.()
                            '''
                        except:
                            pass

            cv2.imshow('Hand Tracking', image)
            #print("Distance of x5= ", Distance_x5)
            #print("Distance of y5= ", Distance_y5)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

video.release()
cv2.destroyAllWindows()
