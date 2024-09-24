# -*- coding: utf-8 -*-
"""Project CSE423_Tic_tac.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zWEg0NPDetaN8pnXx6LsFFU99jfScDee
"""

!pip install -q numpy>=1.2.1

!pip install --quiet lucid>=0.2.3

import numpy as np

import ctypes.util
from lucid.misc.gl.glcontext import create_opengl_context

# Now it's safe to import OpenGL and EGL functions
import OpenGL.GL as gl
from OpenGL.GLU import *

# create_opengl_context() creates GL context that is attached to an
# offscreen surface of specified size. Note that rendering to buffers
# of different size and format is still possible with OpenGL Framebuffers.
#
# Users are expected to directly use EGL calls in case more advanced
# context management is required.
WIDTH, HEIGHT = 800,600
create_opengl_context((WIDTH, HEIGHT))

# OpenGL context is available here.

print(gl.glGetString(gl.GL_VERSION))
print(gl.glGetString(gl.GL_VENDOR))
#print(gl.glGetString(gl.GL_EXTENSIONS))

# Let's render something!
gl.glClear(gl.GL_COLOR_BUFFER_BIT)

from IPython.display import display
from PIL import Image

#from typing_extensions import ParamSpecKwargs
gl.glClear(gl.GL_COLOR_BUFFER_BIT)
# Let's render something!
#MidPint Line Algo ===========================================
import random
def ownVertex(x,y):
  gl.glVertex2f(x/(WIDTH/2), y/(HEIGHT/2))
def colorChange(x,y,z):
  gl.glColor3f(x,y,z)
def drawAxis():
  gl.glColor3f(0, 255, 0)
  gl.glPointSize(5)
  gl.glBegin(gl.GL_LINES)
  ownVertex(0,HEIGHT/2)
  ownVertex(0,-HEIGHT/2)
  ownVertex(WIDTH/2,0)
  ownVertex(-WIDTH/2,0)
  gl.glEnd()

def pointDraw_LINE(cordinates_list):
  for item in cordinates_list:
    ordinate,abscissa = item
    ownVertex(ordinate,abscissa)

def midPointAlgo(f_cordinate,s_cordinate):
  cordinates= []
  x_1,y_1 = f_cordinate
  x_2,y_2 = s_cordinate
  dx = x_2 - x_1
  dy = y_2 - y_1
  d_init = 2*dy - dx
  d = d_init
  incrE, incrNE = 2 * dy,2 * (dy - dx)
  temp_x,temp_y = x_1,y_1
  while temp_x<=x_2:
    cordinates.append((temp_x,temp_y))
    # print(temp_x,temp_y)
    if d>=0: #NE
      d += incrNE
      temp_x += 1
      temp_y += 1
    elif d<0:
      d += incrE
      temp_x += 1
  return cordinates


def ZoneCovert(f_cordinate,s_cordinate):
  x_1,y_1 = f_cordinate
  x_2,y_2 = s_cordinate
  dx = x_2 - x_1
  dy = y_2 - y_1
  if abs(dx)>= abs(dy):
    if dx>=0 and dy>=0:
      #zone 0
      return f_cordinate,s_cordinate,0
    elif dx<=0 and dy>=0:
      #zone 3
      return (-x_1,y_1),(-x_2 ,y_2),3
    elif dx<=0 and dy<=0:
      #zone 4
      return (-x_1,-y_1),(-x_2 ,-y_2),4
    elif dx>=0 and dy<=0:
      #zone 7
      return (x_1,-y_1),(x_2 ,-y_2),7
  elif abs(dx)<= abs(dy):
    if dx>=0 and dy>=0:#zone1
      return (y_1,x_1),(y_2,x_2),1
    elif dx<=0 and dy>=0:#zone 2
      return (y_1,-x_1),(y_2,-x_2),2
    elif dx<=0 and dy<=0:
      #zone 5
      return (-y_1,-x_1),(-y_2,-x_2),5
    elif dx>=0 and dy<=0:
      #zone 6
      return (-y_1,x_1),(-y_2,x_2),6
def originalZone(cordinates,zone):
  new_cordinates = []
  if zone == 0:
    return cordinates
  elif zone == 1:
    for item in cordinates:
      x,y = item
      new_cordinates.append((y,x))
    return new_cordinates
  elif zone == 2:
    for item in cordinates:
      x,y = item
      new_cordinates.append((-y,x))
    return new_cordinates
  elif zone == 3:
    for item in cordinates:
      x,y = item
      new_cordinates.append((-x,y))
    return new_cordinates
  elif zone == 4:
    for item in cordinates:
      x,y = item
      new_cordinates.append((-x,-y))
    return new_cordinates
  elif zone == 5:
    for item in cordinates:
      x,y = item
      new_cordinates.append((-y,-x))
    return new_cordinates
  elif zone == 6:
    for item in cordinates:
      x,y = item
      new_cordinates.append((y,-x))
    return new_cordinates
  elif zone == 7:
    for item in cordinates:
      x,y = item
      new_cordinates.append((x,-y))
    return new_cordinates

def Draw_point_LINE(p_1,p_2):
  cordinate_1,cordinate_2,zone = ZoneCovert(p_1,p_2)
  cordinates_list = midPointAlgo(cordinate_1,cordinate_2)
  original_cordinates_list=originalZone(cordinates_list,zone)
  pointDraw_LINE(original_cordinates_list)

#MidPint Circle Algo ===========================================

import math
# Let's render something!

# def colorChange(x,y,z):
  # gl.glColor3f(x,y,z)


# gl.glClear(gl.GL_COLOR_BUFFER_BIT)
def pointDraw_CIR(cordinates_list):
  gl.glColor3f(255, 255, 255)
  gl.glPointSize(3)
  gl.glBegin(gl.GL_POINTS)
  for item in cordinates_list:
    ordinate,abscissa = item
    ownVertex(ordinate,abscissa)
  gl.glEnd()

def CircAtorigin(radius):
  d = 1-radius
  x = 0
  y = radius
  cordinates = []
  while x<=y:
    cordinates.append((x,y))
    if d>=0: #SE
      d += 2 * x - 2*y + 5
      x += 1
      y -= 1
    elif d<0:
      d += 2 * x + 5
      x += 1
  return cordinates


def InZone(cordinates,zone):
  # print("Zone:", zone)
  new_cordinates = []
  if zone == 0:
    for item in cordinates:
      x,y = item
      new_cordinates.append((y,x))
  elif zone == 1:
    return cordinates
  elif zone == 2:
    for item in cordinates:
      x,y = item
      new_cordinates.append((-x,y))
    return new_cordinates
  elif zone == 3:
    for item in cordinates:
      x,y = item
      new_cordinates.append((-y,x))
    return new_cordinates
  elif zone == 4:
    for item in cordinates:
      x,y = item
      new_cordinates.append((-y,-x))
    return new_cordinates
  elif zone == 5:
    for item in cordinates:
      x,y = item
      new_cordinates.append((-x,-y))
    return new_cordinates
  elif zone == 6:
    for item in cordinates:
      x,y = item
      new_cordinates.append((x,-y))
    return new_cordinates
  elif zone == 7:
    for item in cordinates:
      x,y = item
      new_cordinates.append((y,-x))
    return new_cordinates


def DrawAllZone(cordinates,h,k):
  for zone in range(8):
    # toPrint=[]
    zone_points = InZone(cordinates,zone)
    pointDraw_CIR(changeOrigin(h,k,zone_points))
def changeOrigin(h,k,points):
  newPoints = []
  for point in points:
    x,y = point
    x+= h
    y+=k
    newPoints.append((x,y))
  return newPoints
def scale_circle(cordinates,factor):
  output= []
  for x,y in cordinates:
    output.append((x*factor,factor*y))
  return output


def digit_draw(digit,erase):
  gl.glPointSize(3)
  gl.glBegin(gl.GL_POINTS)
  if erase == 1:
    colorChange(0,0,0)
  else:
    colorChange(255,255,255)
  if digit==1:
    oneA = (0,90+60+60)
    oneB = (0,90+60)
    Draw_point_LINE(oneA,oneB)
  elif digit == 2:
    oneA = (180-20,90+140)
    oneA_six = (180-20,(90+70))
    oneB = (180-20,90+70)
    oneB_six = (180-20,(90+70+35))
    zeroA = (180+20,90+140)
    # zeroA_one = (180+20,90+140)
    zeroB = (180+20,90+70)
    zeroB_one = (180+20,(90+70)+35)
    Draw_point_LINE(oneA_six,oneB_six) # six
    Draw_point_LINE(zeroA,zeroB_one) # one
    Draw_point_LINE(zeroB_one,oneB_six) # two
    Draw_point_LINE(zeroA,oneA) # Zero
    Draw_point_LINE(zeroB,oneB) # Five
  elif digit == 3:
    left_five = (-180-20,-35)
    right_five = (-180+20,-35)
    left_two = (-180-20,0)
    right_two = (-180+20,0)
    left_zero = (-180-20,+35)
    right_zero = (-180+20,35)
    Draw_point_LINE(left_five,right_five) # Five
    Draw_point_LINE(left_two,right_two) # two
    Draw_point_LINE(left_zero,right_zero) # zero
    Draw_point_LINE(right_zero,right_five) # one and four
  elif digit == 4:
    up_three = (-20,35)
    down_three = (-20,0)
    Draw_point_LINE(up_three,down_three) # three
    Draw_point_LINE((-20,0),(20,0)) # two
    Draw_point_LINE((20,35),(20,0)) # one
    Draw_point_LINE((20,-35),(20,0)) # four
  elif digit == 5:
    up_three = (180-20,35)
    down_three = (180-20,0)
    Draw_point_LINE(up_three,down_three) # three
    Draw_point_LINE((180-20,0),(180+20,0)) # two
    Draw_point_LINE((180-20,35),(180+20,35)) # three
    # Draw_point_LINE((180+20,35),(180+20,0)) # one
    Draw_point_LINE((180+20,-35),(180+20,0)) # four
    Draw_point_LINE((180+20,-35),(180-20,-35)) # four

  elif digit == 6:
    up_three = (-20-180,35-180)
    down_three = (-20-180,-180)
    Draw_point_LINE(up_three,down_three) # three
    Draw_point_LINE((-20-180,-180+35),(20-180,-180+35)) # zero
    Draw_point_LINE((-20-180,-180),(20-180,-180)) # two
    Draw_point_LINE((-20-180,-180-35),(20-180,-180-35)) # five
    Draw_point_LINE((-20-180,-180-35),down_three) # six

    # Draw_point_LINE((20-180,35-180),(20-180,-180)) # one
    Draw_point_LINE((20-180,-35-180),(20-180,-180)) # four
  elif digit == 7:
    up_three = (-20,35-180)
    down_three = (-20,-180)
    # Draw_point_LINE(up_three,down_three) # three
    Draw_point_LINE((-20,-180+35),(20,-180+35)) # zero
    Draw_point_LINE((20,35-180),(20,-180)) # one
    Draw_point_LINE((20,-35-180),(20,-180)) # four
  elif digit == 8:
    up_three = (-20+180,35-180)
    down_three = (-20+180,-180)
    Draw_point_LINE(up_three,down_three) # three
    Draw_point_LINE((-20+180,-180+35),(20+180,-180+35)) # zero
    Draw_point_LINE((-20+180,-180),(20+180,-180)) # two
    Draw_point_LINE((-20+180,-180-35),(20+180,-180-35)) # five
    Draw_point_LINE((-20+180,-180-35),down_three) # six

    Draw_point_LINE((20+180,35-180),(20+180,-180)) # one
    Draw_point_LINE((20+180,-35-180),(20+180,-180)) # four
  elif digit == 0:
    oneA = (-180-20,90+140)
    oneB = (-180-20,90+70)
    zeroA = (-180+20,90+140)
    zeroB = (-180+20,90+70)
    Draw_point_LINE(oneA,oneB)
    Draw_point_LINE(zeroA,zeroB)
    Draw_point_LINE(zeroA,oneA)
    Draw_point_LINE(zeroB,oneB)


  gl.glEnd()


def start_game():
  gl.glPointSize(3)
  gl.glBegin(gl.GL_POINTS)
  colorChange(255,255,255)
  A = (-270,270)
  B = (270,270)
  C = (-270,-270)
  D = (270,-270)
  Draw_point_LINE(A,B)
  Draw_point_LINE(A,C)
  Draw_point_LINE(C,D)
  Draw_point_LINE(B,D)

  Draw_point_LINE((-270,270-180),(270,270-180))
  Draw_point_LINE((-270,270-180-180),(270,270-180-180))

  Draw_point_LINE((-270+180,270),(-270+180,-270))
  Draw_point_LINE((-270+180+180,270),(-270+180+180,-270))
  gl.glEnd()
  digit_draw(0,0)
  digit_draw(1,0)
  digit_draw(2,0)
  digit_draw(3,0)
  digit_draw(4,0)
  digit_draw(5,0)
  digit_draw(6,0)
  digit_draw(7,0)
  digit_draw(8,0)
  img_buf = gl.glReadPixelsub(0, 0, WIDTH, HEIGHT, gl.GL_RGB, gl.GL_UNSIGNED_BYTE)
  img = np.frombuffer(img_buf,np.uint8).reshape(HEIGHT, WIDTH, 3)[::-1]
  display(Image.fromarray(img,'RGB'))





User_x = []
User_o = []
booked = []
count = 0
print("Tossing....")
toss = random.randint(1,2)
if toss == 1:
  print("X won the Tossing....")
else:
  print("O won the Tossing....")

start_game()
zone1_points=CircAtorigin(150) # making a circle
def refresh_board():
  img_buf = gl.glReadPixelsub(0, 0, WIDTH, HEIGHT, gl.GL_RGB, gl.GL_UNSIGNED_BYTE)
  img = np.frombuffer(img_buf,np.uint8).reshape(HEIGHT, WIDTH, 3)[::-1]
  display(Image.fromarray(img,'RGB'))
def x_win():
  gl.glPointSize(3)
  gl.glBegin(gl.GL_POINTS)
  colorChange(255,255,255)
  A = (-400,300)
  B = (-400,-300)
  C = (400,-300)
  D = (400,300)
  Draw_point_LINE(A,C)
  Draw_point_LINE(B,D)
  gl.glEnd()
def place_holder_o(box):
  sc = scale_circle(zone1_points,0.5)
  if box==4:
    DrawAllZone(sc,0,0)
  elif box==1:
    DrawAllZone(sc,0,180)
  elif box==0:
    DrawAllZone(sc,-180,180)
  elif box==2:
    DrawAllZone(sc,180,180)
  elif box==7:
    DrawAllZone(sc,0,-180)
  elif box==8:
    DrawAllZone(sc,180,-180)
  elif box==5:
    DrawAllZone(sc,180,0)
  elif box==3:
    DrawAllZone(sc,-180,0)
  elif box==6:
    DrawAllZone(sc,-180,-180)

def place_holder_x(box):
  gl.glPointSize(3)
  gl.glBegin(gl.GL_POINTS)
  colorChange(255,255,255)
  if box == 0:
    A = (-250,250)
    B = (-250,110)
    C = (-110,110)
    D = (-110,250)
    Draw_point_LINE(A,C)
    Draw_point_LINE(B,D)
  elif box == 1:
    A = (-70,250)
    B = (-70,110)
    C = (70,110)
    D = (70,250)
    Draw_point_LINE(A,C)
    Draw_point_LINE(B,D)
  elif box == 2:
    A = (110,250)
    B = (110,110)
    C = (250,110)
    D = (250,250)
    Draw_point_LINE(A,C)
    Draw_point_LINE(B,D)
  elif box == 3:
    A = (-250,70)
    B = (-250,-70)
    C = (-110,-70)
    D = (-110,70)
    Draw_point_LINE(A,C)
    Draw_point_LINE(B,D)
  elif box == 4:
    A = (-70,70)
    B = (-70,-70)
    C = (70,-70)
    D = (70,70)
    Draw_point_LINE(A,C)
    Draw_point_LINE(B,D)
  elif box == 5:
    A = (110,70)
    B = (250,70)
    C = (250,-70)
    D = (110,-70)
    Draw_point_LINE(A,C)
    Draw_point_LINE(B,D)
  elif box == 6:
    A = (-250,-110)
    B = (-250,-250)
    C = (-110,-250)
    D = (-110,-110)
    Draw_point_LINE(A,C)
    Draw_point_LINE(B,D)
  elif box == 7:
    A = (-70,-110)
    B = (-70,-250)
    C = (70,-250)
    D = (70,-110)
    Draw_point_LINE(A,C)
    Draw_point_LINE(B,D)
  elif box == 8:
    A = (110,-110)
    B = (250,-110)
    C = (250,-250)
    D = (110,-250)
    Draw_point_LINE(A,C)
    Draw_point_LINE(B,D)
  gl.glEnd()
def o_win():
  DrawAllZone(zone1_points,0,0)

def Connect(points):
  gl.glPointSize(3)
  gl.glBegin(gl.GL_POINTS)
  colorChange(255,255,255)
  p_1,p_2 = points
  Draw_point_LINE(p_1,p_2)
  gl.glEnd()
# drawAxis()
winner = {(0,1,2) : ((-250,180),(250,180)), (3,4,5):((-250,0),(250,0)), (6,7,8):((-250,-180),(250,-180)), (0,3,6) : ((-180,250),(-180,-250)), (1,4,7) : ((0,250),(0,-250)), (2,5,8) : ((180,250),(180,-250)), (0,4,8) : ((-180,180),(180,-180)) , (2,4,6):((180,180),(-180,-180))}
#winner = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
win = 0
while count!= 9:
  if toss == 1:
    print("X is Playing....")
    x=int(input("Enter your box no (0-8): "))
    flag = 0
    if 8>=x>=0 and x not in booked:
      pass
    else:
      flag = 1
    while (flag==1):
      x=int(("Error!!! Booked or Wrong value!!! Enter your box no (0-8): "))
      if 8>=x>=0 and x not in booked:
        break
    if 8>=x>=0:
      count+=1
      booked.append(x)
      User_x.append(x)
    digit_draw(x,1)
    place_holder_x(x)
    refresh_board()
    for item in winner.keys():
        a,b,c = item
        if a in User_x and b in User_x and c in User_x:
          Connect(winner[item])
          refresh_board()
          print("X is Winner.")
          gl.glClear(gl.GL_COLOR_BUFFER_BIT)
          x_win()
          refresh_board()
          win = 1
          break
    if win == 1:
      break

    print("O is Playing....")
    o = int(input("Enter your box no (0-8): "))

    flag_o = 0
    if 8>=o>=0 and o not in booked:
      pass
    else:
      flag_o = 1
    while (flag_o==1):
      o=int(input("Booked or Wrong value!!! Enter your box no (0-8): "))
      if 8>=o>=0 and o not in booked:
        break
    if 8>=o>=0:
      count+=1
      booked.append(o)
      User_o.append(o)
    digit_draw(o,1)
    place_holder_o(o)
    refresh_board()
    for item in winner.keys():
      a,b,c = item
      if a in User_o and b in User_o and c in User_o:
        Connect(winner[item])
        refresh_board()
        print("O is Winner.")
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        o_win()
        refresh_board()
        win = 1
        break

  else:
    print("O is Playing....")
    o = int(input("Enter your box no (0-8): "))
    flag_o = 0
    if 8>=o>=0 and o not in booked:
      pass
    else:
      flag_o = 1
    while (flag_o==1):
      o=int(input("Booked or Wrong value!!! Enter your box no (0-8): "))
      if 8>=o>=0 and o not in booked:
        break
    if 8>=o>=0:
      count+=1
      booked.append(o)
      User_o.append(o)
    digit_draw(o,1)
    place_holder_o(o)
    refresh_board()
    for item in winner.keys():
      a,b,c = item
      if a in User_o and b in User_o and c in User_o:
        Connect(winner[item])
        refresh_board()
        print("O is Winner.")
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        o_win()
        refresh_board()
        win = 1
        break
    if win == 1:
      break

    print("X is Playing....")
    x=int(input("Enter your box no (0-8): "))
    flag = 0
    if 8>=x>=0 and x not in booked:
      pass
    else:
      flag = 1
    while (flag==1):
      x=int(input("Error!!! Booked or Wrong value!!! Enter your box no (0-8): "))
      if 8>=x>=0 and x not in booked:
        break
    if 8>=x>=0:
      count+=1
      booked.append(x)
      User_x.append(x)
    digit_draw(x,1)
    place_holder_x(x)
    refresh_board()
    for item in winner.keys():
      a,b,c = item
      if a in User_x and b in User_x and c in User_x:
        Connect(winner[item])
        refresh_board()
        print("X is Winner.")
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        x_win()
        refresh_board()
        #winnner[item]
        win = 1
        break
  if win == 1:
    break












# refresh_board()