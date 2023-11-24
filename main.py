import os
import cv2
from cvzone.PoseModule import PoseDetector

# Inicialización de variables
selectionSpeed = 10
counterLeft = 0
counterRight = 0

# Inicialización de la cámara
cap = cv2.VideoCapture(0)
detector = PoseDetector()

# Ruta de las imágenes de las camisetas
shirtFolderPath = "assets/tshirts"
listShirts = os.listdir(shirtFolderPath)

# Calcula la relación de aspecto fija
fixedRatio = 262 / 190  # Ancho de la camiseta / Ancho de punto 11 a punto 12
shirtRatioHeightWidth = 581 / 440

# Inicializa el número de imagen para la selección de la camiseta
imageNumber = 0

# Carga de imágenes superpuestas y botones
imgButtonRight = cv2.imread("assets/icons/right_arrow.png", cv2.IMREAD_UNCHANGED)
imgButtonLeft = cv2.flip(imgButtonRight, 1)

# Redimensiona las imágenes superpuestas
overlay_width = 128
overlay_height = 128
imgButtonRight = cv2.resize(imgButtonRight, (overlay_width, overlay_height))[:, :, :3]
imgButtonLeft = cv2.resize(imgButtonLeft, (overlay_width, overlay_height))[:, :, :3]

# Tu código base y librerías importadas

# Tu código base y librerías importadas

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList, _ = detector.findPosition(img, draw=False)
    
    if lmList:
        lm11 = lmList[5][1:3]  # Hombro izquierdo
        lm12 = lmList[2][1:3]  # Hombro derecho
        
        imgShirt = cv2.imread(os.path.join(shirtFolderPath, listShirts[imageNumber]), cv2.IMREAD_UNCHANGED)
        
        # Calcula el ancho y alto de la camiseta
        widthOfShirt = int(abs(lm12[0] - lm11[0]) * 1.5)  # Modifica el factor multiplicativo según necesites
        heightOfShirt = int(widthOfShirt * shirtRatioHeightWidth)
        
        # Verifica si el tamaño de redimensionamiento es válido
        if widthOfShirt > 0 and heightOfShirt > 0:
            # Redimensiona la imagen de la camiseta
            imgShirt = cv2.resize(imgShirt, (widthOfShirt, heightOfShirt))
            
            # Resto de tu código para superponer la camiseta en la imagen, mostrar botones, interacción, etc.
        else:
            pass  # Opcional: manejo si el tamaño de redimensionamiento es inválido


    # Muestra la imagen resultante
    cv2.imshow("DressIA", img)
    
    # Condiciones de salida
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera los recursos
cap.release()
cv2.destroyAllWindows()
