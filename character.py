from stats import General
    
class Knight(General):
    id = 'Knight'
    def summon_lightning(self):
        Knight.set_attack(Knight.get_attack()+75)
        Knight.player.set_health(Knight.get_health()+100)
        Knight.player.set_luck(Knight.get_luck()+50)

class Wizard(General):
    id = 'Magician'
    def purify(self):
        Wizard.set_attack(Wizard.get_attack()+30)
        Wizard.set_health(Wizard.get_health()+120)
        Wizard.set_luck(Wizard.get_luck()+30)