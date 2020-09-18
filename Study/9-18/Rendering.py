from pico2d import *
import os

os.chdir('C:\\Users\\hansi\\Desktop\\산기대\\20-2\\2DGP\\Res')

open_canvas()

gra = load_image('grass.png')
cha = load_image('character.png')

x = 0
frame = 0

while(x <800):
    clear_canvas_now()
    gra.draw_now(400, 30)
    cha.draw_now(x, 90)
    x += 2
    
    delay(0.01)
    get_events()

close_canvas()


     


