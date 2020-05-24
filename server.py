import socket
from _thread import *
from game import Game
import pickle
import random
import copy

server = "192.168.0.103"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cards = ["d_A", "c_A", "h_A", "s_A",
         "d_2", "c_2", "h_2", "s_2",
         "d_3", "c_3", "h_3", "s_3",
         "d_4", "c_4", "h_4", "s_4",
         "d_5", "c_5", "h_5", "s_5",
         "d_6", "c_6", "h_6", "s_6",
         "d_7", "c_7", "h_7", "s_7",
         "d_8", "c_8", "h_8", "s_8",
         "d_9", "c_9", "h_9", "s_9",
         "d_10", "c_10", "h_10", "s_10",
         "d_J", "c_J", "h_J", "s_J",
         "d_Q", "c_Q", "h_Q", "s_Q",
         "d_K", "c_K", "h_K", "s_K"]
cardA = ["d_A", "c_A", "h_A", "s_A"]
card2 = ["d_2", "c_2", "h_2", "s_2"]
card3 = ["d_3", "c_3", "h_3", "s_3"]
card4 = ["d_4", "c_4", "h_4", "s_4"]
card5 = ["d_5", "c_5", "h_5", "s_5"]
card6 = ["d_6", "c_6", "h_6", "s_6"]
card7 = ["d_7", "c_7", "h_7", "s_7"]
card8 = ["d_8", "c_8", "h_8", "s_8"]
card9 = ["d_9", "c_9", "h_9", "s_9"]
card10 = ["d_10", "c_10", "h_10", "s_10",
          "d_J", "c_J", "h_J", "s_J",
          "d_Q", "c_Q", "h_Q", "s_Q",
          "d_K", "c_K", "h_K", "s_K"]

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen()
print("Server Started")

connections = 0
players = 0
id = 0
turn = 0
player_names = {}
cplayer_names = {}
game_run = False
restart_count = 0


def init(player_n, cards_list, player_cards, dealer_cards):
    player_A = []
    user_sum = []
    dealer_A = 0
    if player_n == 1:
        card1, cA = generate_card(cards_list, player_cards[0])
        player_A.append(cA)
        card2, cA = generate_card(cards_list, dealer_cards)
        dealer_A += cA
        card3, cA = generate_card(cards_list, player_cards[0])
        player_A[0] += cA
        card4, cA = generate_card(cards_list, dealer_cards)
        dealer_A += cA
        user_sum.append(get_amount(card1) + get_amount(card3))
        player_A.append(0)
        player_A.append(0)
        user_sum.append(0)
        user_sum.append(0)
        return user_sum, player_A, get_amount(card2) + get_amount(card4), dealer_A
    elif player_n == 2:
        card1, cA = generate_card(cards_list, player_cards[0])
        player_A.append(cA)
        card2, cA = generate_card(cards_list, player_cards[1])
        player_A.append(cA)
        card3, cA = generate_card(cards_list, dealer_cards)
        dealer_A += cA
        card4, cA = generate_card(cards_list, player_cards[0])
        player_A[0] += cA
        card5, cA = generate_card(cards_list, player_cards[1])
        player_A[1] += cA
        card6, cA = generate_card(cards_list, dealer_cards)
        dealer_A += cA
        user_sum.append(get_amount(card1) + get_amount(card4))
        user_sum.append(get_amount(card2) + get_amount(card5))
        player_A.append(0)
        user_sum.append(0)
        return user_sum, player_A, get_amount(card3) + get_amount(card6), dealer_A
    elif player_n == 3:
        card1, cA = generate_card(cards_list, player_cards[0])
        player_A.append(cA)
        card2, cA = generate_card(cards_list, player_cards[1])
        player_A.append(cA)
        card3, cA = generate_card(cards_list, player_cards[2])
        player_A.append(cA)
        card4, cA = generate_card(cards_list, dealer_cards)
        dealer_A += cA
        card5, cA = generate_card(cards_list, player_cards[0])
        player_A[0] += cA
        card6, cA = generate_card(cards_list, player_cards[1])
        player_A[1] += cA
        card7, cA = generate_card(cards_list, player_cards[2])
        player_A[2] += cA
        card8, cA = generate_card(cards_list, dealer_cards)
        dealer_A += cA
        user_sum.append(get_amount(card1) + get_amount(card5))
        user_sum.append(get_amount(card2) + get_amount(card6))
        user_sum.append(get_amount(card3) + get_amount(card7))
        return user_sum, player_A, get_amount(card4) + get_amount(card8), dealer_A


def get_amount(card):
    if card in cardA:
        return 11
    elif card in card2:
        return 2
    elif card in card3:
        return 3
    elif card in card4:
        return 4
    elif card in card5:
        return 5
    elif card in card6:
        return 6
    elif card in card7:
        return 7
    elif card in card8:
        return 8
    elif card in card9:
        return 9
    elif card in card10:
        return 10
    else:
        print('get_amount broke')
        exit()


def generate_card(cards_list, ap_list):
    cA = 0
    card = random.choice(cards_list)
    cards_list.remove(card)
    ap_list.append(card)
    if card in cardA:
        cA = 1
    return card, cA


def generate_cards(cards_list, ap_list):
    cA = 0
    temp = ap_list
    card = random.choice(cards_list)
    cards_list.remove(card)
    temp.append(card)
    if card in cardA:
        cA = 1
    return card, cA, temp


g = Game()


def get_id(p_name):
    return player_names[p_name]


def threaded_client(connection):
    global connections, players, id, game_run, g, turn, restart_count, cplayer_names, player_names
    name = ""
    k_sh = 0
    ccards = copy.copy(cards)
    players_cards = [[],[],[]]
    dealer_cards = []
    data_string = pickle.dumps(g)
    connection.send(data_string)
    connections += 1
    if connections > 3:
        connection.close()
    while True:
        try:
            d = connection.recv(2048 * 8)
            data = d.decode("utf-8")
            if not d:
                print("Disconnected")
                break
            else:
                if len(ccards) <= len(cards) / 3:
                    print("shuffle")
                    ccards = copy.copy(cards)
                if data.count("name") > 0:
                    name = data.split(" ")[1]
                    if name in player_names:
                        connections -= 1
                        connection.close()
                    else:
                        if players == 0:
                            id = 0
                            player_names[name] = id
                            player_names[name] = id
                            cplayer_names = player_names.copy()
                            id += 1
                            g.is_running = True
                            game_run = True
                            players += 1
                            g.player_sum, g.player_A, g.deal_sum, g.deal_A = init(players, ccards, players_cards, dealer_cards)
                            g.deal_cards = dealer_cards
                            g.player_cards = players_cards
                            print(dealer_cards, players_cards)
                            turn = 0
                        else:
                            if id > 2:
                                id = 2
                            player_names[name] = id
                            cplayer_names = player_names.copy()
                            id += 1
                if data == "hit":
                    print("hit")
                    players_cards = g.player_cards
                    card, cA, oneplayers_cards = generate_cards(ccards, players_cards[cplayer_names[name]])
                    players_cards[cplayer_names[name]] = oneplayers_cards
                    g.player_A[cplayer_names[name]] += cA
                    g.player_sum[cplayer_names[name]] += get_amount(card)
                    g.player_cards = players_cards
                    for i in range(3):
                        while g.player_sum[i] > 21 and g.player_A[i] > 0:
                            g.player_A[i] -= 1
                            g.player_sum[i] -= 10
                    print(g.deal_cards, players_cards)
                if data == "next":
                    turn += 1
                    g.p_stands[cplayer_names[name]] = True
                    if len(cplayer_names) != len(player_names) and connections == 2:
                        if 0 in player_names.values():
                            turn += 1
                if data == "stand":
                    print("все походили")
                    maxi = 0
                    for i in range(players):
                        if g.player_sum[i] <= 21 and g.player_sum[i] > maxi:
                            maxi = g.player_sum[i]
                    while g.deal_sum <= maxi and g.deal_sum < 17:
                        dealer_cards = g.deal_cards
                        card, cA = generate_card(ccards, dealer_cards)
                        g.deal_A += cA
                        g.deal_sum += get_amount(card)
                        g.deal_cards = dealer_cards
                        while g.deal_sum > 21 and g.deal_A > 0:
                            g.deal_A -= 1
                            g.deal_sum -= 10
                        print(g.deal_sum, g.player_sum)
                    if maxi >= g.deal_sum or g.deal_sum > 21:
                        indices = [i for i, x in enumerate(g.player_sum) if x == max(g.player_sum)]
                        for k, v in cplayer_names.items():
                            if v in indices:
                                g.winners.append(k)
                    g.is_running = False
                    game_run = False
                    turn = 0
                    g.p_stands[cplayer_names[name]] = True
                if data == "gameover":
                    turn += 1
                    if players != len(player_names):
                        turn += 1
                    g.over[cplayer_names[name]] = True
                if data == "quit":
                    if players == 1:
                        connections -= 1
                        restart_count = 0
                        dealer_cards = []
                        players_cards = [[], [], []]
                        g.is_running = False
                        game_run = False
                        g.p_stands = [False, False, False]
                        g.over = [False, False, False]
                        g.pressed_restart = [False, False, False]
                        g.winners = []
                        g.deal_cards = dealer_cards
                        g.player_cards = players_cards
                        g.player_count = 0
                        if connections >= 1:
                            g.player_sum, g.player_A, g.deal_sum, g.deal_A = init(connections, ccards, players_cards, dealer_cards)
                            g.deal_cards = dealer_cards
                            g.player_cards = players_cards
                            counter = 0
                            del player_names[name]
                            for p in player_names:
                                player_names[p] = counter
                                counter += 1
                            cplayer_names = player_names.copy()
                            del g.p_names[name]
                            turn = 0
                            print(dealer_cards, players_cards)
                        else:
                            player_names = {}
                    else:
                        del player_names[name]
                        connections -= 1
                        if turn == cplayer_names[name]:
                            turn += 1
                        g.p_stands[cplayer_names[name]] = True
                if data == "restart":
                    g.pressed_restart[cplayer_names[name]] = True
                    restart_count += 1
                    if connections < players:
                        players = connections
                    if restart_count == players:
                        counter = 0
                        for p in player_names:
                            player_names[p] = counter
                            counter += 1
                        restart_count = 0
                        dealer_cards = []
                        players_cards = [[], [], []]
                        g.is_running = True
                        game_run = True
                        g.p_stands = [False, False, False]
                        g.over = [False, False, False]
                        g.pressed_restart = [False, False, False]
                        g.winners = []
                        g.player_sum, g.player_A, g.deal_sum, g.deal_A = init(connections, ccards, players_cards, dealer_cards)
                        g.deal_cards = dealer_cards
                        g.player_cards = players_cards
                        cplayer_names = player_names.copy()
                        turn = 0
                        print(dealer_cards, players_cards)
                g.player_count = players
                g.p_names = cplayer_names

            cnt = 0
            for c in g.player_cards:
                if len(c) != 0:
                    cnt += 1
            players = cnt
            if connections == 0:
                players = 0
            g.turn = turn
            connection.sendall(pickle.dumps(g))
        except socket.error:
            break

    print("Lost connection")
    connection.close()


while True:
    connection, address = s.accept()
    print("Connected to:", address)

    start_new_thread(threaded_client, (connection,))