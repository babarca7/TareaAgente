class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update_pos(self, new_direction):
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
        updated_pos = []
        updated_pos.append(self.x)
        updated_pos.append(self.y)
        return updated_pos
