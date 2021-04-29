from pyzbar import pyzbar
from datetime import datetime
import argparse
import cv2
import sys
import time


#test0
start2 = 0


#vc0 = cv2.VideoCapture(0)
vc = cv2.VideoCapture(2) # 0은 노트북 웹캠 2는 usb로 연결된 웹캠


vc.set(3, 1920)
vc.set(4, 1024)
vc.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))



while True :
    #time.sleep(0.1)
    print("waiting...")
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    if True:

        print("webcam start!")
        start = time.time()
        chk = 0         
        vc.set(10,0.5)


        while time.time() - start <= 300 :

            #ret0, frame0 = vc0.read()
            #cv2.imshow("Video Window0", frame0)  
            
            ret, frame = vc.read()
            cv2.imshow("Video Window", frame)   
            cv2.imwrite('image.jpg',frame)     

            image = cv2.imread('image.jpg')
            barcodes = pyzbar.decode(image)

            if barcodes:
                  for barcode in barcodes:
                     (x,y,w,h) = barcode.rect
                     cv2.rectangle(image, (x,y) , (x+w , y + h), (0,0,255) ,2)

                     barcodeData = barcode.data.decode("utf-8")
                     barcodeType = barcode.type

                     text = "{} ({})".format(barcodeData, barcodeType)
                     cv2.putText(image, text, (x,y - 10) , cv2.FONT_HERSHEY_SIMPLEX,0.5 , (0,0,255),2)

                     print("[INFO' Found {} barcode:{}".format(barcodeType, barcodeData))

                     cv2.imshow("image", image)
                     #cv2.waitKey(0)

                     chk = 1
				
				
                    
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            
        vc.release()
        cv2.destroyAllWindows()

        if chk == 1:
            print("access success")

        else:
            print("access failed")


      

     
      
