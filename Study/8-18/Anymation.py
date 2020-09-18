from pico2d import *
import os

os.chdir('C:\\Users\\hansi\\Desktop\\산기대\\20-2\\2DGP\\Res')

open_canvas()

gra = load_image('grass.png')
cha = load_image('run_animation.png')

x = 0
frame = 0

while(x <800):
    clear_canvas()
    gra.draw(400, 30)
    cha.clip_draw(frame *100, 0, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    x += 5
    
    delay(0.01)
    get_events()

close_canvas()


     


