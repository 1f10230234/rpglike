import turtle as t

t.speed(0)

t.shape('square')

t.resizemode("user")

t.penup()

global_i = 0

global_j = 0

stamp_count = 0


x = 1280

y = 640

t.screensize(x,y)

cos_list = {
    1:"0002380009333380090777800907770011122247074444200004442200990990",
    2:"0022220009333330097777800977770011122240074444202244442209900990",
    3:"0083209008333390087770900077711102222470744440002244400009909900",
    4:"0088889008888880088888800077771100222240072332202222322209900990",
}

color_list = ['black', 'red','purple', 'blue','green','yellow','orange','brown','gray']

def move_animation(i,j,sz,dir):
    t.shapesize(sz,sz,0)
    global x
    global y
    global global_i
    global global_j
    global stamp_count
    global_i = i
    global_j = j
    nx = i*80-x/2+5
    ny = -j*80+y/2-5
    #print(stamp_count)
    t.clearstamps(-1*stamp_count)
    stamp_count = 0
    t.goto(nx,ny)
    a = 0
    costume = cos_list[dir]
    for l in range(64):
        if int(costume[l]) != 0:
            for b in range(len(color_list)):
                if int(costume[l]) == b+1:
                    t.color(color_list[b])
                    t.stamp()
            stamp_count += 1
        t.fd(20*sz)
        a += 1
        if a%8 == 0:
            t.goto(nx,t.ycor()-20*sz)
    t.ht()
    


    
    

