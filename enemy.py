import random
from stats import General
class Opponent():
    def __init__(self, health_points, attack_points, shield_points):
        self.health_points = health_points
        self.attack_points = attack_points
        self.shield_points = shield_points

    def get_hp(self): return self.health_points
    def get_ap(self): return self.attack_points
    def get_sp(self): return self.shield_points
    
    def set_hp(self, n): self.health_points = n
    def set_ap(self, n): self.attack_points = n
    def set_sp(self, n): self.shield_points = n

    def decide(self):
        de = random.randint(0,2)
        return de
            