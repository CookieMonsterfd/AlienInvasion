class Settings:
    """Клас, який зберігає всі налаштування для гри"""

    def __init__(self):
        
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230,230,230) #rgb format
        self.game_caption = 'Alien Invasion'

        #Ship settings
        self.ship_speed = 1.5