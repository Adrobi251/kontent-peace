import cv2
import mediapipe as mp
import os

MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hand_landmarker.task")

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

latest_result = None

def result_callback(result, output_image, timestamp_ms):
    global latest_result
    latest_result = result

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=MODEL_PATH),
    running_mode=VisionRunningMode.LIVE_STREAM,
    num_hands=2,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5,
    result_callback=result_callback
)

def is_peace_sign(hand_landmarks):

    lm = hand_landmarks

    index_up = lm[8].y < lm[6].y
    middle_up = lm[12].y < lm[10].y
    ring_down = lm[16].y > lm[14].y
    pinky_down = lm[20].y > lm[18].y

    return index_up and middle_up and ring_down and pinky_down


cap = cv2.VideoCapture(0)

print("=" * 50)
print("  TREND: Peace Sign Blur! ✌️")
print("  Tunjukkan peace → layar blur")
print("  Lepaskan → layar normal")
print("  Tekan 'q' untuk keluar")
print("=" * 50)

frame_timestamp = 0

with HandLandmarker.create_from_options(options) as landmarker:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Gagal membuka webcam!")
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

        frame_timestamp += 33
        landmarker.detect_async(mp_image, frame_timestamp)

        peace_detected = False
        if latest_result and latest_result.hand_landmarks:
            for hand_lm in latest_result.hand_landmarks:
                if is_peace_sign(hand_lm):
                    peace_detected = True
                    break

        if peace_detected:
            frame = cv2.GaussianBlur(frame, (35, 35), 10)

        cv2.imshow('Peace Sign Blur - Trend', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
