
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

# ====== CONFIG ======
GRID_SIZE = 5
CELL_SIZE = 0.3
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# Goal position
goal_pos = (4, 3)

# Define path (you can replace this with a real policy path)
agent_path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3)]

# Therapy labels
therapy_labels = {
    (0, 0): ("Journaling", (0.5, 0.8, 1.0)),
    (1, 2): ("Breathing", (0.7, 0.9, 1.0)),
    (3, 1): ("Chatbot", (0.8, 0.6, 1.0)),
    (2, 4): ("CBT", (0.5, 1.0, 0.9)),
    (4, 3): ("Crisis", (1.0, 0.4, 0.4))
}

# Agent simulation state
current_step = 0

def draw_grid():
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if (x, y) in therapy_labels:
                _, color = therapy_labels[(x, y)]
                glColor3f(*color)
            else:
                glColor3f(0.9, 0.9, 0.9)

            glBegin(GL_QUADS)
            glVertex2f(x * CELL_SIZE, y * CELL_SIZE)
            glVertex2f((x + 1) * CELL_SIZE, y * CELL_SIZE)
            glVertex2f((x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE)
            glVertex2f(x * CELL_SIZE, (y + 1) * CELL_SIZE)
            glEnd()

            glColor3f(0.2, 0.2, 0.2)
            glBegin(GL_LINE_LOOP)
            glVertex2f(x * CELL_SIZE, y * CELL_SIZE)
            glVertex2f((x + 1) * CELL_SIZE, y * CELL_SIZE)
            glVertex2f((x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE)
            glVertex2f(x * CELL_SIZE, (y + 1) * CELL_SIZE)
            glEnd()

def draw_labels():
    glColor3f(0, 0, 0)
    for (x, y), (label, _) in therapy_labels.items():
        glRasterPos2f(x * CELL_SIZE + 0.05, y * CELL_SIZE + 0.12)
        for ch in label:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch))

def draw_agent():
    global current_step
    if current_step >= len(agent_path):
        return

    x, y = agent_path[current_step]
    glColor3f(0.0, 1.0, 0.0)
    margin = 0.05
    glBegin(GL_QUADS)
    glVertex2f(x * CELL_SIZE + margin, y * CELL_SIZE + margin)
    glVertex2f((x + 1) * CELL_SIZE - margin, y * CELL_SIZE + margin)
    glVertex2f((x + 1) * CELL_SIZE - margin, (y + 1) * CELL_SIZE - margin)
    glVertex2f(x * CELL_SIZE + margin, (y + 1) * CELL_SIZE - margin)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    draw_grid()
    draw_labels()
    draw_agent()
    glutSwapBuffers()

def update(value):
    global current_step
    current_step += 1
    if current_step < len(agent_path):
        glutPostRedisplay()
        glutTimerFunc(700, update, 0)
    else:
        print("✅ Simulation complete")

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, GRID_SIZE * CELL_SIZE, 0.0, GRID_SIZE * CELL_SIZE)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Therapy Grid Agent Simulation")
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(500, update, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
