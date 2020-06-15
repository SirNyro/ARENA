from stats import General
    
class Knight(General):
    id = 'Knight'
    def summon_lightning(self, player):
        player.set_attack(player.get_attack()+20)
        player.set_health(player.get_health()+40)
        player.set_luck(player.get_luck()+20)

class Wizard(General):
    id = 'Magician'
    def purify(self, player):
        player.set_attack(player.get_attack()+10)
        player.set_health(player.get_health()+60)
        player.set_luck(player.get_luck()+10)