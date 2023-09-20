fr=open("sudoku.txt","r")
sudoku=[]
#for i in fr:
#   print(i.end="")

def inputParser(fr,sudoku):
    for row in fr:
        temp=[]
        for cc in row.strip():
            temp.append(int(cc))
        sudoku.append(temp)
    print(sudoku)

count_x=0
count_y=0
def check(x:int,y=int,n=int)->bool:
    global count
    for i in range(9):
        if sudoku[j][x]==n or sudoku[y][j]==n:
            return False
        if count_x<3:
            check(x+1,y,n)
            count_x+=1
        else:
            if count_y<3:
                check(x,y+1,n)
                count_y+=1
                count_x=0

def solver():
    global sudoku
    for y in range(9):
        for x in range(9):
            if sudoku[y][x]==0:
                for n in range(1,10):
                    if check(x,y,n):
                        sudoku[y][x]=n
                        solver()
                        sudoku[y][x]=0
                return
    print(sudoku)
    input()

inputParser(fr,sudoku)
