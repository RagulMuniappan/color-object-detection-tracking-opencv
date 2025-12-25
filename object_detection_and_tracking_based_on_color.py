import cv2
import imutils #to resize and framing

# HSV color range (adjust as needed)
redLower = (69, 21, 0)
redUpper = (100, 255, 255)

# Camera initialization
camera = cv2.VideoCapture(0)   # cam id

while True:
    grabbed, frame = camera.read()
    if not grabbed:
        break

    frame = imutils.resize(frame, width=500) # Resize frame

    blurred = cv2.GaussianBlur(frame, (11, 11), 0) # Blur to reduce noise

    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV) # Convert to HSV

    mask = cv2.inRange(hsv, redLower, redUpper) # Mask based on HSV range
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find contours
    cnts = cv2.findContours(
        mask.copy(),
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )[-2]

    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea) # Get largest contour

        ((x, y), radius) = cv2.minEnclosingCircle(c) # Minimum enclosing circle

        M = cv2.moments(c) # Moments for center
        if M["m00"] != 0:
            center = (
                int(M["m10"] / M["m00"]),
                int(M["m01"] / M["m00"])
            )

        if radius > 10:
            # Draw circle and center
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

            print(center, radius)

            # Decision logic
            if radius > 250:
                print("Stop")
            else:
                if center[0] < 150:
                    print("Right")
                elif center[0] > 450:
                    print("Left")
                elif radius < 250:
                    print("Front")
                else:
                    print("Stop")

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

camera.release()
cv2.destroyAllWindows()