import cv2
import mediapipe as mp
import time


class Manos:
    def __init__(self, static_image_mode=False, max_num_hands=2, model_complexity=1, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode, max_num_hands, model_complexity, min_detection_confidence, min_tracking_confidence)
        self.mpDraw = mp.solutions.drawing_utils
        self.ptime = 0
        self.ctime = 0

    def calcularFPS(self,img):
        ctime = time.time()
        fps = 1 / (ctime - self.ptime)
        self.ptime = ctime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    def draw_landmarks(self, img, result):
        for handLms in result.multi_hand_landmarks:

            for id, lm in enumerate(handLms.landmark):

                h, w, c = img.shape

                cx, cy = int(lm.x*w), int(lm.y*h)
                if id == 4:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
            self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

    def main(self):
        cap = cv2.VideoCapture(0)
        while True:
            success, img = cap.read()
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            result = self.hands.process(imgRGB)
            if result.multi_hand_landmarks:
                self.draw_landmarks(img, result)
            self.calcularFPS(img)
            cv2.imshow("Image", img)
            cv2.waitKey(1)


