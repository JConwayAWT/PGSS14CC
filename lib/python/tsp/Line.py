
def linesIntersect(self,c1,c2,c3,c4):
    if c2.x==c1.x:
      m1=float("inf")
    else:
      m1 = (c2.y-c1.y)/(c2.x-c1.x)
    if c4.x==c3.x:
      m2=float("inf")
    else:
      m2 = (c4.y-c3.y)/(c4.x-c3.x)
    if m2==m1:
      return False
    else:
      x = (m1*c1.x-m2*c3.x-c1.y+c3.y)/(m1-m2) 
      y = m1*(x-c1.x)+c1.y

      if min(x,c1.x,c2.x)!=x and min(x,c3.x,c4.x)!=x:
        if min(y,c1.y,c2.y)!=y and min(y,c3.y,c4.y)!=y:
          return True
      return False
        