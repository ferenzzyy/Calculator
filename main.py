# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()
running = True
dt = 0
font = pygame.font.SysFont('Arial',40)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

class Button():
    def __init__(self, btn_text, colour, size_x, size_y, pos_x, pos_y):
        self.btn_txt = btn_text
        self.size = pygame.math.Vector2(size_x, size_y)
        self.position = pygame.math.Vector2(pos_x, pos_y)
        self.colour = colour
        self.button_rect = pygame.Rect((640,360),(self.size.x, self.size.y))

    def DrawButton(self):
        self.button_rect.center = self.position
        pygame.draw.rect(screen, self.colour, self.button_rect)
        btn_txt_surface = font.render(self.btn_txt, True, "black")
        btn_txt_rect = btn_txt_surface.get_rect()
        btn_txt_rect.center = self.position
        screen.blit(btn_txt_surface, btn_txt_rect)

    def CheckForMouse(self):
        return self.button_rect.collidepoint(mouse_pos.x, mouse_pos.y)

    def Clicking(self):
            if pygame.mouse.get_just_pressed()[0] and self.CheckForMouse():
                print(f"{self.btn_txt} Clicked")
        
button_data = [
    {"number" : "1", "position" : pygame.Vector2(55, 200)},
    {"number" : "2", "position" : pygame.Vector2(160, 200)},
    {"number" : "3", "position" : pygame.Vector2(265, 200)},
    {"number" : "4", "position" : pygame.Vector2(55, 255)},
    {"number" : "5", "position" : pygame.Vector2(160, 255)},
    {"number" : "4", "position" : pygame.Vector2(265, 255)}
]

# Creates a list of buttons for the numbers 
# uses the values given from the data 
# for each piece of data it creates a new button class
number_btns = [Button(data["number"], "white", 100, 50, data["position"].x, data["position"].y) for data in button_data]






while running:
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos(desktop=False)[0], pygame.mouse.get_pos(desktop=False)[1])
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.MOUSEBUTTONDOWN and number1_btn.CheckForMouse():
        #     print(number1_btn.btn_txt + ' Clicked!')

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    for item in number_btns:
        item.DrawButton()
        item.Clicking()
    


   
    # pygame.draw.circle(screen, "red", player_pos, 40)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     player_pos.y -= 300 * dt
    # if keys[pygame.K_s]:
    #     player_pos.y += 300 * dt
    # if keys[pygame.K_a]:
    #     player_pos.x -= 300 * dt
    # if keys[pygame.K_d]:
    #     player_pos.x += 300 * dt

    # print(player_pos)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
