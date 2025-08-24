import cv2
import numpy as np

# Open webcam
cap = cv2.VideoCapture(0)

# Load the saved background (captured from background.py)
back = cv2.imread('image.jpg')

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Flip the frame for natural selfie view
    frame = cv2.flip(frame, 1)

    # Convert frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define red color range (cloak color)
    l_red = np.array([0, 120, 70])
    u_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, l_red, u_red)

    l_red2 = np.array([170, 120, 70])
    u_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, l_red2, u_red2)

    # Combine both masks
    mask = mask1 + mask2

    # Clean the mask - remove noise and smooth edges
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

    # Part 1: cloak area replaced with background
    part1 = cv2.bitwise_and(back, back, mask=mask)

    # Part 2: rest of the frame
    mask_inv = cv2.bitwise_not(mask)
    part2 = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Final output
    cloak = cv2.addWeighted(part1, 1, part2, 1, 0)

    cv2.imshow("Invisibility Cloak", cloak)

    # Press 'q' to quit
    if cv2.waitKey(5) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
