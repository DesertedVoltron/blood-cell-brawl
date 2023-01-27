def enemy_spacer(enemy, enemy_amount, start_time, end_time): # enemy can be anything, rest must be numbers
    length = end_time - start_time
    wave_list = []
    for i in range(1, enemy_amount + 1):
        wave_list.append((enemy, start_time + round((length / enemy_amount) * i, 3))) # rounds to 3 digits, can be forgone or changed if needed
    return wave_list
waves = { # enemy_spacer is fairly self-explanatory, i sorted the ones that have multiple enemies overlapping idk how you're handling the waves so idk if thats necessary, feel free to change the enemy names
    1: enemy_spacer("red", 20, 0, 17.51),
    2: enemy_spacer("red", 35, 0, 19),
    3: enemy_spacer("red", 10, 0, 5.1) + enemy_spacer("blue", 5, 5.7, 7.95) + enemy_spacer("red", 15, 9.71, 16.71),
    4: sorted(enemy_spacer("red", 25, 0, 12) + enemy_spacer("blue", 18, 7.9, 10.4) + enemy_spacer("red", 10, 14.51, 17.31)),
    5: enemy_spacer("blue", 12, 0, 5.14) + enemy_spacer("red", 5, 5.7, 7.98) + enemy_spacer("blue", 15, 8.6, 16.5),
    6: enemy_spacer("green", 4, 0, 1.71) + enemy_spacer("red", 15, 5.33, 10.33) + enemy_spacer("blue", 15, 10.8, 18.7),
    7: enemy_spacer("blue", 10, 0, 5.14) + enemy_spacer("green", 5, 5.7, 10.65) + enemy_spacer("red", 20, 11.81, 22.65) + enemy_spacer("blue", 10, 22.81, 26.8),
    8: enemy_spacer("blue", 20, 0, 10.84) + enemy_spacer("green", 2, 11.42, 11.99) + enemy_spacer("red", 10, 14.03, 16) + enemy_spacer("green", 12, 18.27, 28.87),
    9: enemy_spacer("green", 30, 0, 18.95),
    10: enemy_spacer("blue", 60, 0, 35) + enemy_spacer("blue", 20, 35, 44) + enemy_spacer("blue", 22, 44, 47.99),
    11: sorted(enemy_spacer("yellow", 3, 0, 1) + enemy_spacer("green", 12, 4.47, 10.75) + enemy_spacer("blue", 10, 10.87, 14.67) + enemy_spacer("red", 10, 14.59, 19.16)),
    12: enemy_spacer("green", 10, 0, 5.13) + enemy_spacer("blue", 15, 5.7, 11.77) + enemy_spacer("yellow", 5, 14.27, 17.39),
    13: sorted(enemy_spacer("blue", 50, 0, 30) + enemy_spacer("green", 23, 2.21, 32.21)),
    14: sorted(enemy_spacer("red", 18, 0, 9.71) + enemy_spacer("blue", 5, 2.85, 3.97) + enemy_spacer("green", 5, 5.71, 6.83) + enemy_spacer("yellow", 4, 8.56, 9.51) + enemy_spacer("red", 31, 9.5, 26.63) + enemy_spacer("blue", 10, 15.96, 17.34) + enemy_spacer("green", 5, 19.84, 21.22) + enemy_spacer("yellow", 5, 23.71, 25.26)),
    15: sorted(enemy_spacer("red", 20, 0, 25) + enemy_spacer("blue", 15, 2.78, 22.78) + enemy_spacer("green", 12, 5.68, 20.68) + enemy_spacer("yellow", 10, 8.87, 20.87) + enemy_spacer("pink", 5, 17.55, 20.55)),
    16: sorted(enemy_spacer("green", 20, 0, 10.85) + enemy_spacer("green", 20, .2, 11.05) + enemy_spacer("yellow", 8, 14.59, 16.02)),
    17: enemy_spacer("yellow", 12, 0, 5), # regrow yellows
    18: enemy_spacer("green", 60, 0, 25) + enemy_spacer("green", 20, 25, 26.82),
    19: sorted(enemy_spacer("green", 10, 0, 2.89) + enemy_spacer("yellow", 5, 2.85, 5.19) + enemy_spacer("pink", 15, 5.96, 13.57) + enemy_spacer("yellow", 4, 13.48, 15.76)), # first set of yellows is regrow
    20: enemy_spacer("black", 6, 0, 5.25)
}
