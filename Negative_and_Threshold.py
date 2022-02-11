import cv2

#Read the image and stored in img object
img=cv2.imread('c:\\Users\\User\\Downloads\\ex4.jpg')


#Find width and height of image
height = img.shape[0]
print(height)
width = img.shape[1]
print(width)


#FIND NEGATIVE

#Looping to change pixel value
for x in range(height):
  for y in range(width):

     pixel_val=img[x,y]
    
        #s=(L-1)-r s=255-r
        #subtract ecah pixel value from 255(maximum value)
     
     red=255-pixel_val[0]
     green=255-pixel_val[1]
     blue=255-pixel_val[2]

      #written modified pixel value
     img[x,y]=red,green,blue

#save negative image
cv2.imwrite('c:\\Users\\User\\Downloads\\img_negative.jpg', img)

#THRESOLDING


for x in range(height):
  for y in range(width):

     r,g,b=img[x,y]
     
     #if pixel value >127 change it to 255 (maximum)
     if r>=127 and g>=127 and b>=127:
         
        red=255
        green=255
        blue=255

     #else make pixel value=0    
     else:
         
        red=0
        green=0
        blue=0

      
     img[x,y]=red,green,blue

#save the image
cv2.imwrite('c:\\Users\\User\\Downloads\\img_thresold.jpg', img)


#THRESOLD SECOND WAY

sumr=0
sumg=0
sumb=0
count=0

for x in range(height):
  for y in range(width):
    r,g,b=img[x,y]
    sumr=sumr+r
    sumg=sumg+g
    sumb=sumb+b
    
    count=count+1 
    
#Calculating Average Independently for Red,Green,Blue

avgr=sumr/count
avgg=sumg/count
avgb=sumb/count


for x in range(height):
  for y in range(width):

     rr,gg,bb=img[x,y]
    
     #if pixel value is greater than average than make it 255(maximum)     
     if rr>=avgr and gg>=avgg and bb>=avgb:
         
         
        red=255
        green=255
        blue=255

     #else make it 0
     else:
         
        red=0
        green=0
        blue=0

      
     img[x,y]=red,green,blue
     
cv2.imwrite('c:\\Users\\User\\Downloads\\img_thresoldsecond.jpg', img)

