import cv2
import numpy as np

image = cv2.imread('screen_parsing.png')
#cv2.imshow('original',image)
"""
kernel_3x3=np.ones((3,3),np.float32)/9

blurred=cv2.filter2D(image,-1,kernel_3x3)
cv2.imshow('3x3_blurring', blurred)
"""
#print(image.shape)
#area = image[200:400, 100:200]

startRow = 0
startCol = 0
loopi = True
loopj = True

signedArray = []
startRow = 0
startCol = 0

for i in range(len(image)):
    if loopi == True:
        for j in range(len(image[0])):
            if loopj == True:
                if image[i][j][2] > 160 and image[i][j][1] > 160 and image[i][j][0] == 0:
                    if i > startRow + 30 or j > startCol + 30 :
                        startRow = i
                        startCol = j
                        endRow = i + 10
                        endCol = j + 8
                        signedArray.append([startRow,endRow,startCol,endCol])
                        print("I am here for")

print(signedArray)

for i in range(len(signedArray)):
    for j in range(len(signedArray[0])):
        result = image[signedArray[i][0]:signedArray[i][1],signedArray[i][2]:signedArray[i][3]]
        print(i)
        cv2.imwrite(f"results/result{i}.jpg",result)

#area = image[startRow:endRow, startCol:endCol]

#cv2.imshow("image",image)
#cv2.imshow("area",area)


#print(area.shape)
#print(startRow,startCol)
#print(area[0][0])

cv2.waitKey(0)