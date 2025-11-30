from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# -----------------------------
# Draw X and Y axes
# -----------------------------
def draw_axes():
    glColor3f(1.0, 1.0, 1.0)       # White
    glLineWidth(1)

    glBegin(GL_LINES)
    # X-axis
    glVertex2f(-10, 0)
    glVertex2f(10, 0)

    # Y-axis
    glVertex2f(0, -10)
    glVertex2f(0, 10)
    glEnd()


# -----------------------------
# Draw square
# -----------------------------
def draw_square():
    glColor3f(0.0, 1.0, 0.0)       # Green
    glLineWidth(3)

    glBegin(GL_LINE_LOOP)
    glVertex2f(2, 2)   # bottom-left
    glVertex2f(6, 2)   # bottom-right
    glVertex2f(6, 6)   # top-right
    glVertex2f(2, 6)   # top-left
    glEnd()


# -----------------------------
# Main display function
# -----------------------------
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    draw_axes()
    draw_square()

    glFlush()
    glutSwapBuffers()


# -----------------------------
# Window Reshape
# -----------------------------
def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Orthographic projection
    glOrtho(-10, 10, -10, 10, -1, 1)

    glMatrixMode(GL_MODELVIEW)


# -----------------------------
# GLUT Initialization
# -----------------------------
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow(b"OpenGL Triangle & Axes")

# Background color
glClearColor(0.0, 0.0, 0.0, 1.0)

glEnable(GL_DEPTH_TEST)

glutDisplayFunc(display)
glutReshapeFunc(reshape)

glutMainLoop()
