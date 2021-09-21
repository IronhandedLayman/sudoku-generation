import random

class BasicSudoku:
    def __init__(self, sx=3, sy=3, bx=3, by=3):
        self.sx=sx #size of each box in columns
        self.sy=sy #size of each box in rows
        self.bx=bx #number of boxes horizontally
        self.by=by #number of boxes vertically
        self.dx=sx*bx #total number of columms
        self.dy=sy*by #total number of rows
        self.givens=[[None for _ in range(self.dx)] for _ in range(self.dy)] #clean slate set of givens
        self.curstate=[[None for _ in range(self.dx)] for _ in range(self.dy)] #clean slate set of current solved position


    def printProblem(self):
        self.print(self.givens)

    def printCurstate(self):
        self.print(self.curstate)

    def print(self, grid):
        print("\n".join(self.repr(grid)))
    
    def repr(self, grid):
        # on calculation of lines below: numlines = num. of rows (dy) + box separators (by-1) + top and bottom (2)
        ans = [""]*(self.dy+self.by+1) # clean slates an array of the number of rows in the representation
        horizBorder = "+" + ("-"*self.sx + "+") * self.bx
        numBorders=0 # number of horizBorders in the count so far
        for r in range(len(ans)):
            if r % (self.sy+1) == 0:
                ans[r]=horizBorder
                numBorders+=1
            else:
                #real row is current printed row, minus the number of extra horizBorder rows already printed
                y=r-numBorders
                # for each groups, we break the group into segments [x:x+self.sx] for each row in a box
                # then convert to a string (or a space if None, which means unspecified) which is the map lambda part
                # then join the strings together
                groups=["".join(map(lambda x: str(x) if x is not None else " ",grid[y][x:x+self.sx])) for x in range(0,len(grid[y]),self.sx)]
                # then join the groups with column separators (|) with more column separators on the outside
                ans[r]="|"+("|".join(groups))+"|"
        return ans
                

    def totalRandomizeGivens(self):
        random.seed()
        for y in range(len(self.givens)):
            for x in range(len(self.givens[y])):
                self.givens[y][x] = random.randrange(0,self.sx*self.sy+1)
                if self.givens[y][x]==0:
                    self.givens[y][x]=None
