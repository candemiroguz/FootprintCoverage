#Footprint Coverage and GSD Calculation#

#written by candemiroguz


#Camera sensor x size
#Camera sensor y size
#f focal lenght
#h AGL
#Xo= Middle of X coordinate of image
#Yo= Middle of Y coordinate of image
#Zo= Middle of Z coordinate of image



Question = input("Do you have Xo, Yo and Zo Coordinates ?\n")

FL= Question[0].lower()
if FL == "" or not FL in ['y','n']:
    print("****************************\n\n","--Please Answer Correctly--\n\n****************************")

elif FL == 'y':

    #inputs
    PSx = float(input("Pixel number x \n"))
    PSy = float(input("Pixel number y \n"))
    CSx = float(input("Camera sensor x size (mm)\n"))
    CSy = float(input("Camera sensor y size (mm)\n"))
    f = float(input("Camera focal lenght (mm)\n"))
    h = float(input("h (meter) from AGL\n"))
    Xo= float(input("Xo coordinates\n"))
    Yo= float(input("Yo coordinates\n"))
    Zo= float(input("Zo coordinates\n"))

    #calculation
    ax = (Zo / f) * CSx
    ay = (Zo / f) * CSy
    Area = (ax * ay)
    Lx = Xo - ax
    Rx = Xo + ax
    Ly = Yo - ay
    Ry = Yo + ay
    pxszex = CSx / PSx
    pxszey = CSy / PSy
    GSD = Zo / f * pxszex

    #print
    print('X Coordinate -left- \n', Lx)
    print('Y Coordinate -left- \n', Ly)
    print('X Coordinate -right- \n', Rx)
    print('Y Coordinate -right- \n', Ry)
    print('Footprint Coverage Area\n', Area,'m2')
    print(GSD)

elif FL == 'n':

    #inputs
    PSx = float(input("Pixel number x \n"))
    PSy = float(input("Pixel number y \n"))
    CSx = float(input("Camera sensor x size (mm)\n"))
    CSy = float(input("Camera sensor y size (mm)\n"))
    f = float(input("Camera focal lenght (mm)\n"))
    h = float(input("h (meter) from AGL\n"))

    #calculation
    ax = (h/f) * CSx
    ay = (h/f) * CSy
    Area = (ax*ay)
    pxszex = CSx / PSx
    pxszey = CSy / PSy
    GSD = h/f * pxszex

    #print
    print('Along x\n',ax,'m')
    print('Along y\n',ay,'m')
    print('Footprint Coverage Area\n',Area,'m2')
    print(GSD)
