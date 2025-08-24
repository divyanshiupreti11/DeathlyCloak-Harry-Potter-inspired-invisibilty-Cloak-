import cv2

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, back = cap.read()
    if not ret:
        break

    # Flip for natural selfie view
    back = cv2.flip(back, 1)

    cv2.imshow("Capture Background - Press 'q'", back)

    # Press 'q' to capture background
    if cv2.waitKey(5) == ord('q'):
        cv2.imwrite('image.jpg', back)  # save background image
        print("✅ Background image saved as 'image.jpg'")
        break

cap.release()
cv2.destroyAllWindows()
