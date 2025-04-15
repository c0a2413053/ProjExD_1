import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img2, 1, 0)
    pc_img = pg.image.load("fig/3.png")
    pc_img = pg.transform.flip(pc_img, 1, 0)
    pc_rct = pc_img.get_rect()
    pc_rct.center = 300, 200
    tmr = 0
    x = tmr
    pcx = 0
    pcy = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])

        pc_rct.move_ip(-1+pcx, pcy)            
        key_lst = pg.key.get_pressed()  
        if key_lst[pg.K_UP]:
            pcy = -1
        else:
            pcy = 0
        if key_lst[pg.K_DOWN]:
            pcy = 1
        if key_lst[pg.K_LEFT]:
            pcx = -1
        else:
            pcx = 0
        if key_lst[pg.K_RIGHT]:
            pcx = +2
        screen.blit(pc_img, pc_rct)
        pg.display.update()
        tmr += 1
        x += 1        
        clock.tick(200)
        if x >= 3200:
            x = 0


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()