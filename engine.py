import cv2
import os
import face_recognition
import threading
from tkinter import messagebox

def showres(img):
    window_name = 'image'
    cv2.imshow(window_name,img)
    cv2.waitKey(0)
count = 0
def Frames(vidName,imgname):

    global count
    cam = cv2.VideoCapture(vidName)

    image  = face_recognition.load_image_file(imgname)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
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
    cd =0
    
    while i<=time:

        cam.set(cv2.CAP_PROP_POS_MSEC, i)
        ret, frame = cam.read()

        frameid = './data/frame'+str(i)+".jpg"
        cv2.imwrite(frameid,frame)

        unImage  = face_recognition.load_image_file(frameid)
        unImage = cv2.cvtColor(unImage,cv2.COLOR_BGR2RGB)
        try :
            unImg_encoding = face_recognition.face_encodings(unImage)[0]
        except:
            
            print("NO FACE ")
            i+=1000
            continue

        result = face_recognition.compare_faces([image_encoding], unImg_encoding,tolerance = 0.6)
        

        if True in result:
            print(result)
            frameid2 = './found_images/frame'+str(i)+".jpg"
            cv2.imwrite(frameid2,frame)
            if cd==0:
                imag = cv2.imread(frameid2)
                T2 = threading.Thread(target=lambda:showres(imag))
                T2.setDaemon=True
                T2.start()
                T2.join()
                cd+=1
            count+=1

        

        i+=1000

    messagebox.showinfo("Result","Found "+ str(count)+" Results")
    
    cam.release()
    cv2.destroyAllWindows()
