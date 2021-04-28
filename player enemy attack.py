import random
playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp >0:
    dmg = random.randrange(enemyatkl,enemyatkh)
    playerhp = playerhp-dmg
    if playerhp <=30:
        playerhp = 30
        print("enemy strikes for",dmg,"points of damage.Current playerhp is ",playerhp)
        if playerhp ==30:
            print("you have been teleported to nearest med center")
            break