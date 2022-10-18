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
    lmp = xd.getPos(img)
    try:
        lmp2 = xd.getPos(img, 1, False)
    except:
        lmp2 = []
    cant = []
    if len(lmp) > 0:
        if lmp[4][1] < lmp[20][1]:
            if lmp[4][1] < lmp[3][1]:
                cant.append(1)
        else:
            if lmp[4][1] > lmp[3][1]:
                cant.append(1)
        for x in range(8, 21, 4):
            if lmp[x][2] < lmp[x-1][2]:
                cant.append(1)
    if len(lmp2) > 0:
        if lmp2[4][1] < lmp2[20][1]:
            if lmp2[4][1] < lmp2[3][1]:
                cant.append(1)
        else:
            if lmp2[4][1] > lmp2[3][1]:
                cant.append(1)
        for x in range(8, 21, 4):
            if lmp2[x][2] < lmp2[x-1][2]:
                cant.append(1)
    nCant = len(cant)
    cv2.rectangle(img, (0,0), (120,120), (174, 242, 101), cv2.FILLED)
    cv2.putText(img, str(nCant), (25, 80), cv2.FONT_HERSHEY_PLAIN , 5, (0, 0, 0))
    #region fps
    # ctime = time.time()
    # fps = 1/(ctime-ptime)
    # ptime = ctime
    # cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    #endregion
    cv2.waitKey(1)
