import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("ERROR: Cannot open camera. Check if camera is connected and accessible.")
else:
    print("Camera opened successfully!")
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Failed to grab frame")
            break
        
        cv2.imshow("Camera", frame)
        
        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Camera released.")
