from manimpp.constants import *
from manimpp.for_3b1b_videos.pi_creature import PiCreature
from manimpp.mobject.types.vectorized_mobject import VGroup


class PiCreatureClass(VGroup):
    CONFIG = {
        "width": 3,
        "height": 2
    }

    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        for i in range(self.width):
            for j in range(self.height):
                pi = PiCreature().scale(0.3)
                pi.move_to(i * DOWN + j * RIGHT)
                self.add(pi)
