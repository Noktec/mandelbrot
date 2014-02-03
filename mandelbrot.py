import Image

x1 = -2.1
x2 = 0.6
y1 = -1.2
y2 = 1.2
maxIterations = 50

image_x = 1024          
image_y = 1024
image = Image.new("RGB", (image_x, image_y), "black")

for y in range(image_y):
    Zy = y * (y2 - y1) / (image_y - 1) + y1
    for x in range(image_x):
        Zx = x * (x2 - x1) / (image_x - 1) + x1
        Z = Zx + Zy * 1j    
        c = Z
        for n in range(maxIterations): 
            if abs(Z) > 2.0: 
                break                           
            Z = Z * Z + c                              
        R = n % 4 * 256
        G = n % 8 * 256
        B = n % 16 * 256
        image.putpixel((x, y), R*10+G+B)

image.show()
