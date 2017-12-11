"""Sudoku game

Exercises

1. Make sudoku game layout
2. Give some hint for avaiable input number
3. Work like helping tool for player


"""

from random import *
from turtle import *
from freegames import floor, vector

tiles = {}
tiles_change = {}
# sudoku data input by row 
input = [(8,None,None,None,None,4,6,None,None),
        (None,9,6,1,None,None,None,3,None),
        (None,None,None,None,None,None,2,5,None),
        (None,4,5,8,None,7,None,2,6),
        (6,8,None,None,2,None,None,4,1),
        (9,2,None,4,None,5,8,7,None),
		(None,5,8,None,None,None,None,None,None),
        (None,1,None,None,None,8,3,6,None),
        (None,None,3,2,None,None,None,None,7)]

#
number = {}
number_change = {}
digit = [1,2,3,4,5,6,7,8,9,None]

current_digit_number = 1
current_digit_vector = (0,0)

block = {'row0':[], 'row1':[], 'row2':[], 'row3':[], 'row4':[], 'row5':[], 'row6':[], 'row7':[], 'row8':[], 
        'col0':[], 'col1':[], 'col2':[], 'col3':[], 'col4':[], 'col5':[], 'col6':[], 'col7':[], 'col8':[],
        'square00':[], 'square01':[], 'square02':[], 'square10':[], 'square11':[], 'square12':[], 'square20':[], 'square21':[], 'square22':[]}

def load():
    "Load tiles and scramble."
    for y in range(-250, 200, 50):
        for x in range(-250, 200, 50):
            mark = vector(x, y)
            #i = int((y+250)/50)
            #j = int((x+250)/50)
            i,j = vec2rowcol(mark)
            row = 'row' + str(j)
            col = 'col' + str(i)
            square = 'square' + str(int(j/3)) + str(int(i/3))
            #print("x,y,j,i", x,y,j,i,square)
            
            block[row].append(mark)
            block[col].append(mark)
            block[square].append(mark)
            tiles[mark] = input[8-i][j]
            tiles_change[(x,y)] = [1,0, 'black', 'white']

    #print("block", block)
    for y in range(250, 300, 50):
        for x in range(-250, 250, 50):
            mark = vector(x, y)
            j = int((x+250)/50)
            number[mark] = digit[j]
            number_change[(x,y)] = 1

def vec2rowcol(vector):
    i = int((vector.y+250)/50)
    j = int((vector.x+250)/50)    
    return i,j   

def checkIfUnchangedPos(mark):
    global input
    i,j = vec2rowcol(mark)
    if input[8-i][j] is not None:
        return True
    else:
        return False
    
def square(mark, number, penclrm='black', fillclr='white'):
    "Draw white square with black outline and number."
    up()
    goto(mark.x, mark.y)
    down()
   
    color(penclrm, fillclr)
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()
       
    if number is None:
        return
    elif number < 10:
        forward(20)

    write(number, font=('Arial', 30, 'normal'))

def tap(x, y):
    "Swap tile and empty square."
    global current_digit_number
    temp = [0,0,0,0,0,0,0,0,0,0]
    x = int(floor(x, 50))
    y = int(floor(y, 50))
    mark = vector(x, y)
    #print("tap", x, y)
   
    if(y >= 250 and y < 300 and x >= -250 and x < 250):
        # fill color to white
        update_number()
        current_digit_number = number[mark]
        current_digit_vector = mark
        square(mark, number[mark], 'black', 'yellow')
        number_change[(x,y)] = 1
        #print("current digit number", current_digit_number)
    elif(y >= -250 and y < 200 and x >= -250 and x < 200):
        if checkIfUnchangedPos(mark):
            return
        initTilesChange()
        #print("tiles_change", tiles_change)
        tiles[mark] = current_digit_number
        #square(mark, tiles[mark], 'black', 'pink')
        #tiles_change[(x,y)] = [1,'black', 'pink']
        copyList((x,y),[1, 'black', 'pink'])
        #print("tiles_change tap", tiles_change)
        
        i,j = vec2rowcol(mark)
        row = 'row' + str(j)
        col = 'col' + str(i)
        squ = 'square' + str(int(j/3)) + str(int(i/3))
        for vec in block[row]:
            if(tiles[vec] == current_digit_number) and (tiles[vec] is not None):
                #square(vec, tiles[vec], 'red', 'pink')
                #tiles_change[(vec.x,vec.y)] = [1, 'red', 'pink']
                copyList((vec.x,vec.y),[1, 'red', 'pink'])
            else:
                #square(vec, tiles[vec], 'black', 'pink')
                #"tiles_change[(vec.x,vec.y)] = [1, 'black', 'pink']
                copyList((vec.x,vec.y),[1, 'black', 'pink'])
            if tiles[vec] is not None:
                temp[tiles[vec]] = 1
        #print("tiles_change row", tiles_change)
        for vec in block[col]:
            if(tiles[vec] == current_digit_number) and (tiles[vec] is not None):
                #square(vec, tiles[vec], 'red', 'pink')
                #tiles_change[(vec.x,vec.y)] = [1,'red', 'pink']
                copyList((vec.x,vec.y),[1, 'red', 'pink'])
            else:
                #square(vec, tiles[vec], 'black', 'pink')
                #tiles_change[(vec.x,vec.y)] = [1,'black', 'pink']
                copyList((vec.x,vec.y),[1, 'black', 'pink'])
            if tiles[vec] is not None:
                temp[tiles[vec]] = 1
        for vec in block[squ]:
            if(tiles[vec] == current_digit_number) and (tiles[vec] is not None):
                #tiles_change[(vec.x,vec.y)] = [1, 'red', 'pink']
                copyList((vec.x,vec.y),[1, 'red', 'pink'])
            else:
                #tiles_change[(vec.x,vec.y)] = [1, 'black', 'pink']
                copyList((vec.x,vec.y),[1, 'black', 'pink'])
            if tiles[vec] is not None:
                temp[tiles[vec]] = 1         
        update_tiles()

        for vec in number:
            if (number[vec] is not None) and temp[number[vec]] != 0 :
                square(vec, number[vec], 'black', 'grey')
                number_change[(vec.x,vec.y)] = 1
    else:
        initTilesChange()
        update_tiles()
        
def copyList(t,l):
    global tiles_change
    #print("before ",t[0], t[1], tiles_change[t])
    tiles_change[t][1] = l[0]
    tiles_change[t][2] = l[1]
    tiles_change[t][3] = l[2]
    #print("after ",tiles_change[t])
    
def draw_tiles():
    "Draw all tiles."
    for mark in tiles:
        i,j = vec2rowcol(mark)
        if (i in range(3,6)) and (j in range(3,6)):
            square(mark, tiles[mark], 'black', 'green')		
        elif  (i in range(3,6)):
            square(mark, tiles[mark], 'black', 'grey')
        elif  (j in range(3,6)):
            square(mark, tiles[mark], 'black', 'blue')			
        else:        		
            square(mark, tiles[mark])
        #break
    update()
def initTilesChange():
    #print("initTilesChange")
    for k,v in tiles_change.items():
        mark = vector(k[0],k[1])
        i, j = vec2rowcol(mark)
        if checkIfUnchangedPos(mark):
            v[2] = 'purple'
        else:
            v[2] = 'black'
        if (i in range(3,6)) and (j in range(3,6)):
            v[3] = 'green'
        elif  (i in range(3,6)):
            v[3] = 'green'
        elif  (j in range(3,6)):
            v[3] = 'blue'
        else:        		
            v[3] = 'white'
    #print("tiles_change", tiles_change)
    
def update_tiles():
    #print("update_tiles")
    #print("tiles_change before", tiles_change)
    "Draw all tiles."
    penclr = 'black'
    fillclr = 'white'
    #print("tiles_change before update\n", tiles_change)
    for k,v in tiles_change.items():
        if v[0] == 1 or v[1] == 1:
            #print("i,j", i, j)
            mark = vector(k[0],k[1])
            i, j = vec2rowcol(mark)
            penclr = v[2]
            fillclr = v[3]
            square(mark, tiles[mark], penclr, fillclr)
            if v[0] == 1 and v[1] == 0:
                v[0] = 0
            else:
                v[0] = 1
                v[1] = 0
                            
        #break
    #print("tiles_change after update\n", tiles_change)
    #print("tiles_change after", tiles_change)
    update()

def draw_number():
    for mark in number:
        square(mark, number[mark])
    update()

def update_number():
    for k,v in number_change.items():
        if v == 1:
            mark = vector(k[0],k[1])
            square(mark, number[mark])
            number_change[k] = 0
    update()

#setup(420, 420, 370, 0)
setup(900, 900, 0, 0)
hideturtle()
tracer(False)
load()
update_number()
initTilesChange()
update_tiles()
onscreenclick(tap)
done()
