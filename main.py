import pygame, random

running = True
pygame.init()
screen = pygame.display.set_mode((288, 512))

background_image = pygame.image.load("assets/background-day.png")
base_image = pygame.image.load("assets/base.png")
bird_image = pygame.image.load("assets/bluebird.png")
gameover_image = pygame.image.load("assets/gameover.png")
downpipe_image = pygame.image.load("assets/pipe-green.png")
uppipe_image = pygame.transform.flip(downpipe_image, False, True)

FPS = 60

class Pipe():
    def __init__(self):
        self.x = 300
        self.y = random.randint(-75, 150)

    def drawpipe(self):
        self.x -= 2
        screen.blit(downpipe_image, (self.x, self.y+210))
        screen.blit(uppipe_image, (self.x, self.y-210))

    def collision(self, birdx, birdy):
        tolerance = 7
        bird_side_dx = birdx + bird_image.get_width()-tolerance
        bird_side_sx = birdx + tolerance
        pipe_side_dx = self.x + downpipe_image.get_width()
        pipe_side_sx = self.x
        bird_side_up = birdy + tolerance
        bird_side_down = birdy + bird_image.get_height() - tolerance
        pipe_side_up = self.y + 110
        pipe_side_down = self.y + 210
        if bird_side_dx > pipe_side_sx and bird_side_sx < pipe_side_dx: 
            if bird_side_up < pipe_side_up or bird_side_down > pipe_side_down:
                gameover()

def gameover():
    global birdx, birdy, gravity, basex, start_again
    screen.blit(gameover_image, (50,180))
    pygame.display.update()
    pygame.time.Clock().tick(FPS)
    start_again = False
    while not start_again:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                variable()
                start_again = True
            if event.type == pygame.QUIT:
                pygame.quit()

def base(x):
    global basex
    screen.blit(base_image, (x,400))
    if basex < -45:
        basex = 0

def background():
    screen.blit(background_image, (0,0))

def bird():
    global birdy
    birdy += 1
    screen.blit(bird_image, (60, birdy))

def checkpipeposition():
    if pipes[-1].x < 150:
        pipes.append(Pipe())
    for p in pipes:
        p.collision(birdx, birdy)

def draw():
    background()
    for pipe in pipes:
        pipe.drawpipe()
    base(basex)
    bird()
    checkpipeposition()

def variable():
    global birdx, birdy, gravity, basex, pipe, start_again, pipes
    basex = 0
    start_again = False
    birdx = 60
    birdy = 256
    gravity = 0
    pipe = Pipe()
    pipes = []
    pipes.append(Pipe())

variable()

while running:
    basex -= 1
    gravity += 0.8
    birdy += gravity
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
            gravity = -8
    if birdy >= 380:
        gameover()
    draw()
    pygame.time.Clock().tick(FPS)
    pygame.display.update()
    


