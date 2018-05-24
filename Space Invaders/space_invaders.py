import pygame;

pygame.mixer.pre_init(44100, 16, 2, 4096);
pygame.init();
clock = pygame.time.Clock();
screen_size = (785, 700);

white = (255, 255, 255);
black = (0, 0, 0);
green = (0, 254, 44);
red = (255, 0, 0);

number_of_enemies = 32;
enemy_speed = 30;
enemy_timer = 0;
score = 0;
FPS = 60;
temp = 0;

game_over = False;
victory = False;
reverse = False;
go_down = False;

game_display = pygame.display.set_mode(screen_size);
explode_sfx = pygame.mixer.Sound('Sound FX/Player/270307__littlerobotsoundfactory__explosion-01.wav');
shoot_sfx = pygame.mixer.Sound('Sound FX/Player/270343__littlerobotsoundfactory__shoot-01.wav');
font = pygame.font.SysFont('hooge0555cyr2', 25);

def game_over_screen():
    for event in pygame.event.get():
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_q):
                return 'quit';
            if(event.key == pygame.K_c):
                return 'continue';

    game_display.fill(black);

    text1 = font.render(('GAME OVER'), True, white);
    text2 = font.render(("You got " + str(score)) + ' points!', True, white);

    game_display.blit(text1, [screen_size[0]/2 - text1.get_width()/2, screen_size[1]/2 - text1.get_height()/2 - 50]);
    game_display.blit(text2, [screen_size[0]/2 - text2.get_width()/2, screen_size[1]/2 - text2.get_height()/2]);

    pygame.display.update();
def victory_screen():
    for event in pygame.event.get():
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_q):
                return 'quit';
            if(event.key == pygame.K_c):
                return 'continue';

    game_display.fill(black);

    text1 = font.render(('CONGRATULATIONS!'), True, white);
    text2 = font.render(("You got " + str(score)) + ' points!', True, white);

    game_display.blit(text1, [screen_size[0]/2 - text1.get_width()/2, screen_size[1]/2 - text1.get_height()/2 - 50]);
    game_display.blit(text2, [screen_size[0]/2 - text2.get_width()/2, screen_size[1]/2 - text2.get_height()/2]);

    pygame.display.update();
def initialize_player():
    square_one = [screen_size[0] / 2, screen_size[1] - 10];
    square_two = [screen_size[0] / 2, screen_size[1] - 20];
    square_three = [square_one[0] + 10, square_one[1]];
    square_four = [square_one[0] - 10, square_one[1]];
    player = [square_one, square_two, square_three, square_four];
    return player;
def initialize_enemies(modifier, line_mod):
    #line 1
    square_one = [40 + modifier, 10 + line_mod];
    square_two = [100 + modifier, 10 + line_mod];

    # line 2
    square_three = [50 + modifier, 20 + line_mod];
    square_four = [90 + modifier, 20 + line_mod];

    # line 3
    square_five = [40 + modifier, 30 + line_mod];
    square_six = [50 + modifier, 30 + line_mod];
    square_seven = [60 + modifier, 30 + line_mod];
    square_eight = [70 + modifier, 30 + line_mod];
    square_nine = [80 + modifier, 30 + line_mod];
    square_ten = [90 + modifier, 30 + line_mod];
    square_eleven = [100 + modifier, 30 + line_mod];

    # line 4
    square_twelve = [30 + modifier, 40 + line_mod];
    square_thirteen = [40 + modifier, 40 + line_mod];
    square_fourteen = [60 + modifier, 40 + line_mod];
    square_fifteen = [70 + modifier, 40 + line_mod];
    square_sixteen = [80 + modifier, 40 + line_mod];
    square_seventeen = [100 + modifier, 40 + line_mod];
    square_eighteen = [110 + modifier, 40 + line_mod];

    #line 5
    square_nineteen = [20 + modifier, 50 + line_mod];
    square_twenty = [30 + modifier, 50 + line_mod];
    square_twentyone = [40 + modifier, 50 + line_mod];
    square_twentytwo = [50 + modifier, 50 + line_mod];
    square_twentythree = [60 + modifier, 50 + line_mod];
    square_twentyfour = [70 + modifier, 50 + line_mod];
    square_twentyfive = [80 + modifier, 50 + line_mod];
    square_twentysix = [90 + modifier, 50 + line_mod];
    square_twentyseven = [100 + modifier, 50 + line_mod];
    square_twentyeight = [110 + modifier, 50 + line_mod];
    square_twentynine = [120 + modifier, 50 + line_mod];

    #line 6
    square_thirty = [20 + modifier, 60 + line_mod];
    square_thirtyone = [40 + modifier, 60 + line_mod];
    square_thirtytwo = [50 + modifier, 60 + line_mod];
    square_thirtythree = [60 + modifier, 60 + line_mod];
    square_thirtyfour = [70 + modifier, 60 + line_mod];
    square_thirtyfive = [80 + modifier, 60 + line_mod];
    square_thirtysix = [90 + modifier, 60 + line_mod];
    square_thirtyseven = [100 + modifier, 60 + line_mod];
    square_thirtyeight = [120 + modifier, 60 + line_mod];

    #line 7
    square_thirtynine = [20 + modifier, 70 + line_mod];
    square_forty = [40 + modifier, 70 + line_mod];
    square_fortyone = [100 + modifier, 70 + line_mod];
    square_fortytwo = [120 + modifier, 70 + line_mod];

    #line 8
    square_fortythree = [50 + modifier, 80 + line_mod];
    square_fortyfour = [60 + modifier, 80 + line_mod];
    square_fortyfive = [80 + modifier, 80 + line_mod];
    square_fortysix = [90 + modifier, 80 + line_mod];

    enemy = [square_one, square_two, square_three, square_four, square_five, square_six, square_seven, square_eight, square_nine, square_ten,
    square_eleven, square_twelve, square_thirteen, square_fourteen, square_fifteen, square_sixteen, square_seventeen, square_eighteen,
    square_nineteen, square_twenty, square_twentyone, square_twentytwo, square_twentythree, square_twentyfour, square_twentyfive,
    square_twentysix, square_twentyseven, square_twentyeight, square_twentynine, square_thirty, square_thirtyone, square_thirtytwo,
    square_thirtythree, square_thirtyfour, square_thirtyfive, square_thirtysix, square_thirtyseven, square_thirtyeight, square_thirtynine,
    square_forty, square_fortyone, square_fortytwo, square_fortythree, square_fortyfour, square_fortyfive, square_fortysix];

    for i in enemy:
        i[0] = round(i[0] / 10) * 10;
        i[1] = round(i[1] / 10) * 10;

        i[0] /= 2;
        i[1] /= 2;

    return enemy;
def render_bullet(bullet, bullet_speed):
    if (len(bullet) != 0):
        for elem in bullet:
            elem[0] = int(elem[0]);
            elem[0] = round(elem[0] / 10) * 10;
            elem[1] += bullet_speed;
            pygame.draw.rect(game_display, white, [elem[0], elem[1], 4, 4]);
def render_player(player, block_size, move):
    for i in range(0, 4):
        player[i][0] = int(player[i][0]) + move;
        pygame.draw.rect(game_display, white, [player[i][0], player[i][1], block_size - 2, block_size - 2]);
def render_enemies(enemies, bullet, explosion):
    global number_of_enemies
    global game_over;
    global go_down;
    global reverse;
    global score;

    for elem in enemies:
        for i in elem:
            for b in bullet:
                if(b == i):
                    explode_sfx.play();
                    explosion.append(elem[:]);
                    del elem[:];
                    bullet[:] = [];
                    number_of_enemies -= 1;
                    score += 100;
                    break;

            if(i[1] >= screen_size[0] - 85):
                game_over = True;
            if (i[0] == screen_size[1] + 50):
                go_down = True;
                reverse = True;
            elif(i[0] == 25):
                go_down = True;
                reverse = False;
            if(len(elem) != 0):
                pygame.draw.rect(game_display, green, [i[0], i[1], 4, 4]);
def enemy_movement(enemies, enemy_down_speed):
    global enemy_timer;
    global enemy_speed;
    global go_down;

    if (enemy_timer >= 40):
        for elem in enemies:
            for i in elem:
                if(go_down):
                    i[1] += enemy_down_speed;

                i[0] += enemy_speed;
                enemy_timer = 0;
    go_down = False;
def render_screen(player, move, bullet, bullet_speed, enemies, enemy_down_speed, block_size, explosion, is_explosion):
    global number_of_enemies;
    global game_over;
    global enemy_speed;
    global enemy_timer;
    global reverse;
    global score;
    global temp;
    global go_down;
    global victory;

    if(number_of_enemies == 0):
        victory = True;

    if(reverse):
        enemy_speed = -(enemy_speed);
    if(score % 500 == 0 and score != 0 and score != temp):
        enemy_speed += 5;
        temp = score;

    game_display.fill(black);
    render_player(player, block_size, move);
    render_bullet(bullet, bullet_speed);
    render_enemies(enemies, bullet, explosion);
    enemy_movement(enemies, enemy_timer);

    for e in explosion:
        for i in e:
            pygame.draw.rect(game_display, red, [i[0], i[1], 5, 5]);

    text = font.render(("Points: " + str(score)), True, white);
    game_display.blit(text, [10, 5]);

    pygame.display.update();
    clock.tick(FPS);

    enemy_timer += 1;

def main():
    pygame.display.set_caption("Space Invaders");
    pygame.mixer.music.load('Sound FX/Music/Best VGM 153 - Mega Man 2 - Dr. Wily Stage 1  2.mp3');
    pygame.mixer.music.set_volume(1);
    pygame.mixer.music.play(-1);

    enemies = [];
    init_mod = 210;

    bullet = [];
    bullet_speed = -10;
    enemy_down_speed = 2 * 3000;
    block_size = 10;
    move = 0;
    count = 0;

    exit_game = False;
    cooldown = False;
    is_explosion = False;
    global game_over;
    global victory;
    global number_of_enemies;

    player = initialize_player();

    for num in range(0, 400, 100):
        for i in range(0, 1000, 140):
            enemy = initialize_enemies(i + init_mod, num);
            enemies.append(enemy);
    while(not exit_game and not game_over and not victory):
        if(count >= 60):
            cooldown = False
            count = 0;
        for event in pygame.event.get():
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_q):
                    exit_game = True;
                if(event.key == pygame.K_d or event.key == pygame.K_RIGHT):
                    move += 5;
                if (event.key == pygame.K_a or event.key == pygame.K_LEFT):
                    move -= 5;
                if(event.key == pygame.K_k and cooldown == False):
                    bullet.append([player[1][0], player[1][1]]);
                    #bullet = [player[1][0], player[1][1]];
                    shoot_sfx.play();
                    cooldown = True;

            if(event.type == pygame.KEYUP):
                if(event.key == pygame.K_a or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                    move = 0;
                if(event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_s):
                    move = 0;
        if(cooldown):
            count += 1;

        render_screen(player, move, bullet, bullet_speed, enemies, enemy_down_speed, block_size, [], is_explosion);

    if(game_over):
        pygame.mixer.music.load('Sound FX/Music/Super Mario Bros. Music - Lose a Life.mp3');
        pygame.mixer.music.set_volume(1);
        pygame.mixer.music.play(1);
        while 1:
            command = game_over_screen();
            if(command == None):
                continue;
            elif(command == 'quit'):
                break;
            elif(command == 'continue'):
                game_display.fill(black);
                text = font.render(("That's The Spirit!"), True, white);
                game_display.blit(text, [screen_size[0] / 2 - text.get_width() / 2, screen_size[1] / 2 - text.get_height() / 2 - 50]);
                pygame.display.update();
                pygame.time.delay(2000);
                game_over = False;
                number_of_enemies = 24;
                main();
    if(victory):
        pygame.mixer.music.load('Sound FX/Music/ff6 8 bit fanfare.mp3');
        pygame.mixer.music.set_volume(1);
        pygame.mixer.music.play(1);
        while 1:
            command = victory_screen();
            if(command == None):
                continue;
            elif(command == 'quit'):
                break;
            elif(command == 'continue'):
                game_display.fill(black);
                text = font.render(("That's The Spirit!"), True, white);
                game_display.blit(text, [screen_size[0] / 2 - text.get_width() / 2, screen_size[1] / 2 - text.get_height() / 2 - 50]);
                pygame.display.update();
                pygame.time.delay(2000);
                victory = False;
                number_of_enemies = 24;
                main();

if __name__ == '__main__':
    main();