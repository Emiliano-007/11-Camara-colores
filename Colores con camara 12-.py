#Hecho por Emiliano Villanueva Barrera
import cv2
import numpy as np
 
#Iniciamos la camara
#Depewnde de la cmarra que tengas instalada
captura = cv2.VideoCapture(0)
 
while(1):
     
    #Capturamos una imagen y la convertimos de RGB -> HSV
    _, imagen = captura.read()
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
 
    #Establecemos el rango de colores que vamos a detectar
    verde_bajos = np.array([49,50,50], dtype=np.uint8)
    verde_altos = np.array([80, 255, 255], dtype=np.uint8)
    
    amarillo_bajos = np.array([0,0,85], dtype=np.uint8)
    amarillo_altos = np.array([35, 255, 255], dtype=np.uint8)
    
    azul_bajos = np.array([100,51,0], dtype=np.uint8)
    azul_altos = np.array([255, 200, 145], dtype=np.uint8)
    
    rojo_bajos = np.array([0,0,100], dtype=np.uint8)
    rojo_altos = np.array([119, 119, 255], dtype=np.uint8)
 
    #Crear una mascara con solo los pixeles dentro del rango de verdes
    maskv = cv2.inRange(hsv, verde_bajos, verde_altos)
    maskm = cv2.inRange(hsv, amarillo_bajos, amarillo_altos)
    maska = cv2.inRange(hsv, azul_bajos, azul_altos)
    maskr = cv2.inRange(hsv, rojo_bajos, rojo_altos)
    
    union1=cv2.bitwise_or(maskv,maskm)
    union2=cv2.bitwise_or(maska,maskr)
    
    unionf=cv2.bitwise_or(union1,union2)
 
    #Encontrar el area de los objetos que detecta la camara
    moments = cv2.moments(unionf)
    area = moments['m00']
 
    #Descomentar para ver el area por pantalla
    #print area
    if(area > 2000000):
         
        #Buscamos el centro x, y del objeto
        x = int(moments['m10']/moments['m00'])
        y = int(moments['m01']/moments['m00'])
         
        #Mostramos sus coordenadas por pantalla
        print ("x = ", x)
        print ("y = ", y)
 
        #Dibujamos una marca en el centro del objeto
        cv2.rectangle(imagen, (x, y), (x+2, y+2),(0,255,0), 2)
     
     
    #Mostramos la imagen original con la marca del centro y
    #la mascara
    cv2.imshow('Camara colores verde, amarillo, azul, rojo', unionf)
    cv2.imshow('Camara original', imagen)
    
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
    
cv2.destroyAllWindows()
#Hecho por Emiliano Villanueva Barrera