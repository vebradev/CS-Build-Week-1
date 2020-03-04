from django.contrib.auth.models import User
from adventure.models import Player, Room

Room.objects.all().delete()

r_one = Room(title="1", description="Room 1")
r_two = Room(title="2", description="Room 2")
r_three = Room(title="3", description="Room 3")
r_four = Room(title="4", description="Room 4")
r_five = Room(title="5", description="Room 5")
r_six = Room(title="6", description="Room 6")
r_seven = Room(title="7", description="Room 7")
r_eight = Room(title="8", description="Room 8")
r_nine = Room(title="9", description="Room 9")

r_one.save()
r_two.save()
r_three.save()
r_four.save()
r_five.save()
r_six.save()
r_seven.save()
r_eight.save()
r_nine.save()

# Link rooms together
r_one.connectRooms(r_two, "e")
r_two.connectRooms(r_one, "w")

r_one.connectRooms(r_four, "s")
r_four.connectRooms(r_one, "n")

r_four.connectRooms(r_five, "e")
r_five.connectRooms(r_four, "w")

r_five.connectRooms(r_six, "e")
r_six.connectRooms(r_five, "w")

r_three.connectRooms(r_six, "s")
r_six.connectRooms(r_three, "n")

r_five.connectRooms(r_eight, "s")
r_eight.connectRooms(r_five, "n")

r_seven.connectRooms(r_eight, "e")
r_eight.connectRooms(r_seven, "w")

r_eight.connectRooms(r_nine, "e")
r_nine.connectRooms(r_eight, "w")

players = Player.objects.all()
for p in players:
    p.currentRoom = r_one.id
    p.save()
