

xpos=0
ypos=0
xVers=+1
yVers=+1
rag=50
xrac=0

def setup ():
    global xpos, ypos
    xpos=10
    ypos=100
    size(900,600)
    background(255)
    
def draw():
    global xpos,ypos,xVers,yVers,rag, xrac
    background(255)
    ellipse(xpos,ypos,rag,rag)
    xpos=xpos+xVers*4
    ypos=ypos+yVers*4
    
    if xpos >width or xpos<0:
        xVers=xVers*(-1)
        a=random(0,255)
        b=random(0,255)
        c=random(0,255)
        fill(a,b,c)
        rag=rag+20
        ellipse(xpos, ypos, rag, rag)

    if ypos >height or ypos<0:
        yVers=yVers*(-1)
        a=random(0,255)
        b=random(0,255)
        c=random(0,255)
        fill(a,b,c)
        rag=rag-20
        ellipse(xpos, ypos, rag, rag)
    rect(xrac,575,100,25)
    if ypos > height-rag/2:
        print("hai perso")
    if ypos > height-(25+rag) and xrac < xpos < xrac+100:
        yVers=yVers*(-1)
    
    
    
def keyPressed():
    global xpos,ypos,xVers,yVers,rag, xrac
    print("premuto")
    if keyCode==LEFT:
        xrac=xrac-20
    if keyCode==RIGHT:
        xrac=xrac+20
