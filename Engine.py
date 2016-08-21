import random
from PIL import Image, ImageDraw
p = Image.open("E:/Эксперименты с Py/Lean.jpg")
#wp = Image.open("E:/Эксперименты с Py/Lean.jpg")
pixels = p.load()
x,y = p.size
print(p.size)
draw = ImageDraw.Draw(p)
mode = int(input('mode:'))
if (mode == 1):
    factor = int(input('factor:'))
    for i in range(x):
        for j in range(y):
            rnd = random.randint(-factor, factor)
            r , g , b = pixels[i,j]
            r = pixels[i,j][0] + rnd
            g = pixels[i,j][1] + rnd
            b = pixels[i,j][2] + rnd
            if (r < 0):
                r = 0
            if (g < 0):
                g = 0
            if (b < 0):
                b = 0
            if ( r > 255):
                r = 255
            if ( g > 255):
                g = 255
            if( b > 255):
                b = 255
            draw.point((i,j),(r, g, b))
    p.show()
    #p.save("E:/Эксперименты с Py/BG - копия.png")
    print("Результат на диске")
if(mode == 2):
    for i in range(x):
        for j in range (y):
            x//2
            r, g ,b = pixels[i,j]
            if(i <(x//2)):
                pixels[i,j] = (r-40)
    p.show()
    p.save("E:/Эксперименты с Py/Lean-копия.jpg")
    print("Результат на диске")
if(mode == 3):
            p.paste(wp, (150, 80),  wp)
            p.save("E:/Эксперименты с Py/lean - копия.png")
            print("Результат на диске")
if (mode == 4):
    for i in range(x):
        for j in range(y):
            
            r,g,b = pixels[i,j]
            if(x > 0 and y > 0 ):
                draw.point((x,y),(r,g,b))
#if (mode == 5):
 #   for i in range(x):
  #      for j in range(y):
   #         row = random.randint(-x,x)
    #        col = random.randint(-y,y)
     #       row//2
#print(row,col)
#p.show()
     #Плланируется намутить сортировку пикселей

    


        
        
