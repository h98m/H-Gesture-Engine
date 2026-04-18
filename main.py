import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import math
import time

class KalmanFilter:
    def __init__(self):
        self.prev_state = None
        self.process_noise = 0.05
        self.measurement_noise = 0.8
        self.error_est = 1.0
    def update(self, measurement):
        if self.prev_state is None:
            self.prev_state = measurement
            return measurement
        gain = self.error_est / (self.error_est + self.measurement_noise)
        curr = self.prev_state + gain * (measurement - self.prev_state)
        self.error_est = (1.0 - gain) * self.error_est + self.process_noise
        self.prev_state = curr
        return curr

cap = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands(max_num_hands=1, model_complexity=0, min_detection_confidence=0.8)
kf_x, kf_y = KalmanFilter(), KalmanFilter()
sw, sh = pyautogui.size()
pyautogui.PAUSE = 0

current_state = "IDLE"
state_counter = 0
CONFIRM_FRAMES = 3 
is_dragging = False
prev_y_scroll = 0
prev_x_vol = 0

while True:
    success, frame = cap.read()
    if not success: break
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.multi_hand_landmarks:
        lms = results.multi_hand_landmarks[0].landmark
        
        f_up = [lms[8].y < lms[6].y, lms[12].y < lms[10].y, lms[16].y < lms[14].y, lms[20].y < lms[18].y]
        
        new_state = "IDLE"
        if f_up[0] and f_up[1] and f_up[2]: new_state = "VOLUME"
        elif f_up[0] and f_up[1]: new_state = "SCROLL"
        elif f_up[0]: new_state = "MOUSE"

        if new_state == current_state:
            state_counter += 1
        else:
            current_state = new_state
            state_counter = 0

        if state_counter >= CONFIRM_FRAMES:
            if current_state == "VOLUME":
                if is_dragging: 
                    pyautogui.mouseUp()
                    is_dragging = False
                
                curr_x_vol = lms[8].x * w
                if prev_x_vol != 0:
                    diff = curr_x_vol - prev_x_vol
                    if diff > 15: pyautogui.press("volumeup")
                    elif diff < -15: pyautogui.press("volumedown")
                prev_x_vol = curr_x_vol
                cv2.putText(frame, "STATE: VOLUME", (50, 50), 2, 1, (0, 255, 255), 2)

            elif current_state == "SCROLL":
                curr_y = lms[8].y * h
                if prev_y_scroll != 0:
                    diff = prev_y_scroll - curr_y
                    if abs(diff) > 10: pyautogui.scroll(int(diff * 15))
                prev_y_scroll = curr_y
                
                dist_r = math.hypot(lms[8].x - lms[12].x, lms[8].y - lms[12].y)
                if dist_r < 0.035: 
                    pyautogui.rightClick()
                    time.sleep(0.4)
                
                cv2.putText(frame, "STATE: SCROLL", (50, 50), 2, 1, (255, 0, 255), 2)

            elif current_state == "MOUSE":
                tx = np.interp(lms[8].x * w, (100, w-100), (0, sw))
                ty = np.interp(lms[8].y * h, (100, h-100), (0, sh))
                pyautogui.moveTo(kf_x.update(tx), kf_y.update(ty))
                
                dist_l = math.hypot(lms[8].x - lms[4].x, lms[8].y - lms[4].y)
                
                if dist_l < 0.045:
                    if not is_dragging:
                        pyautogui.mouseDown()
                        is_dragging = True
                        cv2.circle(frame, (int(lms[8].x*w), int(lms[8].y*h)), 15, (0,0,255), -1)
                else:
                    if is_dragging:
                        pyautogui.mouseUp()
                        is_dragging = False
                
                prev_y_scroll = 0
                prev_x_vol = 0
                cv2.putText(frame, "STATE: MOUSE", (50, 50), 2, 1, (0, 255, 0), 2)

    cv2.imshow('Hussein Stable AI', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
