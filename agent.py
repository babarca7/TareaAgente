class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.times_in_border = 0
        self.strategy = ""

    def update_pos(self, new_direction, is_using_exits):
        if not is_using_exits:
            if new_direction == 1:
                self.x -= 1
                self.y -= 1
            elif new_direction == 2:
                self.y -= 1
            elif new_direction == 3:
                self.x += 1
                self.y -= 1
            elif new_direction == 4:
                self.x -= 1
            elif new_direction == 6:
                self.x += 1
            elif new_direction == 7:
                self.x -= 1
                self.y += 1
            elif new_direction == 8:
                self.y += 1
            else:
                self.x += 1
                self.y += 1
        else:
            self.strategy = "Teleportation"
            self.x = new_direction[0]
            self.y = new_direction[1]
        return [self.x, self.y]
