import pygame
import numpy as np
import matplotlib.pyplot as plt
pygame.init()
size = (640, 480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 10
pygame.display.set_caption("WAVE")
icon = pygame.image.load("waves.png")
pygame.display.set_icon(icon)
pygame.font.init()
myfont = pygame.font.SysFont("Comic Sans MS", 20)
x_text = myfont.render("x", True, (0, 0, 0))
y_text = myfont.render("y", True, (0, 0, 0))
data = []
for i in np.arange(1, 7, 0.5):
    fig, ax = plt.subplots()
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    y = np.sin(x+i)
    ax.plot(x, y, color='orange')
    plt.xlim(-2*np.pi, 2*np.pi)
    ax.grid(True)
    ax.axhline(0, color='black', lw=1.5)
    ax.axvline(0, color='black', lw=1.5)
    ax.set_xticks(np.arange(-2*np.pi, 2*np.pi+0.01, np.pi/2))
    ax.set_yticks(np.arange(-1, 1+0.01, 0.5)) 
    x_labels = [f'$-2\pi$', f'$-3\pi/2$', f'$-\pi$', f'$-\pi/2$', '$0$', f'$\pi/2$', f'$\pi$',
    f'$3\pi/2$',  f'$2\pi$']
    ax.set_xticklabels(x_labels)
    xmin, xmax = ax.get_xlim() 
    ymin, ymax = ax.get_ylim()
    hw = 0.04*(ymax-ymin) 
    hl = 0.04*(xmax-xmin)
    yhw = hw/(ymax-ymin)*(xmax-xmin)* 480/640   
    yhl = hl/(xmax-xmin)*(ymax-ymin)* 640/480
    ax.arrow(xmin, 0, xmax-xmin, 0, head_width=hw, head_length=hl, overhang=0.3, length_includes_head= True)
    ax.arrow(0, ymin, 0, ymax-ymin, head_width=yhw, head_length=yhl, overhang=0.3, length_includes_head= True)
    plt.savefig(f"my_figure{i}.png", dpi=100)
    data.append(f"my_figure{i}.png")
g_labels = [f'-360{chr(176)}', f'-270{chr(176)}', f'-180{chr(176)}', f'-90{chr(176)}',
f'0{chr(176)}', f'90{chr(176)}', f'180{chr(176)}', f'270{chr(176)}', f'360{chr(176)}']
font = pygame.font.SysFont("Comic Sans MS", 12)
for j in range(len(g_labels)):
    exec(f'g_{j} = font.render("{g_labels[j]}", True, (255, 0, 0))')
for i in range(len(data)):
    exec(f'wave_{i} = pygame.image.load(data[i])')
running = True
k = 0
while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    k += 1
    k = k%len(data)
    exec(f'screen.blit(wave_{k}, (0,0))')
    screen.blit(x_text, (size[0] - 60, size[1]//2 - 16))
    screen.blit(y_text, (size[0]//2 + 4, 25))
    s = 10
    for j in range(len(g_labels)):
        s += 62
        exec(f'screen.blit(g_{j}, ({s}, 455))')
    pygame.display.flip()
    clock.tick(fps)