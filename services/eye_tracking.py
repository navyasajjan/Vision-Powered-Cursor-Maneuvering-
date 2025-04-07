import cv2
import mediapipe as mp
import pyautogui

from utils.app_config import AppConfig



def start_eye_tracking():
    eye_tracking_active = AppConfig.eye_tracking_active
    cam = cv2.VideoCapture(0)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    screen_w, screen_h = pyautogui.size()

    while eye_tracking_active:
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        if landmark_points:

            landmarks = landmark_points[0].landmark
            for id, landmark in enumerate(landmarks[474:478]):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 0))
                if id == 1:
                    screen_x = screen_w * landmark.x
                    screen_y = screen_h * landmark.y
                    pyautogui.moveTo(screen_x, screen_y)
            left = [landmarks[145], landmarks[159]]
            right = [landmarks[374], landmarks[386]]
            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255))
            for landmark in right:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (255, 0, 255))
            left_eye_aspect_ratio = left[0].y - left[1].y
            right_eye_aspect_ratio = right[0].y - right[1].y

            if left_eye_aspect_ratio < 0.008 and right_eye_aspect_ratio < 0.008:
                pyautogui.doubleClick()
                print("double clicked")

            else:
                if left_eye_aspect_ratio < 0.008:
                    print("left clicked")
                    pyautogui.click(button='left')
            
                elif right_eye_aspect_ratio < 0.008:
                    print("right clicked")
                    pyautogui.click(button='right')
        # elif not landmark_points:
              # This block handles when person moves out of the screen.            
        #     cam.release()
        #     break
                    
        if (not AppConfig.eye_tracking_active):
            break
        cv2.imshow('Eye Controlled Mouse', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
            break

    cam.release()
    cv2.destroyAllWindows()


# start_eye_tracking()  # Start eye tracking