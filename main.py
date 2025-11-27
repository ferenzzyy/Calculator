# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 400))
app_name = "Pygame Calc(Short For calculator)"
pygame.display.set_caption(app_name)
clock = pygame.time.Clock()
running = True
dt = 0
font = pygame.font.SysFont('Arial',40)

result = 0
num1 = 0
num2 = 0
num1str = ""
num2str = ""


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
                # print(f"{self.btn_txt} Clicked")
                return True
        
no_btn_data = [
    {"number" : 1, "position" : pygame.Vector2(55, 200)},
    {"number" : 2, "position" : pygame.Vector2(160, 200)},
    {"number" : 3, "position" : pygame.Vector2(265, 200)},
    {"number" : 4, "position" : pygame.Vector2(55, 255)},
    {"number" : 5, "position" : pygame.Vector2(160, 255)},
    {"number" : 6, "position" : pygame.Vector2(265, 255)},
    {"number" : 7, "position" : pygame.Vector2(55, 310)},
    {"number" : 8, "position" : pygame.Vector2(160, 310)},
    {"number" : 9, "position" : pygame.Vector2(265, 310)}
]

operator_btn_data = [
    {"number" : "+", "position" : pygame.Vector2(370, 200)},
    {"number" : "-", "position" : pygame.Vector2(370, 255)}
    # {"number" : "=", "position" : pygame.Vector2(370, 310)}
]

# Creates a list of buttons for the numbers 
# uses the values given from the data 
# for each piece of data it creates a new button class
number_btns = [Button(str(data["number"]), "white", 100, 50, data["position"].x, data["position"].y) for data in no_btn_data]

operator_btn = [Button(str(data["number"]), "white", 100, 50, data["position"].x, data["position"].y) for data in operator_btn_data]

equals_btn = Button("=", "white", 100, 50, 370, 310)


can_dial_number1 = True
can_dial_number2 = False
addition = False
subtraction = False
value = 0

while running:
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos(desktop=False)[0], pygame.mouse.get_pos(desktop=False)[1])
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen_txt_surface = font.render(str(value), True, "white")
    screen_txt_rect = screen_txt_surface.get_rect()
    screen_txt_rect.center = pygame.Vector2(265,145) 

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    screen.blit(screen_txt_surface, screen_txt_rect)
    equals_btn.DrawButton()
    # print(can_dial_number1, can_dial_number2)

    # Renders Number Buttons
    for item in number_btns:
        item.DrawButton()
        if can_dial_number1:
            if item.Clicking() and isinstance(int(item.btn_txt), int) :
                # can_dial_number1 = False
                
                num1str = f"{num1str}{item.btn_txt}"
                num1 = int(num1str)
                value = f"{num1}"
                print(f"Number 1: {num1}")
                # can_dial_number2 = True
        else:
            if can_dial_number2:
                if item.Clicking() and isinstance(int(item.btn_txt), int):
                    num2str = f"{num2str}{item.btn_txt}"
                    num2 = int(num2str)
                    value = f"{value}{num2}"
                    print(f"Number 2: {num2}")

    if can_dial_number1 == True:
        can_dial_number2 = False
    else:
        can_dial_number2 = True


    # Renders Operator buttons 
    for item in operator_btn:
        item.DrawButton()
        if item.Clicking():
            can_dial_number1 = False
            match (item.btn_txt):
                case ("+"):
                    print("+")
                    value = f"{value} {"+"} "
                    addition = True
                    
                case ("-"):
                    print("-")
                    value = f"{value} {"-"} "
                    subtraction = True
            # end match

    
    if equals_btn.Clicking():
        if addition == True:
            result = num1 + num2
            print(f"The Result is : {result}")
            value = f"{value} = {result}"
            addition = False
        if subtraction:
            result = num1 - num2
            value = f"{value} = {result}"
            print(f"The Result is : {result}")
            subtraction = False
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
