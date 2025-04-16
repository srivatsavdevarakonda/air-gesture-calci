import cv2
import mediapipe as mp
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

tip_ids = [4, 8, 12, 16, 20]

cap = cv2.VideoCapture(0)

expression = ""
last_input_time = 0
input_delay = 2  # seconds
last_input_value = -1

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    fingers_up = []

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, _ = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((cx, cy))

            for i in range(1, 5):
                fingers_up.append(1 if lm_list[tip_ids[i]][1] < lm_list[tip_ids[i] - 2][1] else 0)

            # Thumb (horizontal check)
            fingers_up.insert(0, 1 if lm_list[tip_ids[0]][0] > lm_list[tip_ids[0] - 1][0] else 0)

            total = sum(fingers_up)
            current_time = time.time()

            # Only input if enough time has passed AND the input changed
            if current_time - last_input_time > input_delay and total != last_input_value:
                if total == 0:
                    try:
                        result = str(eval(expression))
                        expression = result
                    except:
                        expression = "Error"
                elif total == 1:
                    expression += "1"
                elif total == 2:
                    expression += "2"
                elif total == 3:
                    expression += "3"
                elif total == 4:
                    expression += "+"
                elif total == 5:
                    expression += "-"
                
                last_input_value = total
                last_input_time = current_time

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Show current expression
    cv2.putText(frame, f"Expr: {expression}", (10, 100), cv2.FONT_HERSHEY_SIMPLEX,
                1.5, (255, 255, 0), 3)

    cv2.imshow("Air Calculator", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()