import pyautogui
import imageio
import pygame
import imageio
import math
import sys
import csv
import os
import time
import pygame
from pygame.locals import *
from tkinter import Tk, filedialog
output_file=""
def escolher_csv():
    global output_file
    root = Tk()
    root.withdraw()
    caminho = filedialog.askopenfilename(
        title="Selecionar ficheiro CSV",
        filetypes=[("Ficheiros txt", "*.txt")]
    )
    output_file=caminho.replace(".txt",".gif")
    root.destroy()
    return caminho

def ler_faces_csv(caminho):
    faces = []
    with open(caminho, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >1:
                
                try:
                    pontos = row
                    faces.append(pontos)
                except ValueError:
                    continue
    return faces

           
def render_gif():
    global output_file
    caminho = escolher_csv()
    if not caminho or not os.path.exists(caminho):
        print("Ficheiro não encontrado.")
        return

    faces = ler_faces_csv(caminho)
    if not faces:
        print("Nenhuma face válida encontrada no ficheiro.")
        return
    
    pygame.init()
    display = (800, 600)
    
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN )
    pygame.display.set_caption("bash")
    
    angulo = 0
    tempo_ultima_rotacao = time.time()
    clock = pygame.time.Clock()


    running = True
    

    
    frames = []
    screen.fill((255, 255, 0))  # RGB color for black
    colors=(0,0,0)
    vars=""
    for face in faces:
        
        
        
        if face[0].strip().lower()=="ret":
            pygame.draw.rect(screen,colors,pygame.Rect(int(face[1].strip()),int(face[2].strip()),int(face[3].strip()),int(face[4].strip())))
        if face[0].strip().lower()=="clear":
            screen.fill((int(face[1].strip()),int(face[2].strip()),int(face[3].strip())))
        if face[0].strip().lower()=="circle":
            pygame.draw.circle(screen,colors,(int(face[1].strip()),int(face[2].strip())),float(face[3].strip()))
        if face[0].strip().lower()=="color":
            colors=((int(face[1].strip()),int(face[2].strip()),int(face[3].strip())))
        clock.tick(60)
        if face[0].strip().lower()=="foto":
            pygame.display.flip()
            
            # Captura da imagem
            screenshot = pyautogui.screenshot()
            frames.append(screenshot)
        if face[0].strip().lower()=="var":
            vars=(str(face[1:]))
        if face[0].strip().lower()=="print":
            font = pygame.font.Font(None, int(36))
            text_surface = font.render(vars, True, colors)
            xy=(int(face[1].strip()),int(face[2].strip()))
            screen.blit(text_surface, xy)
        if face[0].strip().lower()=="sleep":
            pygame.display.flip()
            # Captura da imagem
            screenshot = pyautogui.screenshot()
            frames.append(screenshot)
            xy=int(face[1].strip())
            time.sleep(xy)
            pygame.display.flip()
            # Captura da imagem
            screenshot = pyautogui.screenshot()
            frames.append(screenshot)
        for evento in pygame.event.get():
            if evento.type == QUIT:
                running = False

        # Rotação automática a cada 1.5 segundos
        if time.time() - tempo_ultima_rotacao > 0.1:
            angulo += 1
            tempo_ultima_rotacao = time.time()

        


        
    pygame.display.flip()    
    # Captura da imagem
    screenshot = pyautogui.screenshot()
    frames.append(screenshot)
    # Save frames as a GIF
    screenshot = pyautogui.screenshot()
    frames.append(screenshot)
    # Save frames as a GIF
    frames[0].save(
        output_file,
        save_all=True,
        append_images=frames[1:],
        duration=1000 // 10,
        loop=0
    )

    print(f"GIF salvo em: "+output_file)
    pygame.quit()

print("\033c\033[43;30m\n")
render_gif()
