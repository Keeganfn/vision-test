import cv2

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, image = cap.read()

    # Convert BGR to HSV
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blur = cv2.medianBlur(image, 9)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 100, 200, cv2.THRESH_BINARY)[1]

    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

#    min_area = 100
#    for c in cnts:
#        area = cv2.contourArea(c)
#        if area > min_area:
    #cv2.drawContours(image, [c], 0, (36, 255, 12), 2)

    c = max(cnts, key=cv2.contourArea)
    if cv2.contourArea(c):
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(image, (x-20, y), (x+w + 30, y+h + 70), (0, 255, 0), 2)

    cv2.imshow('thresh', thresh)
    cv2.imshow('image', image)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
