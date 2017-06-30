import pygame
import pygame.mixer_music
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, file_name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file_name).convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y


    def render(self, screen, file_name):
        ship = pygame.image.load(file_name).convert_alpha()
        screen.blit(ship, (self.x, self.y))




# class X_Wing(Spaceship):
#     def ship(self, ship_type):
#         xwing = pygame.image.load("new-xwing.png").convert_alpha()

# class Tie_Fighter(Spaceship):
#     def ship(self, ship_type):
#         enemy_tie_fighter = pygame.image.load("TieFighter-icon.png").convert_alpha()
        

def main():
    width = 650
    height = 650
    # background_music = pygame.mixer.Sound("Fighter Captured (Galaga Remix) - Joe Monday.mp3")


    pygame.init()
    KEY_UP = 273
    KEY_DOWN = 274
    KEY_LEFT = 276
    KEY_RIGHT = 275
    screen = pygame.display.set_mode((650, 650))
    pygame.display.set_caption('My Game')

    pygame.mixer.music.load("Fighter Captured (Galaga Remix) - Joe Monday.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    
    clock = pygame.time.Clock()
    background = pygame.image.load("Starfield.jpeg").convert_alpha()

    xwing = pygame.image.load("new-xwing.png").convert_alpha()
    xwing = Spaceship(290, 570, "new-xwing.png")

    enemy_tie_fighter = pygame.image.load("TieFighter-icon.png").convert_alpha()
    enemy_tie_fighter1 = Spaceship(90, 0, "TieFighter-icon.png")
    enemy_tie_fighter2 = Spaceship(290, 0, "TieFighter-icon.png")
    enemy_tie_fighter3 = Spaceship(490, 0, "TieFighter-icon.png")
    # Game initialization      

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            # Event handling
            #sound
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     sound.play()
            #spaceship movement
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_DOWN:
                    xwing.speed_y = 6
                elif event.key == KEY_UP:
                    xwing.speed_y = -6
                elif event.key == KEY_LEFT:
                    xwing.speed_x = -6
                elif event.key == KEY_RIGHT:
                    xwing.speed_x = 6
            if event.type == pygame.KEYUP:
                if event.key == KEY_DOWN:
                    xwing.speed_y = 0
                elif event.key == KEY_UP:
                    xwing.speed_y = 0
                elif event.key == KEY_LEFT:
                    xwing.speed_x = 0
                elif event.key == KEY_RIGHT:
                    xwing.speed_x = 0
            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        xwing.update()

        enemy_tie_fighter1.speed_y += .0075
        enemy_tie_fighter1.update()
        if enemy_tie_fighter1.y > 650:
            enemy_tie_fighter1 = Spaceship(90, 0, "TieFighter-icon.png")
        enemy_tie_fighter2.speed_y += .0075
        enemy_tie_fighter2.update()
        if enemy_tie_fighter2.y > 650:
            enemy_tie_fighter2 = Spaceship(290, 0, "TieFighter-icon.png")
        enemy_tie_fighter3.speed_y += .0075
        enemy_tie_fighter3.update()
        if enemy_tie_fighter3.y > 650:
             enemy_tie_fighter3 = Spaceship(490, 0, "TieFighter-icon.png")
            


        # Draw background
        screen.blit(background, (0,0))

        # Game display
        # background_music.play()
        xwing.render(screen, "new-xwing.png")
        enemy_tie_fighter1.render(screen, "TieFighter-icon.png")
        enemy_tie_fighter2.render(screen, "TieFighter-icon.png")
        enemy_tie_fighter3.render(screen, "TieFighter-icon.png")

        font = pygame.font.Font("Xcelsion Italic.ttf", 20)
        text = font.render('Use arrow keys to fly your ship', True, (250, 250, 250))
        screen.blit(text, (50, 150))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
