#Snake Game
import time,pygame,random
from itertools import combinations

#Initialization
pygame.init()
score = 0
game = True
v = 0.1
times = 0
score_list = []
current_key = "S"
colors = ["blue","orange"]

def write(text, font, x, y, size, col, screen): #Shortcut function for writing text onto the screen.
    font = pygame.font.Font(f"{font}", size)
    text_ = font.render(f"{text}", True, col)
    screen.blit(text_, (x, y))

def snake_game(): #Main function.
    global game,times,score,v,score_list,current_key
    running = True
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Snake Game")
    apple = pygame.Rect(30,30,30,30)
    rect = pygame.Rect(30,30,30,30)

    rect.x = 300
    rect.y = 300

    apple.x = random.randint(40,570)
    apple.y = random.randint(40,570)
    snake = [rect] #Snake is defined as an array object.

    def reset():
        global score, game, v, current_key
        score = 0
        game = True
        v = 0.1
        current_key = "S"

    def c_cc(): #Changing the current key function.
        global current_key

        if game:
            if key[pygame.K_LEFT]:
                if current_key == "D":
                    pass
                else:
                    current_key = "A"
            elif key[pygame.K_RIGHT]:
                if current_key == "A":
                    pass
                else:
                    current_key = "D"
            elif key[pygame.K_DOWN]:
                if current_key == "W":
                    pass
                else:
                    current_key = "S"
            elif key[pygame.K_UP]:
                if current_key == "S":
                    pass
                else:
                    current_key = "W"

    def grow():
        #It simply adds a rectangle to the main Snake object.
        new_rect = pygame.Rect(30,30,30,30)
        snake.append(new_rect)

    def move(key_): #Main move function.
        if game:
            if key_ == "A":
                rect.x -= 30
                time.sleep(v)
            elif key_ == "S":
                rect.y += 30
                time.sleep(v)
            elif key_ == "D":
                rect.x += 30
                time.sleep(v)
            elif key_ == "W":
                rect.y -= 30
                time.sleep(v)

    def draw(): #Function for drawing the snake.
        a = True

        for i in snake:
            if a:
                pygame.draw.rect(screen, colors[0], i)
                a = not a
            else:
                pygame.draw.rect(screen, colors[1], i)
                a = not a

    def jiggle(): #The function that provides the snake movement.
        if game:
            for num in range(len(snake)-2,-1,-1): #Every rectangle on the snake follows the preceded coordinate of the next rectangle.
                snake[num+1].x = snake[num].x
                snake[num+1].y = snake[num].y

    def cc(apple_): #Change coordinates function.
        global score,v

        #Checks if Snake ate the apple.
        if pygame.Rect.colliderect(apple_, rect):
            apple_.x = random.randint(40,570)
            apple_.y = random.randint(40,570)
            score += 250
            if v - 0.0006 > 0:
                v -= 0.0006
            grow()

    def check_coll(): #Checks if Snake collided with itself.
        global game,times,score,score_list

        m = snake
        list_ = combinations(m,2)
        for i,j in list_:
            #If collision occurred game ends.
            if pygame.Rect.colliderect(i,j):
                game = False
                score_list.append(score)
                best_score = max(score_list)
                write("GAME OVER", "toxigenesis bd.otf", 45, 250, 70,"black",screen)
                write("For restart press R", "toxigenesis bd.otf", 130, 355, 30, "black",screen)
                write(f"Your Score:{score}", "toxigenesis bd.otf", 130, 405, 30, "black",screen)
                write(f"Best:{best_score}", "toxigenesis bd.otf", 130, 455, 30, "black",screen)
                score_list = [best_score]
                time.sleep(.16)

    #Snake position correction for traveling behind walls.
    def pos_cor():
        if rect.x == -30:
            rect.x = 570
        elif rect.x == 600:
            rect.x = 0
        if rect.y == -30:
            rect.y = 570
        elif rect.y == 600:
            rect.y = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        key = pygame.key.get_pressed()

        screen.fill("dark green")
        pygame.draw.rect(screen, "red", apple)
        draw()

        if key[pygame.K_p]:
            while times == 0:
                j = game
                game = not j
                times += 1
        else:
            times = 0

        if key[pygame.K_g]:
            grow()
        if key[pygame.K_r]:
            running = False
            reset()
            snake_game()
        if key[pygame.K_m]:
            running = False
            reset()
            opening_screen()

        c_cc()
        check_coll()
        cc(apple)
        jiggle()
        move(current_key)
        pos_cor()

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(f"Score:{score}", True, "white")
        screen.blit(text, (5, 5))
        pygame.display.flip()

def opening_screen():
    running = True
    op_screen = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Snake Game")
    rect = pygame.Rect(200,80,200,80)
    rect.x = 185
    rect.y = 300
    but_color = "white"
    mouse_bd = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_bd = True
            else:
                mouse_bd = False

        mouse_pos = pygame.mouse.get_pos()
        range_flag = (185 <= mouse_pos[0] <= 385) and (300 <= mouse_pos[1] <= 380)

        op_screen.fill("dark green")

        if range_flag:
            but_color = "gray"
        else:
            but_color = "white"

        if range_flag and mouse_bd:
            running = False
            snake_game()

        pygame.draw.rect(op_screen, but_color,rect)
        write("START","toxigenesis bd.otf",243,322,20,"black",op_screen)
        write("SNAKE GAME","toxigenesis bd.otf",67,200,57,"black",op_screen)
        write("To go back to main menu press M", "toxigenesis bd.otf", 100, 420, 20, "black", op_screen)
        write("To restart press R", "toxigenesis bd.otf", 180, 460, 20, "black", op_screen)
        pygame.display.flip()

opening_screen()