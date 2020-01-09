from PIL import Image, ImageDraw
import face_recognition
import cv2
import numpy as np
#initialise webcam
video_capture = cv2.VideoCapture(0)

process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    #resize to speed up the process
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face landmarks in the current frame of video(reduced by 0.25)
        face_landmark_list = face_recognition.face_landmarks(rgb_small_frame)

    process_this_frame = not process_this_frame
    # Create a PIL imagedraw object so we can draw on the picture
    pil_image = Image.fromarray(frame)
    d = ImageDraw.Draw(pil_image)
    # Display the results
    for face_landmarks in face_landmark_list:
        # Let's trace out each facial feature in the image and resize the thing with a line!
        for facial_feature in face_landmarks.keys():
            d.line(resized_f_landmarks := [tuple(i*4 for i in inner) for inner in face_landmarks[facial_feature]], width=2)
    #for reconstructing in a cv2 readble format and displaying the resulting image
    reframe = np.asarray(pil_image)
    cv2.imshow('Video', reframe)
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
