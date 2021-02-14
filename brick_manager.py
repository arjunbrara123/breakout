from brick import Brick

COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]


class BrickManager:

    def __init__(self):
        super().__init__()
        self.all_bricks = set()

    def setup_bricks(self):
        for iColour in range(6):
            for iXPos in range(15):
                brick = Brick(COLOURS[iColour], iXPos*50 - 350, iColour*30 + 80)
                self.all_bricks.add(brick)

    def remove_brick(self):
        pass