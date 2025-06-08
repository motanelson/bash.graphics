from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    # Enable lighting
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)  # Enable Light 0
    glEnable(GL_DEPTH_TEST)  # Enable depth testing

    # Set light properties
    light_position = [1.0, 1.0, 1.0, 0.0]  # Directional light
    light_ambient = [0.2, 0.2, 0.2, 1.0]   # Ambient light
    light_diffuse = [0.8, 0.8, 0.8, 1.0]   # Diffuse light
    light_specular = [1.0, 1.0, 1.0, 1.0]  # Specular light

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

    # Set material properties
    material_ambient = [0.7, 0.7, 0.7, 1.0]
    material_diffuse = [0.8, 0.8, 0.8, 1.0]
    material_specular = [1.0, 1.0, 1.0, 1.0]
    material_shininess = [50.0]

    glMaterialfv(GL_FRONT, GL_AMBIENT, material_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, material_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, material_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, material_shininess)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(1.0, 1.0, 4.0,  # Eye position
             0.0, 0.0, 0.0,  # Look-at point
              0.0, 1.0, 0.0)  # Up direction

    # Draw a teapot (or any object)
    glutSolidCone(1.0,1.0,90,30)

    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width) / float(height), 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"OpenGL Lighting Example")
    # Fundo amarelo
    glClearColor(1.0, 1.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()