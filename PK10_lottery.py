def mishi(number):
    n = number.split(',')
    data = ''
    banker = 0
    player1 = 0
    player2 = 0
    player3 = 0
    # 庄：冠、亚军号码的数字相加之和值取个位数
    for c in n[0:2]:
        banker += int(c)
    banker = str(banker)[-1]
    # 闲一：第三、四名号码的数字相加之和值取个位数
    for c in n[2:4]:
        player1 += int(c)
    player1 = str(player1)[-1]
    # 闲二：第五、六名号码的数字相加之和值取个位数
    for c in n[4:6]:
        player2 += int(c)
    player2 = str(player2)[-1]
    # 闲三：第七、八名号码的数字相加之和值取个位数
    for c in n[6:8]:
        player3 += int(c)
    player3 = str(player3)[-1]
    data += '庄 ' + banker + ' 閒一 ' + player1 + ' 閒二 ' + player2 + ' 閒三 ' + player3 + '\n'
    # 庄 闲一 比大小，相等則拆開個別數字比大小
    if int(banker) > int(player1):
        data += '庄\n'
    elif int(banker) < int(player1):
        data += '閒一\n'
    else:
        b1 = n[0]
        b2 = n[1]
        p11 = n[2]
        p12 = n[3]
        if int(banker) == 0:
            data += '庄\n'
        else:
            if int(b1) > int(b2):
                bmax = b1
            else:
                bmax = b2
            if int(p11) > int(p12):
                p1max = p11
            else:
                p1max = p12
            if int(bmax) > int(p1max):
                data += '庄\n'
            else:
                data += '閒一\n'

    if int(banker) > int(player2):
        data += '庄\n'
    elif int(banker) < int(player2):
        data += '閒二\n'
    else:
        b1 = n[0]
        b2 = n[1]
        p21 = n[4]
        p22 = n[5]
        if int(banker) == 0:
            data += '庄\n'
        else:
            if int(b1) > int(b2):
                bmax = b1
            else:
                bmax = b2
            if int(p21) > int(p22):
                p2max = p21
            else:
                p2max = p22
            if int(bmax) > int(p2max):
                data += '庄\n'
            else:
                data += '閒二\n'

    if int(banker) > int(player3):
        data += '庄\n'
    elif int(banker) < int(player3):
        data += '閒三\n'
    else:
        b1 = n[0]
        b2 = n[1]
        p31 = n[6]
        p32 = n[7]
        if int(banker) == 0:
            data += '庄\n'
        else:
            if int(b1) > int(b2):
                bmax = b1
            else:
                bmax = b2
            if int(p31) > int(p32):
                p3max = p31
            else:
                p3max = p32
            if int(bmax) > int(p3max):
                data += '庄\n'
            else:
                data += '閒三\n'
    return data

def fantan(number):
    n = number.split(',')
    s = 0
    data = ''
    # 番号：前三个开奖号和值除以4所得的余数。若余数为0，则番为4。
    for c in n[0:3]:
        s += int(c)
    data += ('和 = ' + str(s) + '\n')
    if s % 4 == 0:
        data += '番號:4  大雙\n' \
                '4番\n' \
                '4念1  4念2  4念3\n' \
                '14角  34角\n' \
                '4正\n' \
                '打和：1念4  2念4  3念4  1正  3正\n'
    elif s % 4 == 1:
        data += '番號:1  小單\n' \
                '1番\n' \
                '1念2  1念3  1念4\n' \
                '12角  14角\n' \
                '1正\n' \
                '打和：2念1  3念1  4念1  2正  4正\n'
    elif s % 4 == 2:
        data += '番號:2  小雙\n' \
                '2番\n' \
                '2念1  2念3  2念4\n' \
                '12角  23角\n' \
                '2正\n' \
                '打和：1念2  3念2  4念2  1正  3正\n'
    else:
        data += '番號:3  大單\n' \
                '3番\n' \
                '3念1  3念2  3念4\n' \
                '23角  34角\n' \
                '3正\n' \
                '打和：1念3  2念3  4念3  2正  4正\n'
    return data

# 百家樂
# 以PK10的开奖结果为取号来源,
# -取冠亚军和的个位数为闲家的第一张牌;
# -取第三、第四位和的个位数为闲家的第二张牌;
# -取第九位为闲家的补牌(如果需要)。
# -取第五、第六位和的个位数为庄家的第一张牌;
# -取第七、第八位和的个位数位庄家的第二张牌;
# -取第十位为庄家的补牌(如果需要)。

def bjl(number):
    n = number.split(',')
    data = ''
    add_banker = 0
    add_player = 0
    banker1_1 = 0
    banker2_1 = 0
    for c in n[4:6]:
        banker1_1 += int(c)
    for c in n[6:8]:
        banker2_1 += int(c)
    banker1 = str(banker1_1)[-1]
    banker2 = str(banker2_1)[-1]

    player1_1 = 0
    player2_1 = 0
    for c in n[0:2]:
        player1_1 += int(c)
    for c in n[2:4]:
        player2_1 += int(c)
    player1 = str(player1_1)[-1]
    player2 = str(player2_1)[-1]
    sum_banker = int(banker1) + int(banker2)
    sum_player = int(player1) + int(player2)

    sum_banker = int(str(sum_banker)[-1])
    sum_player = int(str(sum_player)[-1])
    data += 'sum_banker=' + str(sum_banker) + ' sum_player=' + str(sum_player) + '\n'
    # 禁止補牌
    ban_add = [8, 9]
    # 紀錄張數
    card = 0
    # 閒家是否補牌
    if sum_banker in ban_add or sum_player in ban_add:
        add_banker = 100
        add_player = 100
    elif sum_player < 6 and sum_banker not in ban_add:
        add_player = int(n[8])
        card += 1
    elif 5 < sum_player < 8:
        add_player = 100
    # 10 == 0
    if add_player == 10:
        add_player = 0
    # 莊家是否補牌
    if sum_banker in ban_add or sum_player in ban_add:
        add_banker = 100
        add_player = 100
    elif sum_banker == 7:
        add_banker = 100
    elif sum_banker < 3 and sum_banker not in ban_add:
        add_banker = int(n[9])
        card += 1
    elif sum_banker == 3:
        if sum_player in ban_add or add_player == 8:
            add_banker = 100
        elif sum_player in [6, 7] or add_player != 8:
            add_banker = int(n[9])
            card += 1
    elif sum_banker == 4:
        if sum_player in ban_add or add_player in [0, 1, 8, 9]:
            add_banker = 100
        elif sum_player in [6, 7] or add_player in range(2, 8):
            add_banker = int(n[9])
            card += 1
    elif sum_banker == 5:
        if sum_player in ban_add or add_player in [0, 1, 2, 3, 8, 9]:
            add_banker = 100
        elif sum_player in [6, 7] or add_player in range(4, 8):
            add_banker = int(n[9])
            card += 1
    elif sum_banker == 6:
        if sum_player in ban_add or add_player in [0, 1, 2, 3, 4, 5, 8, 9]:
            add_banker = 100
        elif sum_player in [6, 7] or add_player in [6, 7]:
            add_banker = int(n[9])
            card += 1
    # 10 == 0
    if add_banker == 10:
        add_banker = 0

    if add_player != 100:
        player = int(str(sum_player + add_player)[-1])
        data += '閒點 ' + str(player) + ' 閒牌 ' + player1 + ' ' + player2 + ' ' + str(add_player) + '\n'
    else:
        player = sum_player
        data += '閒點 ' + str(player) + ' 閒牌 ' + player1 + ' ' + player2 + ' X\n'
    if add_banker != 100:
        banker = int(str(sum_banker + add_banker)[-1])
        data += '庄點 ' + str(banker) + ' 庄牌 ' + banker1 + ' ' + banker2 + ' ' + str(add_banker) + '\n'
    else:
        banker = sum_banker
        data += '庄點 ' + str(banker) + ' 庄牌 ' + banker1 + ' ' + banker2 + ' X\n'
    # 庄闲和
    if banker > player:
        data += '庄\n'
    elif banker < player:
        data += '闲\n'
    else:
        data += '和\n'
    # 对子
    if banker1 == banker2:
        data += '庄对\n'
    if player1 == player2:
        data += '闲对\n'
    # 大小
    if card > 0:
        data += '大\n'
    else:
        data += '小\n'
    return data
