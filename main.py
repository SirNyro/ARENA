import sysfunc as sf
import os, sys, random
from stats import attack_name_list, attack_level_list, attack_energy_list, heal_name_list, heal_level_list, heal_energy_list, attack_id, heal_id
import displayMenu as display
from termcolor import colored
from time import sleep
from character import Knight, Wizard
from enemy import Opponent

def createHabilities():
    attack_name_list = []
    attack_level_list = []
    attack_energy_list = []
    attack_id = []

    heal_name_list = []
    heal_level_list = []
    heal_energy_list = []
    heal_id = []

    if player.id == 'Knight':
        for i in range(40): player.new_attack('Slice', player.get_attack() + 3, 1, 1)
        for i in range(player.get_luck()): player.new_attack('Rupture', player.get_attack() + 10, 2, 1)
        for i in range(player.get_luck()-10): player.new_attack('Furybreaker', player.get_attack() + 20, 3, 1)
        for i in range(player.get_luck()-15): player.new_attack('Sword Storm', player.get_attack() + 50, 4, 1)

        for i in range(player.get_luck()-15): player.new_heal('Unicorn Milk', player.get_shield() + 3, 2, 2)
        for i in range(player.get_luck()-20): player.new_heal('Raw Meat', player.get_shield() + 8, 3, 2)
        for i in range(player.get_luck()-25): player.new_heal('Health Potion', player.get_shield() + 14, 4, 2)
        for i in range(player.get_luck()-30): player.new_heal('Reborn', player.get_shield() + 25, 5, 2)

    else:
        for i in range(40): player.new_attack('Fire lasso', player.get_attack() + 5, 1, 1)
        for i in range(player.get_luck()): player.new_attack('Thunderfall', player.get_attack() + 15, 3, 1)
        for i in range(player.get_luck()-13): player.new_attack('Divine carnage', player.get_attack() + 30, 4, 1)
        for i in range(player.get_luck()-18): player.new_attack('Eternal regret', player.get_attack() + 75, 5, 1)

        for i in range(player.get_luck()-5): player.new_heal('Unicorn Blood', player.get_shield() + 4, 2, 2)
        for i in range(player.get_luck()-10): player.new_heal('Scroll of Witness', player.get_shield() + 8, 3, 2)
        for i in range(player.get_luck()-15): player.new_heal('Last Whisper', player.get_shield() + 16, 4, 2)
        for i in range(player.get_luck()-18): player.new_heal("Widow's Wail", player.get_shield() + 32, 5, 2)

def drawFloor(x, drawText):
    print(f"""\n\t\t\t\t\t\tFLOOR {x}\n
    \t\t{colored('YOUR HEALTH', 'cyan')}\t\t\t\t\t\t{colored("ENEMY'S HEALTH", 'red')}
    \t\t{colored(str(player.get_hp()), 'green')}\t\t\t\t\t\t\t\t{colored(str(enemy.get_hp()), 'magenta')}""")
        
    if player.id == 'Knight': display.drawKnight()
    else: display.drawWizard()
    if drawText == True:
        print(colored('\t\tCURRENT ENERGY: ', 'green', 'on_magenta', attrs=['bold']),colored(str(player.get_energy()), 'yellow', attrs=['bold']))
        print(colored('\t\tCARDS------------>', 'green'))

def selectCard(y, g, x, totalDamage, dCards):
    z = 4
    try:
        selectedCard = int(input(colored('\t\tType the number of card you want to use: ', 'white', 'on_cyan')))
    except:
        selectCard(y, g, x, totalDamage, dCards)
    sC = (selectedCard-1)
    if selectedCard == 5 or selectedCard == 5 and player.get_energy() >= 0: return
    if selectedCard == '': selectCard(y, g, x, totalDamage, dCards)
    elif eCList[sC] > player.get_energy(): selectCard(y, g, x, totalDamage, dCards)
    else:
        z = z - 1
        if iCList[sC] == 1:
            player.set_energy(player.get_energy()-eCList[sC])
            enemy.set_hp(enemy.get_hp()-lCList[sC])
            totalDamage = totalDamage + lCList[sC]
            if enemy.get_hp() <=0: return
            if player.id == 'Knight': 
                sf.clear()
                display.drawKnight()
                try:
                    os.system('color 4c')
                    sleep(0.50)
                    os.system('color c4')
                    sleep(0.50)
                    os.system('color 0F')
                except:
                    print("Attacking")
            else: 
                sf.clear()
                try:
                    display.drawWizard()
                    os.system('color 51')
                    sleep(0.50)
                    os.system('color 15')
                    sleep(0.50)
                    os.system('color 0f')
                except:
                    print("Casting spells")
        else:
            player.set_energy(player.get_energy()-eCList[sC])
            player.set_hp(player.get_hp()+lCList[sC])
            if enemy.get_hp() <=0: return
            sf.clear()
            if player.id == 'Knight': display.drawKnight()
            elif player.id == 'Wizard': display.drawWizard()
            try:
                os.system('color a2')
                sleep(0.50)
                os.system('color 7a')
                sleep(0.50)
                os.system('color 0F')
            except:
                print('Healing')
        del nCList[sC]
        del lCList[sC]
        del eCList[sC]
        del iCList[sC]
        sf.clear()
        drawFloor(x, True)
        ct = 0
        for i in range(z):
            ct = ct +1
            card1 = colored(str(ct)+'. ', 'white') + colored(str(nCList[g+i])+' L:'+str(lCList[g+i])+' E:'+str(eCList[g+i]), 'white', 'on_green')
            print('\t\t\t\t'+card1)
        card2 = colored('5. ', 'white') + colored('Pass', 'white', 'on_green')
        print('\t\t\t\t'+card2)
        if player.get_energy() > 0: selectCard(y, g, x, totalDamage, dCards)

def shopping():
    sf.clear()
    display.drawShopTitle()
    sleep(2.5)
    print(colored('1. Amulet (Increases your luck by 20 points)', 'yellow'), colored('$350', 'green'))
    print(colored('2. Health Potion Card (Restores 10 points of health)', 'yellow'), colored('$175', 'green'))
    print(colored('3. Last Whisper Card (Restores 16 points of health)', 'yellow'), colored('$190', 'green'))
    print(colored('4. Forge (Increases base attack damage by 15 points)', 'yellow'), colored('$220', 'green'))
    print(colored('5. Young Blood Elixir (Increases your base energy by 1 point)', 'yellow'), colored('$120', 'green'))
    print(colored('6. Pass', 'cyan'))

    print(colored('\nGold: ', 'green'), colored(str(gold), 'yellow'))
    sh = int(input(colored('Type the number of the object you want to buy: ', 'magenta')))
    if sh == 1:
        if gold >= 350: 
            player.set_luck(player.get_luck()+20)
            if gold > 0: shopping()
        else: shopping()
    elif sh == 2:
        if gold >= 175: 
            player.new_heal('Health Potion', player.get_shield() + 10, 4, 2)
            if gold > 0: shopping()
        else: shopping()
    elif sh == 3:
        if gold >= 190: 
            for i in range(player.get_luck()-15): player.new_heal('Last Whisper', player.get_shield() + 16, 4, 2)
            if gold > 0: shopping()
        else: shopping()
    elif sh == 4:
        if gold >= 220: 
            player.set_attack(player.get_attack()+15)
            if gold > 0: shopping()
        else: shopping()
    elif sh == 5:
        if gold >= 220: 
            player.set_baseEnergy(player.get_baseEnergy()+1)
            if gold > 0: shopping()
        else: shopping()
    elif sh == 6: return
    else: shopping()
    

gold = 100
os.system('color 0F')
display.title()
if int(input(colored('Type the number of the character you want to play: ', 'magenta'))) == 1:
    player = Knight(100, 20, 20, 35, 3, 3)
else: player = Wizard(70, 10, 10, 20, 4, 4)

display.gift()
g = int(input(colored('Type the number of the gift you want: ', 'magenta')))

if g == 1: player.set_hp(player.get_hp()+25)
elif g == 2: gold += 150
elif g == 4: player.set_luck(player.get_luck()+20)
elif g == 5: player.set_energy(player.get_energy()+1)

x = 0
while player.get_hp() > 0:
    sf.clear()
    x = x + 1
    y = 0
    g = -4
    enemy = Opponent((player.get_hp()*(x+1 if player.id == 'Knight' else (x+1.5))), (player.get_attack()*(x+0.5)), (player.get_shield()*1.5))

    if x % 3 == 0: 
        sf.clear()
        display.drawSecure()
        sleep(2.5)
        print(colored("1. Rest (Heals 30%) of your current life)", 'green'))
        print(colored("2. Train (Increases your base attack damage by 10)", 'red'))
        print(colored("Any number. Skip", 'red'))

        sec = int(input(colored('Type the number of action you want to do: ', 'magenta')))
        
        if sec == 1: player.set_hp(player.get_hp()+(player.get_hp()*(0.30)))
        elif sec == 2: player.set_attack(player.get_attack()+10)

        pass
    
    if x % 5 == 0:
        sf.clear()
        display.gift()
        g = int(input(colored('Type the number of the gift you want: ', 'magenta')))

        if g == 1: player.set_hp(player.get_hp()+25)
        elif g == 2: gold += 150
        elif g == 4: player.set_luck(player.get_luck()+20)
        elif g == 5: player.set_energy(player.get_energy()+1)

    if x % 10 == 0:
        sf.clear()
        display.drawLevelUp()
        if player.id == 'Knight':
            player.summon_lightning()
        else:
            player.purify()
        sleep(3.5)

    mer = random.randint(0,4)
    if mer == 4:
        shopping()
        sleep(2.5)

    createHabilities()

    nCList = attack_name_list + heal_name_list
    lCList = attack_level_list + heal_level_list
    eCList = attack_energy_list + heal_energy_list
    iCList = attack_id + heal_id
    d = list(map(list, zip(nCList, lCList, eCList, iCList)))
    random.shuffle(d)
    nCList, lCList, eCList, iCList = list(map(list, zip(*d)))
    
    player.set_energy(player.get_baseEnergy())
    totalDamage = 0
    while enemy.get_hp() > 0:
        if y > 1: 
            if player.get_energy() == 0: player.set_energy(player.get_baseEnergy())
            else: player.set_energy(player.get_energy()+player.get_baseEnergy())
        sf.clear()

        drawFloor(x, True)
        
        g = g + 4
        y = y + 4
        
        ct = 0
        dCards = []
        for i in range(g, y):
            ct = ct + 1
            dCards.append(nCList[i])
            card1 = colored(str(ct)+'. ', 'white') + colored(str(nCList[i])+' L:'+str(lCList[i])+' E:'+str(eCList[i]), 'white', 'on_green')
            print('\t\t\t\t'+card1)
        card2 = colored('5. ', 'white') + colored('Pass', 'white', 'on_green')
        print('\t\t\t\t'+card2)

        selectCard(y, g, x, totalDamage, dCards)
        sf.clear()
        drawFloor(x, False)

        if enemy.get_hp() <=0: break
        sleep(1.5)
        print(colored("\t\t\t\tENEMY'S TURN", 'red'))
        sleep(3)

        if enemy.decide() == 0:
            sf.clear()
            drawFloor(x, False)
            os.system('color c0')
            sleep(0.50)
            os.system('color 40')
            sleep(0.50)
            os.system('color 0F')
            print(colored("\t\t\t\tHE IS ATTACKING YOU!", 'red', 'on_magenta'))
            player.set_hp(player.get_hp() - enemy.get_ap())
            sleep(2.5)
            print(colored("\t\t\t\tYOU RECEIVED ", 'red'), colored(str(enemy.get_ap()), 'yellow'), colored(' POINTS OF DAMAGE!', 'red'))
            sleep(4)
            sf.clear()
            drawFloor(x, False)
        elif enemy.decide() == 1:
            sf.clear()
            drawFloor(x, False)
            os.system('color 26')
            sleep(0.50)
            os.system('color 63')
            sleep(0.50)
            os.system('color 0F')
            print(colored("\t\t\t\tTHE ENEMY IS HEALING", 'red', 'on_magenta'))
            enemy.set_hp(enemy.get_hp() + enemy.get_sp())
            sleep(2.5)
            print(colored("\t\t\t\tTHE ENEMY HEALED", 'red'), colored(str(enemy.get_sp()), 'yellow'), colored(' POINTS!', 'red'))
            sleep(4)
            sf.clear()
            drawFloor(x, False)
        else:
            sf.clear()
            drawFloor(x, False)
            os.system('color 80')
            sleep(0.50)
            os.system('color 09')
            sleep(0.50)
            os.system('color 0F')
            print(colored("\t\t\t\tTHE ENEMY IS THINKING WHAT TO DO", 'red', 'on_magenta'))
            sleep(4)
            sf.clear()
            drawFloor(x, False)
    sleep(3)
    display.drawWin()
    gold = gold + (totalDamage*0.40)
    sleep(3)
sleep(3)
display.drawLose()
sleep(3)