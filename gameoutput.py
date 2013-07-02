from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
x=0.0
y=0.0
angle=0.0

def draw(ws_states,ad_states):
     global x,y,angle
     if ws_states != 0:
          x += cos(radians(angle)) * ws_states * 0.5
          y += -sin(radians(angle)) * ws_states * 0.5
     if ad_states != 0:
          angle += ad_states * 3

     glClearColor(0,1,1,1)
     glLoadIdentity()
     camera_position = [x -10 * cos(radians(angle))
                        ,1,y + 10 * sin(radians(angle))]
     camera_vector = [x - camera_position[0],0,y - camera_position[2]]
     gluLookAt(camera_position[0],camera_position[1],camera_position[2],
               camera_position[0] + camera_vector[0] * 10,1,
               camera_position[2] + camera_vector[2] * 10,
               0,1,0)
     glClearDepth(1)
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     glEnable(GL_DEPTH_TEST)
     light()
     teapot()
     drawxyz()
     """glPushMatrix()
     glRotatef(75,0,1,0)
     glTranslatef(1,0,0)
     drawtri()
     glPopMatrix()

     glPushMatrix()
     glTranslatef(1,0,0)


     glRotatef(75,0,1,0)
     drawtri()
     glPopMatrix()

     drawxyz()"""
     
     glDisable(GL_DEPTH_TEST)
     glutSwapBuffers()
    
def drawxyz():
    glBegin(GL_LINES)
    glColor(0,0,0)
    glVertex3f(0,0,0)
    glVertex3f(100,0,0)
    glVertex3f(0,0,0)
    glVertex3f(0,100,0)
    glVertex3f(0,0,0)
    glVertex3f(0,0,100)
    glEnd()

def drawearth():
     glBegin(GL_QUADS)
     glVertex3f(-100,-1.5,-100)
     glVertex3f(-100,-1.5,100)
     glVertex3f(100,-1.5,100)
     glVertex3f(100,-1.5,-100)
     glEnd()

def reshape(w,h):
     glViewport(0,0,w,h)
    
     glMatrixMode(GL_PROJECTION)
     glLoadIdentity()
     gluPerspective(30,float(w)/h,1.0,100)
    
     glMatrixMode(GL_MODELVIEW)


def light():
    lightamb = [0,0,0,1]
    lightdiff = [1,1,1,1]
    lightspe = [1,1,1,1]
    lightpos = [1,1,1,0]

    glLightfv(GL_LIGHT0, GL_AMBIENT, lightamb)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightdiff)
    glLightfv(GL_LIGHT0, GL_SPECULAR, lightspe)

    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)

    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)

def teapot():
     global x,y,angle
     gold_amb = [0.247250, 0.1995, 0.07450, 1.0]
     gold_diff = [0.75164, 0.60648, 0.22648, 1.0]
     gold_spe = [0.628281, 0.555802, 0.366065, 1.0]
     gold_shin = 51.2
     glPushMatrix()
     glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, gold_amb)    
     glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, gold_diff)
     glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, gold_spe)
     glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, gold_shin)
     """glColorMaterial(GL_FRONT_AND_BACK,GL_AMBIENT)
     glColor4fv(gold_amb)
     glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)
     glColor4fv(gold_diff)
     glColorMaterial(GL_FRONT_AND_BACK, GL_SPECULAR)
     glColor4fv(gold_spe)"""
     glTranslatef(x,0.0,y)
     glRotatef(angle,0,1,0)
     glutSolidTeapot(1.0)
     #glDisable(GL_COLOR_MATERIAL)
     glPopMatrix()


     
