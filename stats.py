from termcolor import colored

attack_name_list = []
attack_level_list = []
attack_energy_list = []
attack_id = []

heal_name_list = []
heal_level_list = []
heal_energy_list = []
heal_id = []

class General():
    def __init__(self, health_points, shield, attack_points, luck, energy, baseEnergy):
        self.nickname = input(colored('Type the name of the characer: ', 'magenta'))
        self.health_points = health_points
        self.shield = shield
        self.attack_points = attack_points
        self.luck = luck
        self.energy = energy
        self.baseEnergy = baseEnergy

    def get_hp(self):
        return self.health_points
    
    def set_hp(self, n):
        self.health_points = n
    
    def get_shield(self):
        return self.shield

    def set_shield(self, n):
        self.shield = n
    
    def get_luck(self):
        return self.luck
    
    def set_luck(self, n):
        self.luck = n

    def get_attack(self):
        return self.attack_points
    
    def set_attack(self, n):
        self.attack_points = n
    
    def new_attack(self, name, attack, energy, id):
        attack_name_list.append(name)
        attack_level_list.append(attack)
        attack_energy_list.append(energy)
        attack_id.append(id)
    
    def new_heal(self, name, heal, energy, id):
        heal_name_list.append(name)
        heal_level_list.append(heal)
        heal_energy_list.append(energy)
        heal_id.append(id)
    
    def get_energy(self):
        return self.energy

    def set_energy(self, n):
        self.energy = n
    
    def get_baseEnergy(self):
        return self.baseEnergy

    def set_baseEnergy(self, n):
        self.energy = n

    