# start a RockBand here
class RockBand:
    genre = "rock"
    n_members = 4
    key_instruments = ["electric guitar", "drums"]

    def method(self):
        return self.genre, self.n_members, self.key_instruments

my_band = RockBand()
print(my_band.genre)
print(my_band.n_members)
print(my_band.key_instruments)
