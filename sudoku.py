import random

# TODO:
# 1. How do I define an alphabet for allowed entries in cells?
# 2. What are the most basic restrictions for sudoku like puzzles? (get more general)
# 3. Automatically solving a puzzle brute force
# 4. Automatically designing a puzzle that has exactly one solution.
# 5. Tailoring a puzzle so that it can solve with only given strategies
# 6. Speed up puzzle generation using all cores of CPU
# 7. Speed up puzzle generation using all cores of GPU
# 8. Come up with more interesting puzzle restrictions.
# 9. Develop a way to generate strategies automatically (ML needed for this?)


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
        self.notSameAs = [[[] for _ in range(self.dx)] for _ in range(self.dy)] #restrictions of squares forced to have different values

        self.setLimits()

    def cleanProblem(self): 


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
                
    def setLimits(self):
        for y in range(len(self.givens)):
            for x in range(len(self.givens[y])):
                fullListRestrict = []
                #restrict rows
                #restrict columns
                #restrict boxes

    def totalRandomizeGivens(self):
        random.seed()
        for y in range(len(self.givens)):
            for x in range(len(self.givens[y])):
                self.givens[y][x] = random.randrange(0,self.sx*self.sy+1)
                if self.givens[y][x]==0:
                    self.givens[y][x]=None


