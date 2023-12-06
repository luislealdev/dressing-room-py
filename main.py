# import os
# import cv2 
# from cvzone.PoseModule import PoseDetector

# # Inicialización de variables
# selectionSpeed = 10
# counterLeft = 0
# counterRight = 0

# # Inicialización de la cámara
# cap = cv2.VideoCapture(0)
# detector = PoseDetector()

# # Ruta de las imágenes de las camisetas
# shirtFolderPath = "assets/tshirts"
# listShirts = os.listdir(shirtFolderPath)

# # Calcula la relación de aspecto fija
# fixedRatio = 262 / 190  # Ancho de la camiseta / Ancho de punto 11 a punto 12
# shirtRatioHeightWidth = 581 / 440

# # Inicializa el número de imagen para la selección de la camiseta
# imageNumber = 0

# # Carga de imágenes superpuestas y botones
# imgButtonRight = cv2.imread("assets/icons/right_arrow.png", cv2.IMREAD_UNCHANGED)
# imgButtonLeft = cv2.flip(imgButtonRight, 1)

# # Redimensiona las imágenes superpuestas
# overlay_width = 128
# overlay_height = 128
# imgButtonRight = cv2.resize(imgButtonRight, (overlay_width, overlay_height))[:, :, :3]
# imgButtonLeft = cv2.resize(imgButtonLeft, (overlay_width, overlay_height))[:, :, :3]

# # Tu código base y librerías importadas

# # Tu código base y librerías importadas

# while True:
#     success, img = cap.read()
#     img = detector.findPose(img)
#     lmList, _ = detector.findPosition(img, draw=False)
    
#     if lmList:
#         lm11 = lmList[5][1:3]  # Hombro izquierdo
#         lm12 = lmList[2][1:3]  # Hombro derecho
        
#         imgShirt = cv2.imread(os.path.join(shirtFolderPath, listShirts[imageNumber]), cv2.IMREAD_UNCHANGED)
        
#         # Calcula el ancho y alto de la camiseta
#         widthOfShirt = int(abs(lm12[0] - lm11[0]) * 1.5)  # Modifica el factor multiplicativo según necesites
#         heightOfShirt = int(widthOfShirt * shirtRatioHeightWidth)
        
#         # Verifica si el tamaño de redimensionamiento es válido
#         if widthOfShirt > 0 and heightOfShirt > 0:
#             # Redimensiona la imagen de la camiseta
#             imgShirt = cv2.resize(imgShirt, (widthOfShirt, heightOfShirt))
            
#             # Resto de tu código para superponer la camiseta en la imagen, mostrar botones, interacción, etc.
#         else:
#             pass  # Opcional: manejo si el tamaño de redimensionamiento es inválido


#     # Muestra la imagen resultante
#     cv2.imshow("DressIA", img)
    
#     # Condiciones de salida
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Libera los recursos
# cap.release()
# cv2.destroyAllWindows()



# import os
# import cv2
# from cvzone.PoseModule import PoseDetector

# # Inicialización de variables
# counterLeft = 0
# counterRight = 0

# # Inicialización de la cámara
# cap = cv2.VideoCapture(0)
# detector = PoseDetector()

# # Ruta de las imágenes de las camisetas
# shirtFolderPath = "assets/tshirts"
# listShirts = os.listdir(shirtFolderPath)

# # Calcula la relación de aspecto fija
# shirtRatioHeightWidth = 581 / 440

# # Inicializa el número de imagen para la selección de la camiseta
# imageNumber = 0

# # Carga de imágenes superpuestas y botones
# imgButtonRight = cv2.imread("assets/icons/right_arrow.png", cv2.IMREAD_UNCHANGED)
# imgButtonLeft = cv2.flip(imgButtonRight, 1)

# while True:
#     success, img = cap.read()
#     if not success:
#         print("Error al leer de la cámara.")
#         break

#     img = detector.findPose(img)
#     lmList, _ = detector.findPosition(img, draw=False)

#     if lmList:
#         lm11 = lmList[11][1:3]  # Hombro izquierdo
#         lm12 = lmList[12][1:3]  # Hombro derecho

#         center = ((lm11[0] + lm12[0]) // 2, (lm11[1] + lm12[1]) // 2)
#         widthOfShirt = int(abs(lm12[0] - lm11[0]) * 1.5)
#         heightOfShirt = int(widthOfShirt * shirtRatioHeightWidth)

#         if widthOfShirt > 0 and heightOfShirt > 0:
#             imgShirt = cv2.imread(os.path.join(shirtFolderPath, listShirts[imageNumber]), cv2.IMREAD_UNCHANGED)
#             imgShirt = cv2.resize(imgShirt, (widthOfShirt, heightOfShirt))

#             # Separa el canal alfa
#             shirtAlpha = imgShirt[:, :, 3]
#             imgShirt = imgShirt[:, :, :3]

#             # Calcula las coordenadas de superposición
#             top_left_x = center[0] - widthOfShirt // 2
#             top_left_y = center[1] - heightOfShirt // 2

#             # Área de la imagen donde se superpondrá la camiseta
#             roi = img[top_left_y:top_left_y + heightOfShirt, top_left_x:top_left_x + widthOfShirt]

#             # Superponer usando el canal alfa para la transparencia
#             img1_bg = cv2.bitwise_and(roi.copy(), roi.copy(), mask=cv2.bitwise_not(shirtAlpha))
#             img2_fg = cv2.bitwise_and(imgShirt, imgShirt, mask=shirtAlpha)

#             img[top_left_y:top_left_y + heightOfShirt, top_left_x:top_left_x + widthOfShirt] = cv2.add(img1_bg, img2_fg)

#     cv2.imshow("DressIA", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()





# import os
# import cv2
# import numpy as np
# from cvzone.PoseModule import PoseDetector

# # Inicialización de variables
# counterLeft = 0
# counterRight = 0

# # Inicialización de la cámara
# cap = cv2.VideoCapture(0)
# detector = PoseDetector()

# # Ruta de las imágenes de las camisetas
# shirtFolderPath = "assets/tshirts"
# listShirts = os.listdir(shirtFolderPath)
# shirtRatioHeightWidth = 581 / 440  # Relación de aspecto de la camiseta

# # Inicializa el número de imagen para la selección de la camiseta
# imageNumber = 0

# # Carga de imágenes superpuestas y botones
# imgButtonRight = cv2.imread("assets/icons/right_arrow.png", cv2.IMREAD_UNCHANGED)
# imgButtonLeft = cv2.flip(imgButtonRight, 1)

# while True:
#     success, img = cap.read()
#     if not success:
#         print("Error al leer de la cámara.")
#         break

#     img = detector.findPose(img)
#     lmList, _ = detector.findPosition(img, draw=False)

#     if lmList:
#         # Puntos de referencia para el hombro izquierdo y derecho
#         shoulderLeft = lmList[5][1:3]  # Hombro izquierdo
#         shoulderRight = lmList[2][1:3]  # Hombro derecho

#         # Calcular el ancho y alto del torso basado en los puntos de referencia
#         torsoWidth = np.linalg.norm(np.array(shoulderLeft) - np.array(shoulderRight))
#         torsoHeight = torsoWidth * shirtRatioHeightWidth

#         # Dimensiones de la camiseta ajustadas
#         shirtWidth = int(torsoWidth)
#         shirtHeight = int(torsoHeight)

#         # Coordenadas para colocar la camiseta
#         top_left_x = int((shoulderLeft[0] + shoulderRight[0]) / 2 - shirtWidth / 2)
#         top_left_y = int((shoulderLeft[1] + shoulderRight[1]) / 2 - shirtHeight / 2)

#         # Cargar la imagen de la camiseta
#         imgShirtPath = os.path.join(shirtFolderPath, listShirts[imageNumber])
#         imgShirt = cv2.imread(imgShirtPath, cv2.IMREAD_UNCHANGED)
#         if imgShirt is None:
#             print(f"No se pudo cargar la imagen: {imgShirtPath}")
#             continue

#         # Asegurarse de que la región a superponer esté dentro de los límites de la imagen
#         rows, cols, _ = img.shape
#         top_left_x = max(0, top_left_x)
#         top_left_y = max(0, top_left_y)
#         bottom_right_x = min(cols, top_left_x + shirtWidth)
#         bottom_right_y = min(rows, top_left_y + shirtHeight)

#         # Redimensionar la imagen de la camiseta para que coincida con la región de interés (ROI)
#         imgShirt = cv2.resize(imgShirt, (bottom_right_x - top_left_x, bottom_right_y - top_left_y))
#         shirtRGB = imgShirt[:, :, :3]
#         shirtAlpha = imgShirt[:, :, 3]

#         # Crear la máscara para la superposición
#         mask = cv2.merge([shirtAlpha, shirtAlpha, shirtAlpha])
#         maskInv = cv2.bitwise_not(shirtAlpha)

#         # Área de la imagen donde la camiseta será superpuesta
#         roi = img[top_left_y:bottom_right_y, top_left_x:bottom_right_x]

#         # Superponer la camiseta con la máscara
#         img1Background = cv2.bitwise_and(roi.copy(), roi.copy(), mask=maskInv)
#         img2Foreground = cv2.bitwise_and(shirtRGB, shirtRGB, mask=shirtAlpha)

#         # Sumar las imágenes de fondo y primer plano
#         dst = cv2.add(img1Background, img2Foreground)
#         img[top_left_y:bottom_right_y, top_left_x:bottom_right_x] = dst

#     # Mostrar la imagen resultante
#     cv2.imshow("DressIA", img)

#     # Esperar la tecla 'q' para salir
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Liberar la cámara y cerrar todas las ventanas
# cap.release()
# cv2.destroyAllWindows()





# import os
# import cv2
# import numpy as np
# from cvzone.PoseModule import PoseDetector

# # Inicialización de la cámara
# cap = cv2.VideoCapture(0)
# detector = PoseDetector()

# # Ruta de las imágenes de las camisetas
# shirtFolderPath = "assets/tshirts"
# listShirts = os.listdir(shirtFolderPath)
# shirtRatioHeightWidth = 581 / 440  # Relación de aspecto de la camiseta

# # Inicializa el número de imagen para la selección de la camiseta
# imageNumber = 0

# while True:
#     success, img = cap.read()
#     if not success:
#         print("Error al leer de la cámara.")
#         break

#     img = detector.findPose(img, draw=False)
#     lmList, _ = detector.findPosition(img, draw=False)

#     if lmList:
#         shoulderLeft = lmList[5][1:3]  # Hombro izquierdo
#         shoulderRight = lmList[2][1:3]  # Hombro derecho

#         if shoulderLeft and shoulderRight:
#             # Calcular el ancho y la altura del torso
#             torsoWidth = np.linalg.norm(np.array(shoulderLeft) - np.array(shoulderRight))
#             torsoHeight = torsoWidth * shirtRatioHeightWidth

#             # Ajustar la posición y tamaño de la camiseta
#             shirtWidth = int(torsoWidth * 1.2)
#             shirtHeight = int(shirtWidth * shirtRatioHeightWidth)

#             # Calcular el centro del torso
#             centerX = (shoulderLeft[0] + shoulderRight[0]) // 2
#             centerY = (shoulderLeft[1] + shoulderRight[1]) // 2 + int(shirtHeight * 0.1)  # Ajuste hacia abajo para centrar

#             # Coordenadas para colocar la camiseta
#             top_left_x = max(centerX - shirtWidth // 2, 0)
#             top_left_y = max(centerY - shirtHeight // 2, 0)

#             # Cargar la camiseta y asegurarse de que exista
#             imgShirtPath = os.path.join(shirtFolderPath, listShirts[imageNumber])
#             imgShirt = cv2.imread(imgShirtPath, cv2.IMREAD_UNCHANGED)
#             if imgShirt is None:
#                 print(f"No se pudo cargar la imagen: {imgShirtPath}")
#                 continue

#             # Redimensionar la camiseta y la máscara para coincidir con la región de interés
#             imgShirt = cv2.resize(imgShirt, (shirtWidth, shirtHeight))
#             shirtRGB = imgShirt[:, :, :3]
#             shirtAlpha = imgShirt[:, :, 3]

#             # Superponer la camiseta en la imagen
#             for c in range(0, 3):
#                 img[top_left_y:top_left_y+shirtHeight, top_left_x:top_left_x+shirtWidth, c] = img[top_left_y:top_left_y+shirtHeight, top_left_x:top_left_x+shirtWidth, c] * (1 - shirtAlpha/255.0) + shirtRGB[:, :, c] * (shirtAlpha/255.0)

#             # Dibujar un rectángulo alrededor de la región de interés para visualización
#             cv2.rectangle(img, (top_left_x, top_left_y), (top_left_x + shirtWidth, top_left_y + shirtHeight), (0, 255, 0), 2)

#     cv2.imshow("DressIA", img)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()



# import os
# import cv2
# import numpy as np
# from cvzone.PoseModule import PoseDetector

# # Inicialización de la cámara
# cap = cv2.VideoCapture(0)
# detector = PoseDetector()

# # Ruta de las imágenes de las camisetas
# shirtFolderPath = "assets/tshirts"
# listShirts = os.listdir(shirtFolderPath)

# # Ajuste de la relación de aspecto de la camiseta basada en la proporción real
# shirtRatioHeightWidth = 1.3  # Esto es algo que puedes ajustar

# # Inicializa el número de imagen para la selección de la camiseta
# imageNumber = 0

# while True:
#     success, img = cap.read()
#     if not success:
#         print("Error al leer de la cámara.")
#         break

#     img = detector.findPose(img, draw=True)
#     lmList, _ = detector.findPosition(img, draw=True)

#     if lmList:
#         shoulderLeft = lmList[11][1:3] if len(lmList) > 11 else None
#         shoulderRight = lmList[12][1:3] if len(lmList) > 12 else None

#         if shoulderLeft and shoulderRight:
#             torsoWidth = np.linalg.norm(np.array(shoulderLeft) - np.array(shoulderRight))
#             torsoHeight = torsoWidth * shirtRatioHeightWidth

#             # Ajustes para posicionar la camiseta más abajo en el torso
#             shirtWidth = int(torsoWidth * 1.2)
#             shirtHeight = int(torsoHeight)

#             centerX = (shoulderLeft[0] + shoulderRight[0]) // 2
#             centerY = (shoulderLeft[1] + shoulderRight[1]) // 2 + int(shirtHeight * 0.1)  # Bajamos la camiseta un poco

#             top_left_x = max(centerX - shirtWidth // 2, 0)
#             top_left_y = max(centerY - shirtHeight // 2, 0)

#             imgShirtPath = os.path.join(shirtFolderPath, listShirts[imageNumber])
#             imgShirt = cv2.imread(imgShirtPath, cv2.IMREAD_UNCHANGED)
#             if imgShirt is None:
#                 print(f"No se pudo cargar la imagen: {imgShirtPath}")
#                 continue

#             imgShirt = cv2.resize(imgShirt, (shirtWidth, shirtHeight))
#             shirtRGB = imgShirt[:, :, :3]
#             shirtAlpha = imgShirt[:, :, 3]

#             for c in range(0, 3):
#                 img[top_left_y:top_left_y+shirtHeight, top_left_x:top_left_x+shirtWidth, c] = img[top_left_y:top_left_y+shirtHeight, top_left_x:top_left_x+shirtWidth, c] * (1 - shirtAlpha/255.0) + shirtRGB[:, :, c] * (shirtAlpha/255.0)

#             cv2.rectangle(img, (top_left_x, top_left_y), (top_left_x + shirtWidth, top_left_y + shirtHeight), (0, 255, 0), 2)

#     cv2.imshow("DressIA", img)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()




# import os
# import cv2
# import numpy as np
# from cvzone.PoseModule import PoseDetector

# # Inicialización de la cámara
# cap = cv2.VideoCapture(0)
# detector = PoseDetector()

# # Ruta de las imágenes de las camisetas
# shirtFolderPath = "assets/tshirts"
# listShirts = os.listdir(shirtFolderPath)
# shirtRatioHeightWidth = 1.3  # Este valor puede necesitar ajuste

# # Inicializa el número de imagen para la selección de la camiseta
# imageNumber = 0

# while True:
#     success, img = cap.read()
#     if not success:
#         print("Error al leer de la cámara.")
#         break

#     img = detector.findPose(img, draw=True)
#     lmList, _ = detector.findPosition(img, draw=True)

#     if lmList:
#         shoulderLeft = lmList[11][1:3] if len(lmList) > 11 else None
#         shoulderRight = lmList[12][1:3] if len(lmList) > 12 else None

#         if shoulderLeft and shoulderRight:
#             torsoWidth = np.linalg.norm(np.array(shoulderLeft) - np.array(shoulderRight))
#             torsoHeight = torsoWidth * shirtRatioHeightWidth

#             shirtWidth = int(torsoWidth * 1.2)
#             shirtHeight = int(torsoHeight)

#             centerX = (shoulderLeft[0] + shoulderRight[0]) // 2
#             centerY = (shoulderLeft[1] + shoulderRight[1]) // 2

#             # Ajustar la posición vertical
#             centerY += int((lmList[1][1] - centerY) * 0.5)  # Suponiendo que lmList[1] es el cuello

#             top_left_x = max(centerX - shirtWidth // 2, 0)
#             top_left_y = max(centerY - shirtHeight // 2, 0)

#             imgShirtPath = os.path.join(shirtFolderPath, listShirts[imageNumber])
#             imgShirt = cv2.imread(imgShirtPath, cv2.IMREAD_UNCHANGED)
#             if imgShirt is None:
#                 print(f"No se pudo cargar la imagen: {imgShirtPath}")
#                 continue

#             imgShirt = cv2.resize(imgShirt, (shirtWidth, shirtHeight))
#             shirtRGB = imgShirt[:, :, :3]
#             shirtAlpha = imgShirt[:, :, 3]

#             for c in range(0, 3):
#                 img[top_left_y:top_left_y+shirtHeight, top_left_x:top_left_x+shirtWidth, c] = img[top_left_y:top_left_y+shirtHeight, top_left_x:top_left_x+shirtWidth, c] * (1 - shirtAlpha/255.0) + shirtRGB[:, :, c] * (shirtAlpha/255.0)

#             cv2.rectangle(img, (top_left_x, top_left_y), (top_left_x + shirtWidth, top_left_y + shirtHeight), (0, 255, 0), 2)

#     cv2.imshow("DressIA", img)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()



# import os
# import cv2
# import numpy as np
# from cvzone.PoseModule import PoseDetector

# # Inicialización de la cámara
# cap = cv2.VideoCapture(0)
# detector = PoseDetector()

# # Ruta de las imágenes de las camisetas
# shirtFolderPath = "assets/tshirts"
# listShirts = os.listdir(shirtFolderPath)

# # Relación de aspecto de la camiseta (esto podría necesitar ajuste)
# shirtRatioHeightWidth = 1.3  

# # Inicializa el número de imagen para la selección de la camiseta
# imageNumber = 0

# while True:
#     success, img = cap.read()
#     if not success:
#         print("Error al leer de la cámara.")
#         break

#     img = detector.findPose(img, draw=True)
#     lmList, _ = detector.findPosition(img, draw=True)

#     if lmList:
#         shoulderLeft = lmList[11][1:3] if len(lmList) > 11 else None
#         shoulderRight = lmList[12][1:3] if len(lmList) > 12 else None

#         if shoulderLeft and shoulderRight:
#             torsoWidth = np.linalg.norm(np.array(shoulderLeft) - np.array(shoulderRight))
#             torsoHeight = torsoWidth * shirtRatioHeightWidth

#             shirtWidth = int(torsoWidth * 1.2)
#             shirtHeight = int(torsoHeight)

#             centerX = (shoulderLeft[0] + shoulderRight[0]) // 2
#             centerY = (shoulderLeft[1] + shoulderRight[1]) // 2

#             centerY += int((lmList[1][1] - centerY) * 0.5)  # Suponiendo que lmList[1] es el cuello

#             top_left_x = max(centerX - shirtWidth // 2, 0)
#             top_left_y = max(centerY - shirtHeight // 2, 0)

#             bottom_right_x = min(top_left_x + shirtWidth, img.shape[1])
#             bottom_right_y = min(top_left_y + shirtHeight, img.shape[0])

#             shirtWidth = bottom_right_x - top_left_x
#             shirtHeight = bottom_right_y - top_left_y

#             imgShirtPath = os.path.join(shirtFolderPath, listShirts[imageNumber])
#             imgShirt = cv2.imread(imgShirtPath, cv2.IMREAD_UNCHANGED)
#             if imgShirt is None:
#                 print(f"No se pudo cargar la imagen: {imgShirtPath}")
#                 continue

#             imgShirt = cv2.resize(imgShirt, (shirtWidth, shirtHeight))
#             shirtRGB = imgShirt[:, :, :3]
#             shirtAlpha = imgShirt[:, :, 3]

#             for c in range(0, 3):
#                 img[top_left_y:bottom_right_y, top_left_x:bottom_right_x, c] = img[top_left_y:bottom_right_y, top_left_x:bottom_right_x, c] * (1 - shirtAlpha/255.0) + shirtRGB[:, :, c] * (shirtAlpha/255.0)

#             cv2.rectangle(img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 2)

#     cv2.imshow("DressIA", img)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()



# import os
# import cv2
# import numpy as np
# from cvzone.PoseModule import PoseDetector

# # Inicialización de la cámara
# cap = cv2.VideoCapture(0)
# detector = PoseDetector()

# # Ruta de las imágenes de las camisetas
# shirtFolderPath = "assets/tshirts"
# listShirts = os.listdir(shirtFolderPath)

# # Relación de aspecto de la camiseta
# shirtRatioHeightWidth = 1.3  # Este valor puede necesitar ajuste

# # Inicializa el número de imagen para la selección de la camiseta
# imageNumber = 0

# while True:
#     success, img = cap.read()
#     if not success:
#         print("Error al leer de la cámara.")
#         break

#     img = detector.findPose(img, draw=False)
#     lmList, _ = detector.findPosition(img, draw=False)

#     if lmList:
#         # Asumiendo que los índices 11 y 12 son hombros izquierdo y derecho
#         shoulderLeft = lmList[11][1:3] if len(lmList) > 11 else None
#         shoulderRight = lmList[12][1:3] if len(lmList) > 12 else None

#         if shoulderLeft and shoulderRight:
#             # Cálculos del torso y camiseta
#             torsoWidth = np.linalg.norm(np.array(shoulderLeft) - np.array(shoulderRight))
#             torsoHeight = torsoWidth * shirtRatioHeightWidth

#             shirtWidth = int(torsoWidth * 1.2)
#             shirtHeight = int(torsoHeight)

#             # Suponiendo que lmList[1] es el cuello
#             neck = lmList[1][1:3] if len(lmList) > 1 else None

#             if neck:
#                 # Cálculos para la transformación de perspectiva
#                 neckX, neckY = neck
#                 centerX = (shoulderLeft[0] + shoulderRight[0]) // 2
#                 centerY = (shoulderLeft[1] + shoulderRight[1]) // 2
#                 centerY += int((neckY - centerY) * 0.5)  # Ajuste para la posición vertical

#                 top_left_x = max(centerX - shirtWidth // 2, 0)
#                 top_left_y = max(centerY - shirtHeight // 2, 0)

#                 bottom_right_x = min(top_left_x + shirtWidth, img.shape[1])
#                 bottom_right_y = min(top_left_y + shirtHeight, img.shape[0])

#                 # Asegurarse de que la región seleccionada de 'img' tenga el mismo tamaño que 'imgShirt'
#                 shirtWidth = bottom_right_x - top_left_x
#                 shirtHeight = bottom_right_y - top_left_y

#                 # Cargar la imagen de la camiseta
#                 imgShirtPath = os.path.join(shirtFolderPath, listShirts[imageNumber])
#                 imgShirt = cv2.imread(imgShirtPath, cv2.IMREAD_UNCHANGED)
#                 if imgShirt is None:
#                     print(f"No se pudo cargar la imagen: {imgShirtPath}")
#                     continue

#                 # Redimensionar la imagen de la camiseta y la máscara alfa para que coincidan con la región de destino
#                 imgShirt = cv2.resize(imgShirt, (shirtWidth, shirtHeight))
#                 shirtAlpha = imgShirt[:, :, 3] / 255.0
#                 shirtRGB = imgShirt[:, :, :3]

#                 # Superponer la camiseta en la imagen
#                 for c in range(0, 3):
#                     imgSection = img[top_left_y:bottom_right_y, top_left_x:bottom_right_x, c]
#                     imgSectionResized = cv2.resize(imgSection, (shirtWidth, shirtHeight))

#                     # Ahora imgSectionResized y shirtRGB deberían tener las mismas dimensiones
#                     img[top_left_y:bottom_right_y, top_left_x:bottom_right_x, c] = (
#                         (1.0 - shirtAlpha) * imgSectionResized + shirtAlpha * shirtRGB[:, :, c]
#                     )

#     # Mostrar la imagen resultante
#     cv2.imshow("DressIA", img)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()






# import os
# import cv2
# import numpy as np
# from cvzone.PoseModule import PoseDetector

# # Inicialización de la cámara
# cap = cv2.VideoCapture(0)
# detector = PoseDetector()

# # Ruta de las imágenes de las camisetas
# shirtFolderPath = "assets/tshirts"
# listShirts = os.listdir(shirtFolderPath)
# imageNumber = 0  # Asegúrate de que este índice sea válido en la lista de camisetas

# # Relación de aspecto de la camiseta
# shirtRatioHeightWidth = 1.3  # Este valor puede necesitar ajuste

# while True:
#     success, img = cap.read()
#     if not success:
#         print("Error al leer de la cámara.")
#         break

#     img = detector.findPose(img, draw=False)
#     lmList, _ = detector.findPosition(img, draw=False)

#     if lmList:
#         # Asumiendo que los índices 11 y 12 son hombros izquierdo y derecho
#         shoulderLeft = lmList[11][1:3] if len(lmList) > 11 else None
#         shoulderRight = lmList[12][1:3] if len(lmList) > 12 else None

#         if shoulderLeft and shoulderRight:
#             torsoWidth = np.linalg.norm(np.array(shoulderLeft) - np.array(shoulderRight))
#             torsoHeight = torsoWidth * shirtRatioHeightWidth

#             shirtWidth = int(torsoWidth * 1.2)
#             shirtHeight = int(torsoHeight * 1.2)

#             # Suponiendo que lmList[1] es el cuello
#             neck = lmList[1][1:3] if len(lmList) > 1 else None
#             if neck:
#                 neckX, neckY = neck
#                 centerX = (shoulderLeft[0] + shoulderRight[0]) // 2
#                 centerY = (shoulderLeft[1] + shoulderRight[1]) // 2
#                 centerY += int((neckY - centerY) * 0.5)  # Ajuste para la posición vertical

#                 top_left_x = max(centerX - shirtWidth // 2, 0)
#                 top_left_y = max(centerY - shirtHeight // 2, 0)

#                 bottom_right_x = min(top_left_x + shirtWidth, img.shape[1])
#                 bottom_right_y = min(top_left_y + shirtHeight, img.shape[0])

#                 # Asegurar que la región de destino tiene las dimensiones correctas
#                 region_width = bottom_right_x - top_left_x
#                 region_height = bottom_right_y - top_left_y

#                 # Cargar la imagen de la camiseta
#                 imgShirtPath = os.path.join(shirtFolderPath, listShirts[imageNumber])
#                 imgShirt = cv2.imread(imgShirtPath, cv2.IMREAD_UNCHANGED)
#                 if imgShirt is None:
#                     print(f"No se pudo cargar la imagen: {imgShirtPath}")
#                     continue

#                 # Redimensionar la imagen de la camiseta y la máscara alfa para que coincidan con la región de destino
#                 imgShirt = cv2.resize(imgShirt, (region_width, region_height))
#                 shirtAlpha = imgShirt[:, :, 3] / 255.0
#                 shirtRGB = imgShirt[:, :, :3]

#                 # Superponer la camiseta en la imagen
#                 for c in range(0, 3):
#                     img[top_left_y:top_left_y+region_height, top_left_x:top_left_x+region_width, c] = (
#                         img[top_left_y:top_left_y+region_height, top_left_x:top_left_x+region_width, c] * (1 - shirtAlpha) +
#                         shirtRGB[:, :, c] * shirtAlpha
#                     )

#     cv2.imshow("DressIA", img)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()




import os
import cv2
import numpy as np
from cvzone.PoseModule import PoseDetector

# Inicialización de la cámara
cap = cv2.VideoCapture(0)
detector = PoseDetector()

# Ruta de las imágenes de las camisetas
shirtFolderPath = "assets/tshirts"
listShirts = os.listdir(shirtFolderPath)
imageNumber = 0  # Asegúrate de que este índice sea válido en la lista de camisetas

# Relación de aspecto de la camiseta
shirtRatioHeightWidth = 1.3  # Este valor puede necesitar ajuste

while True:
    success, img = cap.read()
    if not success:
        print("Error al leer de la cámara.")
        break

    img = detector.findPose(img, draw=False)
    lmList, _ = detector.findPosition(img, draw=False)

    if lmList:
        shoulderLeft = lmList[11][1:3] if len(lmList) > 11 else None
        shoulderRight = lmList[12][1:3] if len(lmList) > 12 else None
        hipLeft = lmList[23][1:3] if len(lmList) > 23 else None
        hipRight = lmList[24][1:3] if len(lmList) > 24 else None
        neck = lmList[1][1:3] if len(lmList) > 1 else None

        if shoulderLeft and shoulderRight and hipLeft and hipRight and neck:
            torsoWidth = np.linalg.norm(np.array(shoulderLeft) - np.array(shoulderRight))
            hipWidth = np.linalg.norm(np.array(hipLeft) - np.array(hipRight))
            torsoHeight = torsoWidth * shirtRatioHeightWidth

            shirtWidth = int((hipWidth + torsoWidth) / 2 * 1.2)
            shirtHeight = int(torsoHeight * 1.2)

            neckX, neckY = neck
            centerX = (shoulderLeft[0] + shoulderRight[0]) // 2
            centerY = (shoulderLeft[1] + shoulderRight[1]) // 2
            centerY += int((neckY - centerY) * 0.5)

            top_left_x = max(centerX - shirtWidth // 2, 0)
            top_left_y = max(centerY - shirtHeight // 2, 0)

            bottom_right_x = min(top_left_x + shirtWidth, img.shape[1])
            bottom_right_y = min(top_left_y + shirtHeight, img.shape[0])

            region_width = bottom_right_x - top_left_x
            region_height = bottom_right_y - top_left_y

            imgShirtPath = os.path.join(shirtFolderPath, listShirts[imageNumber])
            imgShirt = cv2.imread(imgShirtPath, cv2.IMREAD_UNCHANGED)
            if imgShirt is None:
                print(f"No se pudo cargar la imagen: {imgShirtPath}")
                continue

            imgShirt = cv2.resize(imgShirt, (region_width, region_height))
            shirtAlpha = imgShirt[:, :, 3] / 255.0
            shirtRGB = imgShirt[:, :, :3]

            for c in range(0, 3):
                img[top_left_y:top_left_y+region_height, top_left_x:top_left_x+region_width, c] = (
                        img[top_left_y:top_left_y+region_height, top_left_x:top_left_x+region_width, c] * (1 - shirtAlpha) +
                        shirtRGB[:, :, c] * shirtAlpha
                )

    cv2.imshow("DressIA", img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('c'):
        img_with_clothing = img.copy()
        cv2.imwrite("persona_con_camisa.jpg", img_with_clothing)
        print("Imagen con la camiseta puesta guardada como 'persona_con_camisa.jpg'")
    elif key == ord('r'):
        if lmList:
            shoulderWidth = np.linalg.norm(np.array(shoulderLeft) - np.array(shoulderRight))
            torsoWidth = np.linalg.norm(np.array(hipLeft) - np.array(hipRight))

            report_text = f"Tamaño de hombros: {shoulderWidth:.2f} px\nTamaño de torso: {torsoWidth:.2f} px\n"

            # Lógica de recomendaciones de tallas
            size_recommendation = ""
            if torsoWidth < 100:
                size_recommendation += "Talla S podría ser apropiada.\n"
            elif 100 <= torsoWidth < 150:
                size_recommendation += "Talla M podría ser apropiada.\n"
            else:
                size_recommendation += "Talla L podría ser apropiada.\n"

            report_text += f"Recomendaciones:\n{size_recommendation}"

            with open('reporte_tallas.txt', 'a') as file:
                file.write(report_text)
                print("Reporte guardado en 'reporte_tallas.txt'")

cap.release()
cv2.destroyAllWindows()