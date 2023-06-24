from game.components.power_ups.shield import Shield

class PowerUpHandler:
    INTERVAL_TIME = 300


    def __init__(self):
        self.power_ups = []
        self.interval_time = 0

    def update(self, player):
        self.interval_time += 1
        if self.interval_time % self.INTERVAL_TIME == 0:
            self.add_power_up()
            self.interval_time = 0
        for power_up in self.power_ups:
            power_up.update(player)
            if power_up.is_used:
                player.activate_power_up(power_up)
            if not power_up.is_alive:
                self.remove_power_up(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def add_power_up(self):
            self.power_ups.append(Shield()) 
        
    def remove_power_up(self, power_up):
        self.power_ups.remove(power_up)

    def reset(self):
        self.power_ups = []
        self.interval_time = 0 