#Cathy Doherty
class Ambulance:
    """This is an ambulance that will drive patients to the emergency room.
    it's attributes are priority, speed, and capacity."""

amb = Ambulance()

amb.priority = 0
amb.speed = 100
amb.capacity = 4

import math
def urgent(priority, speed, capacity):
    controlled_velocity = -10 *(1-priority) + math.log(50) * (speed+2.2)**2 + 5 * (capacity+1)
    return controlled_velocity

print (urgent(amb.priority, amb.speed, amb.capacity))
