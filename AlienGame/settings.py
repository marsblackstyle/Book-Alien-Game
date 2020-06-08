# Einen Klassen Namen kann man defenieren wie man mag 
class Settings: 
    
    """ A class to store all settings for Alien Invasion. """
    # init wird von Python austomatisch erstellt und ist eine Art Konstruktor
    # Zweck: verhinder, dass Standardmethodennamen von Python in einen Konflikt geraten
    # Self: ist immer erforderlich, da diese Methode sich immer selber aufrufen muss
    
    def __init__(self):
        """ Initialize the game's settings. """
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 10



