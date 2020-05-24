import pygame
import socket
from sys import exit
from network import Network


pygame.font.init()

width = 1000
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Blackjack")
clock = pygame.time.Clock()
background = pygame.Surface(screen.get_size())
background.fill((5, 79, 33))
id

card_back = pygame.image.load('resources/cards/cardback.png')
d_A = pygame.image.load('resources/cards/ad.png')
c_A = pygame.image.load('resources/cards/ac.png')
h_A = pygame.image.load('resources/cards/ah.png')
s_A = pygame.image.load('resources/cards/as.png')
d_2 = pygame.image.load('resources/cards/2d.png')
c_2 = pygame.image.load('resources/cards/2c.png')
h_2 = pygame.image.load('resources/cards/2h.png')
s_2 = pygame.image.load('resources/cards/2s.png')
d_3 = pygame.image.load('resources/cards/3d.png')
c_3 = pygame.image.load('resources/cards/3c.png')
h_3 = pygame.image.load('resources/cards/3h.png')
s_3 = pygame.image.load('resources/cards/3s.png')
d_4 = pygame.image.load('resources/cards/4d.png')
c_4 = pygame.image.load('resources/cards/4c.png')
h_4 = pygame.image.load('resources/cards/4h.png')
s_4 = pygame.image.load('resources/cards/4s.png')
d_5 = pygame.image.load('resources/cards/5d.png')
c_5 = pygame.image.load('resources/cards/5c.png')
h_5 = pygame.image.load('resources/cards/5h.png')
s_5 = pygame.image.load('resources/cards/5s.png')
d_6 = pygame.image.load('resources/cards/6d.png')
c_6 = pygame.image.load('resources/cards/6c.png')
h_6 = pygame.image.load('resources/cards/6h.png')
s_6 = pygame.image.load('resources/cards/6s.png')
d_7 = pygame.image.load('resources/cards/7d.png')
c_7 = pygame.image.load('resources/cards/7c.png')
h_7 = pygame.image.load('resources/cards/7h.png')
s_7 = pygame.image.load('resources/cards/7s.png')
d_8 = pygame.image.load('resources/cards/8d.png')
c_8 = pygame.image.load('resources/cards/8c.png')
h_8 = pygame.image.load('resources/cards/8h.png')
s_8 = pygame.image.load('resources/cards/8s.png')
d_9 = pygame.image.load('resources/cards/9d.png')
c_9 = pygame.image.load('resources/cards/9c.png')
h_9 = pygame.image.load('resources/cards/9h.png')
s_9 = pygame.image.load('resources/cards/9s.png')
d_10 = pygame.image.load('resources/cards/10d.png')
c_10 = pygame.image.load('resources/cards/10c.png')
h_10 = pygame.image.load('resources/cards/10h.png')
s_10 = pygame.image.load('resources/cards/10s.png')
d_J = pygame.image.load('resources/cards/jd.png')
c_J = pygame.image.load('resources/cards/jc.png')
h_J = pygame.image.load('resources/cards/jh.png')
s_J = pygame.image.load('resources/cards/js.png')
d_Q = pygame.image.load('resources/cards/qd.png')
c_Q = pygame.image.load('resources/cards/qc.png')
h_Q = pygame.image.load('resources/cards/qh.png')
s_Q = pygame.image.load('resources/cards/qs.png')
d_K = pygame.image.load('resources/cards/kd.png')
c_K = pygame.image.load('resources/cards/kc.png')
h_K = pygame.image.load('resources/cards/kh.png')
s_K = pygame.image.load('resources/cards/ks.png')

cards = [d_A, c_A, h_A, s_A,
         d_2, c_2, h_2, s_2,
         d_3, c_3, h_3, s_3,
         d_4, c_4, h_4, s_4,
         d_5, c_5, h_5, s_5,
         d_6, c_6, h_6, s_6,
         d_7, c_7, h_7, s_7,
         d_8, c_8, h_8, s_8,
         d_9, c_9, h_9, s_9,
         d_10, c_10, h_10, s_10,
         d_J, c_J, h_J, s_J,
         d_Q, c_Q, h_Q, s_Q,
         d_K, c_K, h_K, s_K]
cardA = [d_A, c_A, h_A, s_A]
card2 = [d_2, c_2, h_2, s_2]
card3 = [d_3, c_3, h_3, s_3]
card4 = [d_4, c_4, h_4, s_4]
card5 = [d_5, c_5, h_5, s_5]
card6 = [d_6, c_6, h_6, s_6]
card7 = [d_7, c_7, h_7, s_7]
card8 = [d_8, c_8, h_8, s_8]
card9 = [d_9, c_9, h_9, s_9]
card10 = [d_10, c_10, h_10, s_10,
          d_J, c_J, h_J, s_J,
          d_Q, c_Q, h_Q, s_Q,
          d_K, c_K, h_K, s_K]


def convert_pcards(cards):
    rescards = []
    for k in cards:
        temp = []
        for c in k:
            if c == "d_A":
                temp.append(d_A)
            elif c == "d_2":
                temp.append(d_2)
            elif c == "d_3":
                temp.append(d_3)
            elif c == "d_4":
                temp.append(d_4)
            elif c == "d_5":
                temp.append(d_5)
            elif c == "d_6":
                temp.append(d_6)
            elif c == "d_7":
                temp.append(d_7)
            elif c == "d_8":
                temp.append(d_8)
            elif c == "d_9":
                temp.append(d_9)
            elif c == "d_10":
                temp.append(d_10)
            elif c == "d_J":
                temp.append(d_J)
            elif c == "d_Q":
                temp.append(d_Q)
            elif c == "d_K":
                temp.append(d_K)
            elif c == "c_A":
                temp.append(c_A)
            elif c == "c_2":
                temp.append(c_2)
            elif c == "c_3":
                temp.append(c_3)
            elif c == "c_4":
                temp.append(c_4)
            elif c == "c_5":
                temp.append(c_5)
            elif c == "c_6":
                temp.append(c_6)
            elif c == "c_7":
                temp.append(c_7)
            elif c == "c_8":
                temp.append(c_8)
            elif c == "c_9":
                temp.append(c_9)
            elif c == "c_10":
                temp.append(c_10)
            elif c == "c_J":
                temp.append(c_J)
            elif c == "c_Q":
                temp.append(c_Q)
            elif c == "c_K":
                temp.append(c_K)
            elif c == "h_A":
                temp.append(h_A)
            elif c == "h_2":
                temp.append(h_2)
            elif c == "h_3":
                temp.append(h_3)
            elif c == "h_4":
                temp.append(h_4)
            elif c == "h_5":
                temp.append(h_5)
            elif c == "h_6":
                temp.append(h_6)
            elif c == "h_7":
                temp.append(h_7)
            elif c == "h_8":
                temp.append(h_8)
            elif c == "h_9":
                temp.append(h_9)
            elif c == "h_10":
                temp.append(h_10)
            elif c == "h_J":
                temp.append(h_J)
            elif c == "h_Q":
                temp.append(h_Q)
            elif c == "h_K":
                temp.append(h_K)
            elif c == "s_A":
                temp.append(s_A)
            elif c == "s_2":
                temp.append(s_2)
            elif c == "s_3":
                temp.append(s_3)
            elif c == "s_4":
                temp.append(s_4)
            elif c == "s_5":
                temp.append(s_5)
            elif c == "s_6":
                temp.append(s_6)
            elif c == "s_7":
                temp.append(s_7)
            elif c == "s_8":
                temp.append(s_8)
            elif c == "s_9":
                temp.append(s_9)
            elif c == "s_10":
                temp.append(s_10)
            elif c == "s_J":
                temp.append(s_J)
            elif c == "s_Q":
                temp.append(s_Q)
            elif c == "s_K":
                temp.append(s_K)
        rescards.append(temp)
    return rescards


def convert_cards(cards):
    temp = []
    for c in cards:
        if c == "d_A":
            temp.append(d_A)
        elif c == "d_2":
            temp.append(d_2)
        elif c == "d_3":
            temp.append(d_3)
        elif c == "d_4":
            temp.append(d_4)
        elif c == "d_5":
            temp.append(d_5)
        elif c == "d_6":
            temp.append(d_6)
        elif c == "d_7":
            temp.append(d_7)
        elif c == "d_8":
            temp.append(d_8)
        elif c == "d_9":
            temp.append(d_9)
        elif c == "d_10":
            temp.append(d_10)
        elif c == "d_J":
            temp.append(d_J)
        elif c == "d_Q":
            temp.append(d_Q)
        elif c == "d_K":
            temp.append(d_K)
        elif c == "c_A":
            temp.append(c_A)
        elif c == "c_2":
            temp.append(c_2)
        elif c == "c_3":
            temp.append(c_3)
        elif c == "c_4":
            temp.append(c_4)
        elif c == "c_5":
            temp.append(c_5)
        elif c == "c_6":
            temp.append(c_6)
        elif c == "c_7":
            temp.append(c_7)
        elif c == "c_8":
            temp.append(c_8)
        elif c == "c_9":
            temp.append(c_9)
        elif c == "c_10":
            temp.append(c_10)
        elif c == "c_J":
            temp.append(c_J)
        elif c == "c_Q":
            temp.append(c_Q)
        elif c == "c_K":
            temp.append(c_K)
        elif c == "h_A":
            temp.append(h_A)
        elif c == "h_2":
            temp.append(h_2)
        elif c == "h_3":
            temp.append(h_3)
        elif c == "h_4":
            temp.append(h_4)
        elif c == "h_5":
            temp.append(h_5)
        elif c == "h_6":
            temp.append(h_6)
        elif c == "h_7":
            temp.append(h_7)
        elif c == "h_8":
            temp.append(h_8)
        elif c == "h_9":
            temp.append(h_9)
        elif c == "h_10":
            temp.append(h_10)
        elif c == "h_J":
            temp.append(h_J)
        elif c == "h_Q":
            temp.append(h_Q)
        elif c == "h_K":
            temp.append(h_K)
        elif c == "s_A":
            temp.append(s_A)
        elif c == "s_2":
            temp.append(s_2)
        elif c == "s_3":
            temp.append(s_3)
        elif c == "s_4":
            temp.append(s_4)
        elif c == "s_5":
            temp.append(s_5)
        elif c == "s_6":
            temp.append(s_6)
        elif c == "s_7":
            temp.append(s_7)
        elif c == "s_8":
            temp.append(s_8)
        elif c == "s_9":
            temp.append(s_9)
        elif c == "s_10":
            temp.append(s_10)
        elif c == "s_J":
            temp.append(s_J)
        elif c == "s_Q":
            temp.append(s_Q)
        elif c == "s_K":
            temp.append(s_K)
    return temp

def menu_screen(screen, name):
    global game, background
    run = True
    offline = False

    while run:
        screen.blit(background, (0, 0))
        small_font = pygame.font.SysFont("comicsans", 50)

        intr = small_font.render("Нажмите для подключения", 1, (255, 0, 0))
        screen.blit(intr, (int(width / 2 - intr.get_width() / 2), 100))
        if offline:
            off = small_font.render("Сервер оффлайн, попробуйте позже", 1, (255, 0, 0))
            screen.blit(off, (int(width / 2 - off.get_width() / 2), 200))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                offline = False
                try:
                    game = connect()
                    run = False
                    main()
                    break
                except socket.error:
                    print("Server Offline")
                    offline = True


def connect():
    global n
    n = Network()
    return n.p


def redraw_window(pl_cards, dealer_cards, gameover, stand, _game):
    global restart_button, id
    turn = _game.turn
    playing = (len(_game.player_cards[id]) == 0)
    went = game.p_stands[id]
    winners = _game.winners
    font = pygame.font.SysFont('arial', 15)
    hit_txt = font.render('Hit', 1, (0, 0, 0))
    stand_txt = font.render('Stand', 1, (0, 0, 0))
    restart_txt = font.render('Restart', 1, (0, 0, 0))
    gameover_txt = font.render('GAME OVER', 1, (255, 255, 255))

    screen.blit(background, (0, 0))

    for card in dealer_cards:
        x = 230 + dealer_cards.index(card) * 110
        screen.blit(card, (x, 10))
    screen.blit(card_back, (340, 10))

    if id == 0:
        try:
            names = []
            for k, v in _game.p_names.items():
                for i in range(3):
                    if v == i:
                        names.append(k)
            p1 = font.render(names[1], 1, (255, 0, 0))
            screen.blit(p1, (165, 298))
            p2 = font.render(names[0], 1, (255, 0, 0))
            screen.blit(p2, (int(width / 2 - p2.get_width() / 2), 410))
            p3 = font.render(names[2], 1, (255, 0, 0))
            screen.blit(p3, (835 - p3.get_width(), 298))
        except:
            pass
        for card in pl_cards[1]:
            rot = pygame.transform.rotate(card, 270)
            y = 30 + pl_cards[1].index(card) * 110
            screen.blit(rot, (10, y))
        for card in pl_cards[0]:                    
            x = 230 + pl_cards[0].index(card) * 110
            screen.blit(card, (x, 450))
        for card in pl_cards[2]:
            rot = pygame.transform.rotate(card, 90)
            y = 470 - pl_cards[2].index(card) * 110
            screen.blit(rot, (850, y))
    elif id == 1:
        try:
            names = []
            for k, v in _game.p_names.items():
                for i in range(3):
                    if v == i:
                        names.append(k)
            p1 = font.render(names[0], 1, (255, 0, 0))
            screen.blit(p1, (165, 298))
            p2 = font.render(names[1], 1, (255, 0, 0))
            screen.blit(p2, (int(width / 2 - p2.get_width() / 2), 410))
            p3 = font.render(names[2], 1, (255, 0, 0))
            screen.blit(p3, (835 - p3.get_width(), 298))
        except:
            pass
        for card in pl_cards[0]:
            rot = pygame.transform.rotate(card, 270)
            y = 30 + pl_cards[0].index(card) * 110
            screen.blit(rot, (10, y))
        for card in pl_cards[1]:                    
            x = 230 + pl_cards[1].index(card) * 110
            screen.blit(card, (x, 450))
        for card in pl_cards[2]:
            rot = pygame.transform.rotate(card, 90)
            y = 470 - pl_cards[2].index(card) * 110
            screen.blit(rot, (850, y))
    elif id == 2:
        try:
            names = []
            for k, v in _game.p_names.items():
                for i in range(3):
                    if v == i:
                        names.append(k)
            p1 = font.render(names[0], 1, (255, 0, 0))
            screen.blit(p1, (165, 298))
            p2 = font.render(names[2], 1, (255, 0, 0))
            screen.blit(p2, ((width / 2 - p2.get_width() / 2), 410))
            p3 = font.render(names[1], 1, (255, 0, 0))
            screen.blit(p3, (835 - p3.get_width(), 298))
        except:
            pass
        for card in pl_cards[0]:
            rot = pygame.transform.rotate(card, 270)
            y = 30 + pl_cards[0].index(card) * 110
            screen.blit(rot, (10, y))
        for card in pl_cards[2]:                    
            x = 230 + pl_cards[2].index(card) * 110
            screen.blit(card, (x, 450))
        for card in pl_cards[1]:
            rot = pygame.transform.rotate(card, 90)
            y = 470 - pl_cards[1].index(card) * 110
            screen.blit(rot, (850, y))
    if (gameover or stand) and not game.pressed_restart[id]:
        screen.blit(gameover_txt, (int(width/2 - gameover_txt.get_width()/2), 290))
        restart_button = pygame.draw.rect(background, (192, 192, 192), (463, 310, 75, 25))
        screen.blit(restart_txt, (480, 313))
        screen.blit(dealer_cards[1], (340, 10))
    if stand:
        win = ""
        for w in winners:
            win += w + " "
        if len(winners) == 1:
            win += "победил!"
        elif len(winners) > 1:
            win += "победили!"
        wi = font.render(win, 1, (255, 0, 0))
        screen.blit(wi, (int(width / 2 - wi.get_width() / 2), 350))
    if game.pressed_restart[id]:
        restart_button = pygame.draw.rect(background, (5, 79, 33), (463, 310, 75, 25))
        screen.blit(dealer_cards[1], (340, 10))
        wait = font.render("Подождите, пока все нажмут рестарт", 1, (255, 0, 0))
        screen.blit(wait, (int(width / 2 - wait.get_width() / 2), 200))
    if playing or went and not game.pressed_restart[id]:
        wait = font.render("Ждите конца игры", 1, (255, 0, 0))
        screen.blit(wait, (int(width / 2 - wait.get_width() / 2), 215))
    elif turn != id and not game.pressed_restart[id]:
        restart_button = pygame.draw.rect(background, (5, 79, 33), (463, 310, 75, 25))
        wait = font.render("Ждите своего хода", 1, (255, 0, 0))
        screen.blit(wait, (int(width / 2 - wait.get_width() / 2), 215))
    else:
        screen.blit(hit_txt, (39, 571))
        screen.blit(stand_txt, (116, 571))

    pygame.display.update()


def main():
    global game, restart_button, id
    run = True
    stand = False
    try:
        game = n.send("name " + name)

        while (run):
            clock.tick(60)

            game = n.send("update")

            id = game.p_names[name]
            player_sum, player_A, game.deal_sum, dealA = (game.player_sum, game.player_A, game.deal_sum, game.deal_A)
            pl_cards = convert_pcards(game.player_cards)
            dealer_cards = convert_cards(game.deal_cards)
            gameover = False
            if len(game.player_cards[id]) != 0 and game.turn == id and not game.over[id] and not game.p_stands[id]:
                hit_button = pygame.draw.rect(background, (192, 192, 192), (10, 570, 75, 20))
                stand_button = pygame.draw.rect(background, (192, 192, 192), (95, 570, 75, 20))
            else:
                hit_button = pygame.draw.rect(background, (5, 79, 33), (10, 570, 75, 20))
                stand_button = pygame.draw.rect(background, (5, 79, 33), (95, 570, 75, 20))

            redraw_window(pl_cards, dealer_cards, gameover, stand, game)

            k_st = True
            for i in range(game.player_count):
                k_st *= game.p_stands[i] + game.over[i]
            stand = k_st

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    n.send("quit")
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover or game.p_stands[id]) and len(game.player_cards[id]) != 0 \
                        and id == game.turn and hit_button.collidepoint(pygame.mouse.get_pos()):
                    game = n.send("hit")
                    gameover = True if (game.player_sum[id] >= 21 and game.player_A[id] == 0) or len(game.player_cards[id]) == 5 else False
                    if len(game.player_cards[id]) == 2 and game.player_sum[id] == 21:
                        gameover = True
                    elif len(dealer_cards) == 2 and game.deal_sum == 21:
                        gameover = True
                    if gameover:
                        if len(game.p_names) - 1 == game.turn or len(game.player_cards[id + 1]) == 0:
                            game = n.send("stand")
                        else:
                            game = n.send("next")

                elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and len(game.player_cards[id]) != 0 \
                        and id == game.turn and stand_button.collidepoint(pygame.mouse.get_pos()):
                    if len(game.p_names) - 1 == game.turn or len(game.player_cards[id+1]) == 0:
                        game = n.send("stand")
                    else:
                        game = n.send("next")
                elif event.type == pygame.MOUSEBUTTONDOWN and (gameover or stand) and (id - game.player_count) < 0\
                        and restart_button.collidepoint(pygame.mouse.get_pos()):
                    game = n.send("restart")

                    gameover = False
                    stand = False

                    restart_button = pygame.draw.rect(background, (5, 79, 33), (463, 310, 75, 25))
    except AttributeError:
        print("Ошибка доступа. Попробуйте зайти под другим именем либо подождите какое-то время.")
        pygame.quit()
        exit()


name = input("Введите свое имя:")
menu_screen(screen, name)
