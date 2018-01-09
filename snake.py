import sys
import threading
import time
import tkinter
from random import randint



system=sys.platform
if system.find('win')=0:
    up=[87,38]
    r=[39,68]
    d=[83,40]
    l=[65,37]
if system.find('linux')=0:
    up=[25,111]
    r=[40,114]
    d=[39,116]
    l=[38,113]

root=tkinter.Tk()
root.title('snake')
root.geometry('250x250+400+400')
get_new=0

la=tkinter.Label(root,font='Courier 10')

def print_pole():
    global pole,la
    d=''
    for i in range(len(pole)):
        a=''
        for j in range(len(pole[i])):
            a=a+pole[i][j]+" "
        if i!=len(pole)-1:
            a=a+'\n'
        d=d+a
        del a
    la['text']=d


def apple():
    global zmeyka,pole
    appx,appy=randint(1,13),randint(1,13)
    if [appx,appy] in zmeyka:
        apple()
    else:
        pole[appy][appx]='g'
        print('new apple at {0} {1}'.format(appx,appy))
        
    
def qite(e):
    global root
    root.destroy()


def gogo(e):
    global zmeyka,st,pole,but,br
    st=2
    pole=[]
    br.destroy()
    but.destroy()
    for i in range(15):
        a=[]
        for j in range(15):
            a.append(' ')
        pole.append(a)
        del a
    for i in range(15):
        if i==0 or i==14:
            for j in range(15):
                pole[i][j]='+'
        else:
            pole[i][0],pole[i][14]='+','+'
    zmeyka=[[5,5],[5,4],[5,3],[4,3],[4,4],[4,5]]
    apple()
    go()




def loose():
    global la,root,t,br,but
    but=tkinter.Button(root,text='CLOSE',font='Courier 20',background='red')
    but.bind('<Button-1>',qite)
    br=tkinter.Button(root,text='restart',font='Courier 20',background='green')
    br.bind('<Button>',gogo)
    la['text']='YOU LOSE'
    t.cancel()
    br.pack()
    but.pack()


def go():
    global pole,zmeyka,st,get_new,t
    t=threading.Timer(0.5,go)   
    end=zmeyka[len(zmeyka)-1]
    if st==0:
        a=[zmeyka[0][0],zmeyka[0][1]-1]
    if st==1:
        a=[zmeyka[0][0]+1,zmeyka[0][1]]
    if st==2:
        a=[zmeyka[0][0],zmeyka[0][1]+1]
    if st==3:
        a=[zmeyka[0][0]-1,zmeyka[0][1]]
    if pole[a[1]][a[0]]=='g':
        get_new=1
    if pole[a[1]][a[0]]=='+' or a in zmeyka:
        loose()
    else:    
        for i in range(len(zmeyka)):
            pole[zmeyka[i][1]][zmeyka[i][0]]=' '
    
        d=[a]
        for i in range(len(zmeyka)-1):
            d.append(zmeyka[i])
        zmeyka=d
        pole[zmeyka[0][1]][zmeyka[0][0]]='a'
        for i in range(1,len(zmeyka),1):
            pole[zmeyka[i][1]][zmeyka[i][0]]='o'
        print_pole()
        if get_new==1:
            zmeyka.append(end)
            apple()
            get_new=0
    t.start()

def go0(e):
    global st
    st=0

def go1(e):
    global st
    st=1

def go2(e):
    global st
    st=2

def go3(e):
    global st
    st=3


def game():
    print('game started twise')
    i=0
    ts=time.time()
    while 1:
        if time.time()-ts>=2:
            go()
            game()

def start(e):
    global root,la,but_start,but_qite,t
    print('game started')
    but_start.destroy()
    but_qite.destroy()
    la.pack()
    time.sleep(2)
#    game()
    root.title('u in game')
    go()

def god(e):
    a=e.keycode
    if a in up:
        go0(e)
    if a in r:
        go1(e)
    if a in d:
        go2(e)
    if a in l:            



        go3(e)




t=threading.Timer(0.5,go)   
but_start=tkinter.Button(root,text='Start game')
but_start.bind('<Button>',start)
but_start.pack()

but_qite=tkinter.Button(root,text='Qite')
but_qite.bind('<Button>',qite)
but_qite.pack()

root.bind('<Key>',god)
#root.bind('<ц>',go0)
#root.bind('<в>',go1)
#root.bind('<ы>',go2)
#root.bind('<ф>',go3)

       
but=tkinter.Button(root,text='CLOSE',font='Courier 20',background='red')
but.bind('<Button-1>',qite)
br=tkinter.Button(root,text='restart',font='Courier 20',background='green')
br.bind('<Button>',gogo)
st=2
pole=[]
for i in range(15):
    a=[]
    for j in range(15):
        a.append(' ')
    pole.append(a)
    del a
for i in range(15):
    if i==0 or i==14:
        for j in range(15):
            pole[i][j]='+'
    else:
        pole[i][0],pole[i][14]='+','+'
zmeyka=[[5,5],[5,4],[5,3],[4,3],[4,4],[4,5]]

apple()
root.mainloop()