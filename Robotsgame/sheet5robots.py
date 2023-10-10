from gasp import*
begin_graphics()
finished = False
player_x = 1
player_y = 1


def place_player():
    global player_x, player_y, c
    c = Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)
    print("Here I am!")

def move_player():
    global player_x, player_y, c
    print("I'm moving...")
    update_when('key_pressed')

place_player()

while not finished:
    move_player()

end_graphics()
