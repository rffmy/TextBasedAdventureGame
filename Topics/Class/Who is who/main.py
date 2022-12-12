class Angel:
    color = "white"
    feature = "wings"
    home = "Heaven"

class Demon:
    color = "red"
    feature = "horns"
    home = "Hell"


angel = Angel()
demon = Demon()

print("\n".join([angel.color, angel.feature, angel.home]))
print("\n".join([demon.color, demon.feature, demon.home]))
