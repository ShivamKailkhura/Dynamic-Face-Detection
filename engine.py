import cv2
import os
import face_recognition


count = 0
def Frames(vidName,imgname):

    global count
    cam = cv2.VideoCapture(vidName)

    image  = face_recognition.load_image_file(imgname)
    image_encoding = face_recognition.face_encodings(image)[0]



    try:

        if not os.path.exists("data"):
            os.makedirs("data")
        
        if not os.path.exists("found_images"):
            os.makedirs("found_images")
    
    except OSError:
        print("Error creating os directory")


    frames = cam.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cam.get(cv2.CAP_PROP_FPS)

    time = int(frames/fps)*1000

    print(time)
    i = 0

    
    while i<=time:

        cam.set(cv2.CAP_PROP_POS_MSEC, i)
        ret, frame = cam.read()

        frameid = './data/frame'+str(i)+".jpg"

        unImage = face_recognition.load_image_file(frame)
        unImg_encoding = face_recognition.face_encodings(unImage)

        result = face_recognition.compare_faces([image_encoding], unImg_encoding)

        if result:
            frameid2 = './found_images/frame'+str(i)+".jpg"
            cv2.imwrite(frameid2,frame)
            count+=1

        cv2.imwrite(frameid,frame)

        i+=1000

    
    cam.release()
