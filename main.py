from iss import ISS
import turtle


screen = turtle.Screen()
screen.setup(1470, 890)
screen.bgpic("Carte_du_monde_crete.png")

iss = ISS()
iss.process_pos_iss()


