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
result_str = " "
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

    def Clicked(self):
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
clear_all_btn = Button("C", "white", 100, 50, 475, 200)
clear_entry_btn = Button("CE", "white", 100, 50, 475, 255)


first_number = True
addition = False
subtraction = False
results_given = False
value = 0
operator = False
entries=[]
current_entry=[]
display_entries=[""]

def reset_number_list():
    first_number = True
    entries = []
    # entries.clear()

# def addition(numbers):
#     for number in numbers:


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
    clear_all_btn.DrawButton()
    clear_entry_btn.DrawButton()


    if len(entries) == 0:
        first_number = True
        entries=[]

    # Renders Number Buttons
    for item in number_btns:
        item.DrawButton()

        # Takes the FIRST number ever being pressed and puts it into a current entry list
        if not equals_btn.Clicked():
            if item.Clicked() and isinstance(int(item.btn_txt), int) and first_number == True:
                current_entry.append(item.btn_txt)
                first_number = False
                entry = "".join(current_entry)
                display_entries[0] = entry
        
        # After the FIRST EVER number is pressed the rest of the entries is handled here
            elif item.Clicked() and isinstance(int(item.btn_txt), int) and first_number == False:
                if operator == True:

                    current_entry.append(item.btn_txt)
                    entry = "".join(current_entry)
                    display_entries.append(entry)
                    entries = display_entries

                    operator = False

                else:
                    current_entry.append(item.btn_txt)
                    entry = "".join(current_entry)
                    display_entries[len(display_entries) - 1] = entry
                    entries = display_entries       
            result_str = " ".join(entries)


        elif equals_btn.Clicked() and results_given == False:
                
                result_str = " ".join(entries)
                result = eval(result_str)
                
                entries.clear()
                entries.append(str(result))
                result_str = " ".join(entries)
                results_given = True
                print(result)

    # Renders Operator buttons 
    for item in operator_btn:
        item.DrawButton()
        if item.Clicked() and not operator:
            operator = True
            results_given = False
            first_number = False

            current_entry.clear()

            print(entry)

            match (item.btn_txt):
                case ("+"):
                    print("+")
                    display_entries.append(item.btn_txt)
                    entries = display_entries
                    # value = f"{value} {"+"} "
                    # entries += "+"
                    
                case ("-"):
                    print("-")
                    display_entries.append(item.btn_txt)
                    entries = display_entries
                    # value = f"{value} {"-"} "
                    # entries += "-"
            # end match

    if clear_all_btn.Clicked():
        entries.clear()

    if clear_entry_btn.Clicked() and len(entries) != 0:
        entries.pop(len(entries) - 1)
        

    print(display_entries)
    display_entry = " ".join(display_entries)

    value = f"{display_entry}"

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
