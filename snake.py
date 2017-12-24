import tkinter
from random import randint


root=tkinter.Tk()
root.title('snake')
root.geometry('250x250+400+400')
la=tkinter.Label(root,font='Courier 10')
la.pack()
get_new=0
                 

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
        
    

        

def loose():
    global la
    la['text']='YOU LOSE'
    root.bind('<Key>',lambda x:x)
    but=tkinter.Button(root,text='CLOSE',font='Courier 20',background='red')
    but.pack()
    but.bind('<Button>',root.destroy())

def go():
    global pole,zmeyka,st,get_new
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


def go0(e):
    global st
    st=0
    go()

def go1(e):
    global st
    st=1
    go()

def go2(e):
    global st
    st=2
    go()

def go3(e):
    global st
    st=3
    go()

def god(e):
    a=e.keycode
    if a==87 or a==38:
        go0(e)
    if a==68 or a==39 :
        go1(e)
    if a==83 or a==40 :
        go2(e)
    if a==65 or a==37 :
        go3(e)



    
zmeyka=[[5,5],[5,4],[5,3],[4,3],[4,4],[4,5]]
root.bind('<Key>',god)



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


        
apple()
go()