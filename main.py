import pygame, random
import sys
from pygame import Vector2

pygame.init()
WIDTH = 700
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update,150)
game_font = pygame.font.Font(None,50)

GAP = 200  # The vertical gap between top and bottom blocks
bird_image = pygame.image.load('bird.png')
bird = pygame.transform.scale(bird_image,(60,60))
pipe_down_image = pygame.image.load('pipe_down.png')
pipe_up_image = pygame.transform.flip(pipe_down_image,False,True)
class BIRD:
    def __init__(self):
        self.pos = Vector2(50,HEIGHT/2)

    def draw_bird(self):
        bird_rect = pygame.Rect(self.pos.x,self.pos.y,50,50)
        screen.blit(bird,bird_rect)
    def fall_bird(self):
        self.pos -= Vector2(0,-4)

    def jump_bird(self):
        self.pos += Vector2(0,-100)

    def get_rect(self):
        return pygame.Rect(self.pos.x,self.pos.y,50,50)


class BLOCK:
    last_top_height = None  # Class variable to share top height between top and bottom blocks

    def __init__(self, x: int, y: int, height: int, width: int):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.pos = Vector2(self.x, self.y)
        self.speed = 5

    def draw_block(self):
        block_rect = pygame.Rect(self.pos.x,self.pos.y,self.width,self.height)
        pygame.draw.rect(screen,(198,108,116),block_rect)

    def draw_down_block(self):
        block_rect = pygame.Rect(self.pos.x,self.pos.y,self.width,self.height)
        screen.blit(pipe_down_image,block_rect)

    def draw_up_block(self):
        block_rect = pygame.Rect(self.pos.x,self.pos.y,self.width,self.height)
        screen.blit(pipe_up_image,block_rect)

    def move_block(self):
        self.pos += Vector2(-self.speed,0)
        # If block is fully off the left side of the screen, reset it
        if self.pos.x <= 0 - self.width:
            if self.y == 0:
                # This is a top block
                top_height = random.randint(HEIGHT//10, HEIGHT//2)
                self.height = top_height
                self.pos = Vector2(WIDTH,0)
                BLOCK.last_top_height = top_height

            else:
                # This is a bottom block
                # Use the last top height stored by the top block to create a gap
                if BLOCK.last_top_height is None:
                    # If no top block has reset yet, just randomize normally
                    BLOCK.last_top_height = random.randint(HEIGHT//10, HEIGHT//2)
                bottom_height = HEIGHT - BLOCK.last_top_height - GAP
                self.height = bottom_height
                self.pos = Vector2(WIDTH, HEIGHT - bottom_height//1.6)

    def get_pos(self):
        return self.pos

    def get_rect(self):
        return pygame.Rect(self.pos.x,self.pos.y,self.width,self.height)


block_height = random.randint(HEIGHT//10, HEIGHT//2)
block_height2 = random.randint(HEIGHT//4, HEIGHT)

class MAIN:
    def __init__(self):
        self.top_block = BLOCK(WIDTH,0,block_height,60)
        self.top_block_2 = BLOCK(WIDTH+350,0,block_height,60)
        self.buttom_block = BLOCK(WIDTH,HEIGHT - block_height2//4,block_height2,60)
        self.buttom_block_2 = BLOCK(WIDTH+350,HEIGHT - block_height2//2,block_height2,60 )
        self.bird = BIRD()
        self.score = 0

    def update(self):
        self.top_block.move_block()
        self.top_block.draw_up_block()
        self.buttom_block.move_block()
        self.buttom_block.draw_down_block()
        self.top_block_2.move_block()
        self.top_block_2.draw_up_block()
        self.buttom_block_2.move_block()
        self.buttom_block_2.draw_down_block()
        self.bird.draw_bird()
        self.bird.fall_bird()
        main.score_update()
        main.draw_score()

    def check_collision(self):
        bird_rect = self.bird.get_rect()
        if (bird_rect.colliderect(self.top_block.get_rect()) or
                bird_rect.colliderect(self.buttom_block.get_rect()) or
                bird_rect.colliderect(self.top_block_2.get_rect()) or
                bird_rect.colliderect(self.buttom_block_2.get_rect())):
            return True
        return False

    def score_update(self):
        if self.top_block.get_pos().x == 0 or self.top_block_2.get_pos().x == 0:
            self.score += 1
            print(self.score)

    def draw_score(self):
        score_surface = game_font.render(str(self.score),True,(56,74,12))
        score_rect = score_surface.get_rect(center = (20,20))
        screen.blit(score_surface,score_rect)

    def game_over(self):
        print("over")
        game_over_surface = game_font.render('Game Over, Press SPACE to play again',True,(56,74,12))
        game_over_rect = game_over_surface.get_rect(center = (WIDTH/2,HEIGHT/2))
        screen.blit(game_over_surface,game_over_rect)

main = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                main.bird.jump_bird()
    if main.check_collision():
        main.game_over()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                main = MAIN()
            else :
                pygame.quit()
                sys.exit()

    screen.fill((175,215,70))
    main.update()

    pygame.display.update()
    clock.tick(60)
