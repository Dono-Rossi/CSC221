from gasp import *
begin_graphics()
ball_x = 5
ball_y = 5


def place_ball():
    global ball_x, ball_y, c
    c = Circle((ball_x + 8, ball_y + 6), 5, filled=True)
def move_ball():
    global ball_x, ball_y, c
    print("I'm moving...")
    update_when('key_pressed')

place_ball()

while ball_x <= 635:
    move_by(c, 4, 3)
    sleep(0.02)
    update_when('key_pressed')
else: 
    remove_from_screen(c)
    
end_graphics()
