import time
from datetime import datetime
from turtle import Turtle
from constantes import MAX_LNG, MAX_Y_LAT, MAX_LAT, MAX_X_LNG
from data_manager import iss_pos


def convert_coor_axe(lat, lng):
    x = (MAX_X_LNG * lng) / MAX_LNG
    y = (((MAX_Y_LAT * lat) / MAX_LAT) * 0.88) - 30
    return x, y


class ISS(Turtle):
    def __init__(self):
        super().__init__()
        super().penup()
        super().hideturtle()
        self.lat, self.lng = iss_pos()
        self.refresh_pos(self.lat, self.lng)
        super().showturtle()
        super().pendown()

    def refresh_pos(self, lat, lng):
        x, y = convert_coor_axe(lat, lng)
        self.goto(x, y)

    def process_pos_iss(self):
        while True:
            self.lat, self.lng = iss_pos()
            # Mettre la comparaison précédente valeur / nouvelle valeur + lever de stylo
            self.refresh_pos(self.lat, self.lng)
            time.sleep(2)

    def proto_screenshot(self):
        now = datetime.now()
        if now.minute in [0, 15, 30, 45]:
            ts = super().getscreen()
            # ts.getcanvas().postscript(file=f"iss_{now}.eps") # Initial
            ts.getcanvas().postscript(file=f"iss_{now}.png")  # test

    # Ajout de la gestion du passage de droite de la map à gauche de la map et inversement
    # Pour cela, garder en mémoire la précédente lat et lng (à l'initialisation juste stocker la 1ere valeur)
    # Comparer le signe de la précédente valeur avec la valeur actuelle -> faire le traitement
    # La nouvelle valeur devient ancienne valeur puis on reload le process
    # Ne pas oublier de lever le stylo si jamais on passe de droite vers la gauche
