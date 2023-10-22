import pygame, sys, random

pygame.init()


def game_window_start():
    screen.fill(green_light)
    screen.blit(icon_game_surf, icon_game_rect)
    pygame.draw.rect(screen, start_button_colour, start_font_rect)
    screen.blit(start_font, start_font_rect)
    pygame.draw.rect(screen, instructions_button_colour, instructions_font_rect)
    screen.blit(instructions_font, instructions_font_rect)


def game_window_instructions():
    screen.fill(white)
    screen.blit(font_large.render("INSTRUCTIONS", True, black), font_large.render("INSTRUCTIONS", True, black).get_rect(midtop=(450, 0)))
    screen.blit(font_small.render("--> Click one of the three buttons on the left according to", True, black), font_small.render("--> Click one of the three buttons on the left according to", True, black).get_rect(topleft=(0, 100)))
    screen.blit(font_small.render("      your choice.", True, black), font_small.render("    your choice.", True, black).get_rect(topleft=(0, 150)))
    screen.blit(font_small.render("--> You will be playing against the computer. First to", True, black),  font_small.render("You will be playing against the computer. First to.", True, black).get_rect(topleft=(0, 210)))
    screen.blit(font_small.render("      reach 10 points wins.", True, black),  font_small.render("      reach 10 points wins.", True, black).get_rect(topleft=(0, 260)))
    screen.blit(font_small.render("--> Click on the QUIT button in the bottom-left to exit the", True, black), font_small.render("--> Click on the QUIT button in the bottom-left to exit the", True, black).get_rect(topleft=(0, 320)))
    screen.blit(font_small.render("      game at anytime.", True, black), font_small.render("      game at anytime.", True, black).get_rect(topleft=(0, 370)))
    screen.blit(font_small.render("--> In the bottom-right, all the choices made by you and", True, black), font_small.render("--> In the bottom-right, all the choices made by you and", True, black).get_rect(topleft=(0, 430)))
    screen.blit(font_small.render("      the bot is shown. Press left/right arrow buttons to", True, black), font_small.render("      the bot is shown. Press left/right arrow buttons to", True, black).get_rect(topleft=(0, 480)))
    screen.blit(font_small.render("      scroll through it.", True, black), font_small.render("      scroll through it.", True, black).get_rect(topleft=(0, 530)))

    pygame.draw.rect(screen, back_button_colour, back_font_rect)
    screen.blit(back_font, back_font_rect)


def game_window_game():
    screen.fill(blue_medium)

    for i in range(player_choice_count):
        pygame.draw.rect(screen, player_score_win_list[i], player_history_rect_list[i])
        screen.blit(player_history[i], player_history_rect_list[i])
        pygame.draw.rect(screen, bot_score_win_list[i], bot_history_rect_list[i])
        screen.blit(bot_history[i], bot_history_rect_list[i])
    pygame.draw.rect(screen, blue_medium, pygame.Rect(0, 500, 600, 100))
    screen.blit(player_history_font, player_history_font_rect)
    screen.blit(bot_history_font, bot_history_font_rect)

    # drawing buttons
    pygame.draw.rect(screen, rock_button_colour, rock_rect)
    pygame.draw.rect(screen, paper_button_colour, paper_rect)
    pygame.draw.rect(screen, scissors_button_colour, scissors_rect)

    screen.blit(rock_surf, rock_rect)
    screen.blit(paper_surf, paper_rect)
    screen.blit(scissors_surf, scissors_rect)
    screen.blit(bot_surf, bot_rect)

    # drawing fonts
    screen.blit(player_name_font, player_name_font_rect)
    screen.blit(bot_name_font, bot_name_font_rect)
    screen.blit(VS_name_font, VS_name_font_rect)
    pygame.draw.rect(screen, quit_button_colour, quit_font_rect)
    screen.blit(quit_font, quit_font_rect)


def choice_box():
    pygame.draw.rect(screen, gold, player_choice_rect)
    if player_choice == "rock":
        screen.blit(rock_surf, player_choice_rect)
    elif player_choice == "paper":
        screen.blit(paper_surf, player_choice_rect)
    elif player_choice == "scissors":
        screen.blit(scissors_surf, player_choice_rect)

    pygame.draw.rect(screen, gold, bot_choice_rect)
    if bot_choice == "rock":
        screen.blit(rock_surf, bot_choice_rect)
    elif bot_choice == "paper":
        screen.blit(paper_surf, bot_choice_rect)
    elif bot_choice == "scissors":
        screen.blit(scissors_surf, bot_choice_rect)


def score_decision():
    global score_value_player, score_value_bot, bot_choice

    bot_choice = random.choice(("rock", "paper", "scissors"))
    if player_choice == bot_choice:
        player_score_win_list.insert(0, silver)
        bot_score_win_list.insert(0, silver)
        pass
    elif player_choice == "rock" and bot_choice == "paper":
        player_score_win_list.insert(0, red_light)
        bot_score_win_list.insert(0, green_light)
        score_value_bot += 1
    elif player_choice == "paper" and bot_choice == "scissors":
        player_score_win_list.insert(0, red_light)
        bot_score_win_list.insert(0, green_light)
        score_value_bot += 1
    elif player_choice == "scissors" and bot_choice == "rock":
        player_score_win_list.insert(0, red_light)
        bot_score_win_list.insert(0, green_light)
        score_value_bot += 1
    elif player_choice == "paper" and bot_choice == "rock":
        player_score_win_list.insert(0, green_light)
        bot_score_win_list.insert(0, red_light)
        score_value_player += 1
    elif player_choice == "scissors" and bot_choice == "paper":
        player_score_win_list.insert(0, green_light)
        bot_score_win_list.insert(0, red_light)
        score_value_player += 1
    elif player_choice == "rock" and bot_choice == "scissors":
        player_score_win_list.insert(0, green_light)
        bot_score_win_list.insert(0, red_light)
        score_value_player += 1


def show_score():
    screen.blit(score_board, score_board_rect)
    pygame.draw.rect(screen, purple, pygame.Rect(350, 60, 205, 60))

    score_player = font_large.render(str(score_value_player), True, black)
    score_player_rect = score_player.get_rect(topleft=(350, 60))
    screen.blit(score_player, score_player_rect)

    score_bot = font_large.render(str(score_value_bot), True, black)
    score_bot_rect = score_bot.get_rect(topleft=(520, 60))
    screen.blit(score_bot, score_bot_rect)

    screen.blit(hyphen_font, hyphen_font_rect)


def game_window_end():
    global sound_player_win_playdecision, sound_player_lose_playdecision

    screen.fill(silver)
    screen.blit(game_over_font, game_over_font_rect)
    if winner == "player":
        screen.blit(player_wins_font, player_wins_font_rect)
        if sound_player_win_playdecision:
            sound_player_win.play()
            sound_player_win_playdecision = False
    elif winner == "bot":
        screen.blit(bot_wins_font, bot_wins_font_rect)
        if sound_player_lose_playdecision:
            sound_player_lose.play(maxtime=2050)
            sound_player_lose_playdecision = False

    pygame.draw.rect(screen, main_menu_button_colour, main_menu_font_rect)
    screen.blit(main_menu_font, main_menu_font_rect)


def history(a):
    global player_choice_count

    player_choice_count += 1
    player_history.insert(0, a)
    if bot_choice == "rock":
        bot_history.insert(0, rock_32)
    elif bot_choice == "paper":
        bot_history.insert(0, paper_32)
    elif bot_choice == "scissors":
        bot_history.insert(0, scissors_32)


# file path
location_icon_window = "C:\\Users\\gmharish\\Desktop\\Python-Harish\\RockPaperScissorsgame\\icon_32_rockpaperscissors.png"
location_icon_game = "C:\\Users\\gmharish\\Desktop\\Python-Harish\\RockPaperScissorsgame\\icon_256_rockpaperscissors.png"
location_rock_img = "C:\\Users\\gmharish\\Desktop\\Python-Harish\\RockPaperScissorsgame\\img_rock_128.png"
location_paper_img = "C:\\Users\\gmharish\\Desktop\\Python-Harish\\RockPaperScissorsgame\\img_paper_128.png"
location_scissors_img = "C:\\Users\\gmharish\\Desktop\\Python-Harish\\RockPaperScissorsgame\\img_scissors_128.png"
location_bot_img = "C:\\Users\\gmharish\\Desktop\\Python-Harish\\RockPaperScissorsgame\\img_bot_256.png"
location_sound_bg = "C:\\Users\\gmharish\\Desktop\\Python-Harish\\RockPaperScissorsgame\\sound_bg.wav"
location_sound_button_click = "C:\\Users\\gmharish\\Desktop\\Python-Harish\\RockPaperScissorsgame\\sound_gamebuttons.wav"
location_sound_player_win = "C:\\Users\\gmharish\\Desktop\\Python-Harish\\RockPaperScissorsgame\\sound_playerwin.mp3"
location_sound_player_lose = "C:\\Users\\gmharish\\Desktop\\Python-Harish\\RockPaperScissorsgame\\sound_playerlose.mp3"

# screen
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rock Paper Scissors")
icon_window = pygame.image.load(location_icon_window)
pygame.display.set_icon(icon_window)
clock = pygame.time.Clock()

# sound
pygame.mixer.music.load(location_sound_bg)
pygame.mixer.music.play(-1)
sound_button_click = pygame.mixer.Sound(location_sound_button_click)
sound_player_win = pygame.mixer.Sound(location_sound_player_win)
sound_player_lose = pygame.mixer.Sound(location_sound_player_lose)

# font
font_small = pygame.font.Font("freesansbold.ttf", 32)
font_medium_small = pygame.font.Font("freesansbold.ttf", 40)
font_medium_large = pygame.font.Font("freesansbold.ttf", 48)
font_large = pygame.font.Font("freesansbold.ttf", 64)

# colours
red_dark = (255, 0, 0)
red_light = (255, 127, 127)
green_dark = (0, 255, 0)
green_light = (144, 238, 144)
blue_dark = (0, 0, 255)
blue_medium = (150, 170, 255)
blue_light = (173, 216, 230)
white = (255, 255, 255)
black = (0, 0, 0)
gold = (255, 215, 0)
purple = (138, 43, 226)
orange_dark = (255, 140, 0)
orange_light = (255, 213, 128)
silver = (170, 170, 170)
violet = (148, 0, 211)
brown = (210, 105, 30)

rock_button_colour = red_dark
paper_button_colour = red_dark
scissors_button_colour = red_dark
start_button_colour = orange_dark
instructions_button_colour = orange_dark
back_button_colour = red_dark
quit_button_colour = red_dark
main_menu_button_colour = red_dark

player_choice = ""
bot_choice = ""
score_value_player = 0
score_value_bot = 0
screen_window = "start"

# start
icon_game_surf = pygame.image.load(location_icon_game)
icon_game_rect = icon_game_surf.get_rect(midtop=(450, 0))
start_font = font_medium_large.render("START", True, blue_dark)
start_font_rect = start_font.get_rect(center=(450, 320))
instructions_font = font_medium_large.render("INSTRUCTIONS", True, blue_dark)
instructions_font_rect = instructions_font.get_rect(center=(450, 400))

# game
rock_surf = pygame.image.load(location_rock_img)
paper_surf = pygame.image.load(location_paper_img)
scissors_surf = pygame.image.load(location_scissors_img)
rock_rect = rock_surf.get_rect(topleft=(10, 60))
paper_rect = rock_surf.get_rect(topleft=(10, 210))
scissors_rect = rock_surf.get_rect(topleft=(10, 360))
bot_surf = pygame.image.load(location_bot_img)
bot_rect = bot_surf.get_rect(topright=(920, 160))
player_choice_rect = pygame.Rect(210, 210, 128, 128)
bot_choice_rect = pygame.Rect(550, 210, 128, 128)

player_name_font = font_medium_small.render("PLAYER", True, black)
player_name_font_rect = player_name_font.get_rect(topleft=(20, 10))
bot_name_font = font_medium_small.render("COMPUTER", True, black)
bot_name_font_rect = bot_name_font.get_rect(topleft=(650, 10))
VS_name_font = font_large.render("VS", True, black)
VS_name_font_rect = VS_name_font.get_rect(topleft=(410, 240))
score_board = font_small.render("SCOREBOARD", True, red_dark)
score_board_rect = score_board.get_rect(center=(450, 32))
hyphen_font = font_large.render("–", True, black)
hyphen_font_rect = hyphen_font.get_rect(center=(450, 85))
quit_font = font_medium_small.render("<< QUIT", True, black)
quit_font_rect = quit_font.get_rect(bottomleft=(0, 600))

# end
game_over_font = font_large.render("GAME OVER", True, violet)
game_over_font_rect = game_over_font.get_rect(center=(450, 200))
player_wins_font = font_large.render("PLAYER WINS", True, brown)
player_wins_font_rect = player_wins_font.get_rect(center=(450, 300))
bot_wins_font = font_large.render("COMPUTER WINS", True, brown)
bot_wins_font_rect = bot_wins_font.get_rect(center=(450, 300))
main_menu_font = font_medium_large.render("MAIN MENU", True, black)
main_menu_font_rect = main_menu_font.get_rect(center=(450, 400))

# instructions
back_font = font_medium_small.render("<< BACK", True, black)
back_font_rect = back_font.get_rect(bottomleft=(0, 600))

# history
rock_32 = pygame.transform.scale(rock_surf, (32, 32))
paper_32 = pygame.transform.scale(paper_surf, (32, 32))
scissors_32 = pygame.transform.scale(scissors_surf, (32, 32))
player_history_font = font_small.render("PLAYER:", True, black)
player_history_font_rect = player_history_font.get_rect(topright=(580, 500))
bot_history_font = font_small.render("COMPUTER:", True, black)
bot_history_font_rect = bot_history_font.get_rect(topright=(580, 532))
player_history_rect_list = []
bot_history_rect_list = []
for i in range(1, 51):
    player_history_rect_list.append(pygame.Rect(580+32*i, 500, 32, 32))
for i in range(1, 51):
    bot_history_rect_list.append(pygame.Rect(580+32*i, 532, 32, 32))
player_choice_count = 0
player_history = []
bot_history = []
player_score_win_list = []
bot_score_win_list = []
history_rect_list_speed = 0

while True:
    mouse = pygame.mouse.get_pos()


    if screen_window == "start":
        sound_player_win_playdecision = True
        sound_player_lose_playdecision = True
        pygame.mixer.music.set_volume(0.7)
        game_window_start()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if start_font_rect.collidepoint(mouse):
                start_button_colour = orange_light
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen_window = "game"
                    sound_button_click.play()
            if not start_font_rect.collidepoint(mouse):
                start_button_colour = orange_dark

            if instructions_font_rect.collidepoint(mouse):
                instructions_button_colour = orange_light
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen_window = "instructions"
                    sound_button_click.play()
            if not instructions_font_rect.collidepoint(mouse):
                instructions_button_colour = orange_dark


    if screen_window == "instructions":
        pygame.mixer.music.set_volume(1.0)
        game_window_instructions()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if back_font_rect.collidepoint(mouse):
                back_button_colour = red_light
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen_window = "start"
                    sound_button_click.play()
            if not back_font_rect.collidepoint(mouse):
                back_button_colour = red_dark


    if screen_window == "game":
        pygame.mixer.music.set_volume(0.3)
        game_window_game()
        choice_box()
        show_score()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if rock_rect.collidepoint(mouse):
                rock_button_colour = blue_light
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sound_button_click.play()
                    player_choice = "rock"
                    score_decision()
                    history(rock_32)
            if not rock_rect.collidepoint(mouse):
                rock_button_colour = blue_dark

            if paper_rect.collidepoint(mouse):
                paper_button_colour = blue_light
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sound_button_click.play()
                    player_choice = "paper"
                    score_decision()
                    history(paper_32)
            if not paper_rect.collidepoint(mouse):
                paper_button_colour = blue_dark

            if scissors_rect.collidepoint(mouse):
                scissors_button_colour = blue_light
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sound_button_click.play()
                    player_choice = "scissors"
                    score_decision()
                    history(scissors_32)
            if not scissors_rect.collidepoint(mouse):
                scissors_button_colour = blue_dark

            if quit_font_rect.collidepoint(mouse):
                quit_button_colour = red_light
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sound_button_click.play()
                    screen_window = "start"
                    score_value_player = 0
                    score_value_bot = 0
                    player_choice_count = 0
            if not quit_font_rect.collidepoint(mouse):
                quit_button_colour = red_dark

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and player_history_rect_list[0].midright[0] < 900:
                    history_rect_list_speed = 5
                if event.key == pygame.K_LEFT and player_history_rect_list[len(player_history)-1].midleft[0] > 600:
                    history_rect_list_speed = -5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    history_rect_list_speed = 0
                if event.key == pygame.K_LEFT:
                    history_rect_list_speed = 0

        for i in range(50):
            player_history_rect_list[i].x += history_rect_list_speed
            bot_history_rect_list[i].x += history_rect_list_speed
        if player_history_rect_list[0].midright[0] >= 900:
            history_rect_list_speed = 0
        if player_history_rect_list[len(player_history)-1].midleft[0] <= 600:
            history_rect_list_speed = 0

        if score_value_player == 10:
            winner = "player"
            screen_window = "end"
        elif score_value_bot == 10:
            winner = "bot"
            screen_window = "end"


    if screen_window == "end":
        pygame.mixer.music.set_volume(0.1)
        game_window_end()
        score_value_player = 0
        score_value_bot = 0
        player_choice_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if main_menu_font_rect.collidepoint(mouse):
                main_menu_button_colour = red_light
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sound_button_click.play()
                    screen_window = "start"
            if not main_menu_font_rect.collidepoint(mouse):
                main_menu_button_colour = red_dark


    pygame.display.update()
    clock.tick(60)
