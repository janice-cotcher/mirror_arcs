def setup():
    size(300, 300)
    arc(50, 50, 80, 80, 0, PI+QUARTER_PI, CHORD)
    # line(100, 0, 100, height)
    arc(150, 50, 80, 80, -QUARTER_PI, PI, CHORD)
    # line(0, 50, width, 50)
    # line(0, 20, width, 20)

def draw():
    print(mouseX, mouseY)
