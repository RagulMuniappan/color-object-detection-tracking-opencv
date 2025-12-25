import cv2
import numpy as np

# Dummy function for trackbar
def nothing(x):
    pass

# Open camera
cap = cv2.VideoCapture(0)

# Create windows
cv2.namedWindow("Trackbars")
cv2.namedWindow("Mask")

# Create trackbars
cv2.createTrackbar("H Low", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("H High", "Trackbars", 179, 179, nothing)

cv2.createTrackbar("S Low", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("S High", "Trackbars", 255, 255, nothing)

cv2.createTrackbar("V Low", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("V High", "Trackbars", 255, 255, nothing)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (550, 370)) #purpose - See original image & lighting

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #purpose - See what color is being detected

    # Get trackbar positions
    h_low = cv2.getTrackbarPos("H Low", "Trackbars")
    h_high = cv2.getTrackbarPos("H High", "Trackbars")

    s_low = cv2.getTrackbarPos("S Low", "Trackbars")
    s_high = cv2.getTrackbarPos("S High", "Trackbars")

    v_low = cv2.getTrackbarPos("V Low", "Trackbars")
    v_high = cv2.getTrackbarPos("V High", "Trackbars")

    lower = np.array([h_low, s_low, v_low])
    upper = np.array([h_high, s_high, v_high])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Show values on screen
    cv2.putText(
        result,
        f"Lower: {lower} Upper: {upper}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 0, 0),
        2
    )

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", result)

    if cv2.waitKey(1) & 0xFF == 27:
        print("Final HSV Values:")
        print("Lower =", lower)
        print("Upper =", upper)
        break

cap.release()
cv2.destroyAllWindows()