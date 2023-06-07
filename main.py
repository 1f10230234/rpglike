import turtle as t

import print_text as p

import move_animation as m

x = 1280

y = 640

t.screensize(x,y)

global_i = 3


global_j = 6

condition = 1 #0->inputable 1->moving 2->selecting

map = 1

map_wide = 4

map_crate = 0

ban_eventlist = {
    0:"20304021314151324252625363736474/0313234353637304142444546474"
}

#def move_map(map,de,wide):



#def select(mouse_x,mouse_y):
#    global condition
#    if condition == 2:
#        react


def ban_event(i,j):
    print(i,j)
    global ban_eventlist
    ban_event = ban_eventlist[map]
    for n in range((len(ban_eventlist[map])//2)):
        if ban_event[n*2] == "/":
            print("a")
            for l in range(len(ban_eventlist[map])//2-n):
                print(ban_event[l*2+n*2+1],ban_event[l*2+n*2+2])
                if (int(ban_event[l*2+n*2+1]) + 8 == i) and (int(ban_event[l*2+n*2+2]) == j):
                    print("u")
                    return(True)
            break
        print(ban_event[n*2],ban_event[n*2+1])
        if (int(ban_event[n*2]) == i) and (int(ban_event[n*2+1] )== j):
            print("i")
            return(True)




def controll(mouse_x,mouse_y):
    print(1)
    global condition
    if condition == 0:
        if abs(mouse_x) < x/2 or abs(mouse_y) < y/2:
            condition  = -2
        if mouse_x < -x/2:
            mouse_x = -x/2
        if mouse_x > x/2:
            mouse_x = x/2
        if mouse_y < -y/2:
            mouse_y = -y/2
        if mouse_y > y/2:
            mouse_y = y/2
        condition += 1
        global global_i
        global global_j
        a = 0
        b = 0
        c = 0
        d = 0
        de = 0
        while (a != 1 or b != 1 or
               c != 1 or d != 1):
            if mouse_y < global_j*-80+y/2-80:
                print(mouse_x,mouse_y)
                print(global_j*-80+y/2-80)
                global_j += 1
                print(2)
                de = 2
            else:
                a = 1
            if mouse_y > global_j*-80+y/2:
                print(mouse_x,mouse_y)
                print(global_j*-80+y/2)
                global_j -= 1
                print(4)
                de = 4
            else:
                b = 1
            if mouse_x < global_i*80-x/2:
                print(mouse_x,mouse_y)
                print(global_i*80-x/2)
                global_i -= 1
                print(1)
                de = 1
            else:
                c = 1
            if mouse_x > global_i*80-x/2+80:
                print(mouse_x,mouse_y)
                print(global_i*80-x/2+80)
                global_i += 1
                print(3)
                de = 3
            else:
                d = 1
            if ban_event(global_i,global_j):
                p.print_text_start(-320,80,1,4,"%kikenn")
                break
            if (a == 1 and b == 1 and
               c == 1 and d == 1):
                break
            m.move_animation(global_i,global_j,0.5,de)

#            if condition == -1:

            
            print(a,b,c,d)
            
        
        condition = 0


t.onscreenclick(controll,btn=1)
if map_crate == 0:
    if map == 1:
        p.print_text_start(-640,320,4,0,"/400//401/")
        #p.print_text_start(-560,-160,0.5,0,"/500//501/")
        #p.print_text_start(-560,-80,0.5,0,"/502//503/")
        m.move_animation(3,6,0.5,1)
        map_crate = 1
        condition = 0
        map = 0


t.done()
