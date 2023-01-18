import cv2
import imutils
import numpy as np
import pytesseract
import tkinter.filedialog
from tkinter import Tk
tkinter.Tk().withdraw()
filename=tkinter.filedialog.askopenfilename()
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img=cv2.imread(filename)#baga intre'' locatia pozei cu masina de inmatriculare
#img=cv2.resize(img,(500,300))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray scale image',gray )
gray=cv2.bilateralFilter(gray,25,25,25)
#cv2.imshow('Imagine filtrata',gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
edged=cv2.Canny(gray,30,200)
#cv2.imshow('Canny',edged)
contur=cv2.findContours(edged.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)#DETECTARE CONTUR
contur=imutils.grab_contours(contur)
contur=sorted(contur,key=cv2.contourArea,reverse=True)[:10]
screenCnt=None
for c in contur:
    peri=cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,0.018* peri,True)
    if(len(approx)==4):
        screenCnt =approx
        break
    if screenCnt is None :
        detected=0
        print("nu am gasit nici un contur")
    else:
        detected=1
mask=np.zeros(gray.shape,np.uint8)
new_image=cv2.drawContours(mask,[screenCnt],0,255,-1)
new_image=cv2.bitwise_and(img,img,mask=mask)
(x,y)=np.where(mask==255)
(topx,topy)=(np.min(x),np.min(y))
(bottomx,bottomy)=(np.max(x),np.max(y))
Crop=gray[topx:bottomx+1,topy:bottomy+1]
#Stefan Banu
Crop = cv2.add(Crop,np.array([-50.0]) , Crop)
Crop = cv2.multiply(Crop,np.array([1.25]),Crop)
text_numar=pytesseract.image_to_string(Crop,config='--psm 10')
print("Numarul de inmatriculare detectat este",text_numar)
img=cv2.resize(img,(500,300))
Crop=cv2.resize(Crop,(400,200))
cv2.imshow('Crop',Crop)
cv2.waitKey(0)
cv2.destroyAllWindows()  