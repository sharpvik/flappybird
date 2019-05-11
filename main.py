from lib.alter import Alter
from lib.game import FlappyBird


alt = Alter()
if alt.s is None or alt.g is None: exit()
game = FlappyBird(alt.g, alt.s)
