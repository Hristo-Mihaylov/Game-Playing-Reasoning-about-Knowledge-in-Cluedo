class Room:

    def __init__(self, name):
        self.name = name
        self.neighbours = [self]
        self.has_secret_passage = False
    
    def set_neighbour(self, room):
        self.neighbours.append(room)
        room.neighbours.append(self)

    def set_secret_passage(self, room):
        self.has_secret_passage = True
        room.has_secret_passage = True
        self.set_neighbour(room)
