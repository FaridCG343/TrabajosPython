import Hand
import cv2
import time
h = Hand
xd = h.Manos()
cap = cv2.VideoCapture(0)
ptime = 0
ctime = 0
while True:
    success, img = cap.read()
    xd.findHands(img)
    xd.getPos(img)
    #region Calcular dedos
    cant = []
    print(xd.cantMan())
    for a in range(0, xd.cantMan()):
        lmp = xd.getPos(img, a, False)
        if lmp[4][1] < lmp[20][1]:
            if lmp[4][1] < lmp[3][1]:
                cant.append(1)
        else:
            if lmp[4][1] > lmp[3][1]:
                cant.append(1)
        for x in range(8, 21, 4):
            if lmp[x][2] < lmp[x-1][2]:
                cant.append(1)
    nCant = len(cant)
    cv2.rectangle(img, (0, 0), (120, 120), (174, 242, 101), cv2.FILLED)
    cv2.putText(img, str(nCant), (25, 80), cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 0))
    #endregion
    #region fps
    # ctime = time.time()
    # fps = 1/(ctime-ptime)
    # ptime = ctime
    # cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    #endregion
    cv2.imshow("Image", img)
    cv2.waitKey(1)
