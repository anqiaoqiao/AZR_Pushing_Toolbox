def ship_xp(level, isnormal):
    # desribe: input ship level, output ship total xp.
    # ship XP function for azur lane JP/EN version
    # convert level to XP <1-120>
    # unnormal ship: DR and UR
    exp = 0
    if isnormal:
        if 1 <= level <= 40:
            an = 100 * (level - 1)
            exp = int(0.5 * an * level)
        elif 41 <= level <= 60:
            an = 4000 + 200 * (level - 41)
            exp = int(0.5 * (4000 + an) * (level - 40)) + 78000
        elif 61 <= level <= 69:
            an = 8000 + 300 * (level - 61)
            exp = int(0.5 * (8000 + an) * (level - 60)) + 196000
        elif level == 70:
            exp = 289500
        elif 71 <= level <= 79:
            an = 12100 + 440 * (level - 71)
            exp = int(0.5 * (12100 + an) * (level - 70)) + 289500
        elif level == 80:
            exp = 430300
        elif 81 <= level <= 89:
            an = 17250 + 575 * (level - 81)
            exp = int(0.5 * (17250 + an) * (level - 80)) + 430300
        elif level == 90:
            exp = 628675
        elif 91 <= level <= 99:
            l = [1, 1, 2, 2, 4, 5, 5, 20, 72]
            exp = 628675
            an = 24000
            for i in range(level - 90):
                exp += an
                an += 1200 * l[i]
        elif level == 100:
            exp = 1120675
        elif 101 <= level <= 104:
            an = 70000 + 2000 * (level - 101)
            exp = int(0.5 * (70000 + an) * (level - 100)) + 1120675
        elif level == 105:
            exp = 1490675
        elif 106 <= level <= 110:
            an = 85000 + 12000 * (level - 106)
            exp = int(0.5 * (85000 + an) * (level - 105)) + 1490675
        elif 111 <= level <= 120:
            l = [18, 18, 18, 18, 18, 21, 21, 21, 21, 0]
            exp = 2035675
            an = 145000
            for i in range(level - 110):
                exp += an
                an += 1000 * l[i]
        else:
            return -1
    else:
        if 1 <= level <= 40:
            an = 120 * (level - 1)
            exp = int(0.5 * an * level)
        elif 41 <= level <= 60:
            an = 4800 + 240 * (level - 41)
            exp = int(0.5 * (4800 + an) * (level - 40)) + 93600
        elif 61 <= level <= 69:
            an = 9600 + 360 * (level - 61)
            exp = int(0.5 * (9600 + an) * (level - 60)) + 235200
        elif level == 70:
            exp = 347400
        elif 71 <= level <= 79:
            an = 13200 + 480 * (level - 71)
            exp = int(0.5 * (13200 + an) * (level - 70)) + 347400
        elif level == 80:
            exp = 501000
        elif 81 <= level <= 89:
            an = 18000 + 600 * (level - 81)
            exp = int(0.5 * (18000 + an) * (level - 80)) + 501000
        elif level == 90:
            exp = 708000
        elif 91 <= level <= 99:
            l = [1, 1, 2, 2, 4, 5, 5, 20, 72]
            exp = 708000
            an = 26000
            for i in range(level - 90):
                exp += an
                an += 1300 * l[i]
        elif level == 100:
            exp = 1241000
        elif 101 <= level <= 104:
            an = 84000 + 2400 * (level - 101)
            exp = int(0.5 * (84000 + an) * (level - 100)) + 1241000
        elif level == 105:
            exp = 1685000
        elif 106 <= level <= 110:
            an = 102000 + 14400 * (level - 106)
            exp = int(0.5 * (102000 + an) * (level - 105)) + 1685000
        elif 111 <= level <= 120:
            l = [216, 216, 216, 216, 216, 252, 252, 252, 252, 0]
            exp = 2339000
            an = 174000
            for i in range(level - 110):
                exp += an
                an += 100 * l[i]
        else:
            return -1
    return exp

def commander_supply(level):
    # desribe: input commander level, output oil and gold limitation
    if 1 <= level <= 200:
        oil = 1000 + 100 * (level - 1)
        gold = 6000 + 600 * (level - 1)
        return oil, gold
    else:
        return -1

def chapter_xp(cht, sec, isemo=True, ismvp=True, isflag=True):
    # describe: input chatper index, output total xp and average xp per acess
    # defualt: Rank S victory, normal difficulty, average enemy level
    # defualt: auto-battle mode
    # Event chatper: A-14, B-15, C-16, D-17, SP-18
    basic_xp = [
        [240, 456, 492, 756],  # chapter 1
        [666, 949, 1033, 1120],  # chapter 2
        [1205, 1290, 1375, 1462],  # chapter 3
        [1545, 1637, 1718, 2218],  # chapter 4
        [2324, 2430, 2522, 2641],  # chapter 5
        [2744, 2852, 2955, 3635],  # chapter 6
        [3719, 3803, 3886, 3970],  # chapter 7
        [3236, 3306, 3376, 3438],  # chapter 8
        [4172, 4255, 4337, 4420],  # chapter 9
        [5222, 5273, 5368, 5463],  # chapter 10
        [6947, 7012, 7065, 7131],  # chapter 11
        [7255, 7310, 7372, 7429],  # chapter 12
        [7545, 7600, 7660, 8769],  # chapter 13
        [784, 1029, 1212],  # chapter A
        [1579, 2298, 2528],  # chapter B
        [2676, 2859, 3619],  # chapter C
        [4053, 4951, 5206],  # chapter D
        [6377]  # chapter sp
    ]
    basic_acess = [
        [2, 3, 3, 4],  # chapter 1
        [3, 4, 4, 4],  # chapter 2
        [4, 4, 4, 4],  # chapter 3
        [4, 4, 4, 5],  # chapter 4
        [5, 5, 5, 5],  # chapter 5
        [5, 5, 5, 6],  # chapter 6
        [6, 6, 6, 6],  # chapter 7
        [5, 5, 5, 5],  # chapter 8
        [6, 6, 6, 6],  # chapter 9
        [7, 7, 7, 7],  # chapter 10
        [7, 7, 7, 7],  # chapter 11
        [7, 7, 7, 7],  # chapter 12
        [7, 7, 7, 8],  # chapter 13
        [4, 5, 5],  # chapter A
        [5, 6, 6],  # chapter B
        [5, 5, 6],  # chapter C
        [6, 7, 7],  # chapter D
        [8]  # chapter sp
    ]
    if isemo:
        ratio_emo = 1.2
    else:
        ratio_emo = 1
    if ismvp:
        ratio_mvp = 2
    else:
        ratio_mvp = 1
    if isflag:
        ratio_flag = 1.5
    else:
        ratio_flag = 1.5
    xp = basic_xp[cht - 1][sec - 1] * ratio_emo * ratio_mvp * ratio_flag * 1.2
    xp_per_acess = xp / basic_acess[cht - 1][sec - 1]
    return round(xp, 2), round(xp_per_acess, 2)

def chapter_diffculty(cht, sec, aver_level, antiair, air_ctrl, front_num, back_num):
    # defualt: cycle mode, normal mode
    recommend_air_ctrl = [
        [120, 120, 120, 120],  # chapter 1
        [120, 120, 120, 120],  # chapter 2
        [120, 132, 152, 184],  # chapter 3
        [128, 144, 164, 188],  # chapter 4
        [224, 260, 308, 360],  # chapter 5
        [236, 268, 304, 340],  # chapter 6
        [388, 444, 500, 560],  # chapter 7
        [616, 676, 740, 804],  # chapter 8
        [876, 952, 1032, 1108],  # chapter 9
        [1204, 1300, 1400, 1500],  # chapter 10
        [1584, 1676, 1768, 1864],  # chapter 11
        [1968, 2076, 2184, 2296],  # chapter 12
        [2408, 2548, 2692, 2832],  # chapter 13
        [120, 176, 291],  # chapter A
        [249, 395, 384],  # chapter B
        [811, 956, 1185],  # chapter C
        [1133, 1570, 1539],  # chapter D
        [2640]  # chapter sp
    ]
    enemy_level = [
        [2, 4, 6, 10],  # chapter 1
        [12, 15, 18, 21],  # chapter 2
        [24, 27, 30, 33],  # chapter 3
        [36, 39, 42, 45],  # chapter 4
        [48, 51, 54, 57],  # chapter 5
        [60, 63, 66, 69],  # chapter 6
        [72, 74, 76, 78],  # chapter 7
        [80, 82, 84, 86],  # chapter 8
        [89, 91, 93, 95],  # chapter 9
        [96, 98, 100, 102],  # chapter 10
        [104, 105, 106, 107],  # chapter 11
        [108, 110, 112, 114],  # chapter 12
        [116, 118, 120, 121],  # chapter 13
        [25, 30, 35],  # chapter A
        [45, 55, 60],  # chapter B
        [75, 80, 85],  # chapter C
        [95, 100, 105],  # chapter D
        [110]  # chapter sp
    ]

    # damage decrease: antiair: higher is easy
    dd_antiair = (antiair) / (150 + antiair)

    # airctrl gain: higher is easy
    airctrl_diff = (air_ctrl - recommend_air_ctrl[cht - 1][sec - 1])
    dd_airctrl = 1 + (airctrl_diff / (recommend_air_ctrl[cht - 1][sec - 1]) * 0.5)

    # level gain: higher is easy
    level_diff = (aver_level - enemy_level[cht - 1][sec - 1])
    if 0 <= level_diff <= 25:
        dd_level = 0.04 * level_diff
    elif level_diff > 25:
        dd_level = 1
    else:
        dd_level = 0

    # burn or airforce gain: higher is easy
    if 10 <= cht <= 13:
        dd_burn_air = 0
    else:
        dd_burn_air = 1

    # fleetscale gain
    dd_fleetscale = (front_num + back_num) / 6

    # difficulty_ratio: lower is safe
    difficulty_ratio = 1 / (dd_antiair + dd_airctrl + dd_level + dd_fleetscale + dd_burn_air)
    return round(difficulty_ratio, 2)
