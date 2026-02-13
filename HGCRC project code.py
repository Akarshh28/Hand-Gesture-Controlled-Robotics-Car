import cv2
import mediapipe as mp
import serial
import time

# ---- CHANGE THIS to your HC-05 COM port ----
PORT = "COM11"   # e.g., COM6, COM7
BAUD = 9600

try:
    # open serial
    ser = serial.Serial(PORT, BAUD, timeout=1)
    time.sleep(2)
    print("Connected to", PORT)

    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    with mp_hands.Hands(max_num_hands=1,
                        min_detection_confidence=0.6,
                        min_tracking_confidence=0.6) as hands:
        last_cmd = None
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb)

            cmd = 'S'  # default stop

            if result.multi_hand_landmarks:
                lm = result.multi_hand_landmarks[0].landmark
                tips = [8, 12, 16, 20]  # fingertips
                fingers = 0
                for t in tips:
                    if lm[t].y < lm[t-2].y:
                        fingers += 1
                if lm[4].x < lm[3].x:  # thumb
                    fingers += 1

                # map fingers → command
                if fingers == 0: cmd = 'S'  # fist = stop
                elif fingers == 1: cmd = 'F' # forward
                elif fingers == 2: cmd = 'B' # backward
                elif fingers == 3: cmd = 'L' # left
                elif fingers == 4: cmd = 'R' # right
                else: cmd = 'S'

                mp_draw.draw_landmarks(frame, result.multi_hand_landmarks[0],
                                       mp_hands.HAND_CONNECTIONS)

            # send only when command changes
            if cmd != last_cmd:
                ser.write((cmd + "\n").encode())
                ser.flush()
                time.sleep(0.05)   # avoid flooding
                print("Sent:", cmd)
                last_cmd = cmd

            cv2.putText(frame, f'Cmd: {cmd}', (10,30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            cv2.imshow("HGCRC", frame)

            if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
                break

except Exception as e:
    print("Error:", e)

finally:
    # safe exit
    try:
        cap.release()
    except:
        pass
    cv2.destroyAllWindows()
    try:
        ser.close()
    except:
        pass
    print("Resources released. COM11 closed.")