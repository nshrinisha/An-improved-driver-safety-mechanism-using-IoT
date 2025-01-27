from modules.alcohol_detection import detect_alcohol
from modules.drowsiness_detection import detect_drowsiness
from modules.sign_detection import detect_signs
from modules.light_control import control_lights
import cv2

# Initialize the system
print("Starting Driver Safety System")

# Capture video feed
cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture video frame")
            break

        # Alcohol detection (Placeholder function call)
        alcohol_status = detect_alcohol()
        if alcohol_status:
            print("Alcohol detected! Ignition locked.")

        # Drowsiness detection
        drowsiness_status = detect_drowsiness(frame)
        if drowsiness_status:
            print("Driver is drowsy! Alert triggered.")

        # Traffic sign detection
        detected_sign = detect_signs(frame)
        if detected_sign:
            print(f"Detected sign: {detected_sign}")

        # Light control
        control_lights(frame)

        # Display the frame
        cv2.imshow("Driver Safety System", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
    print("System shut down.")