s = input()
c = input()

if s == "1":
    print("Photon Boson")
elif s == "1/2":
    if c == "0":
        print("Neutrino Lepton")
    elif c == "-1":
        print("Electron Lepton")
    elif c == "2/3":
        print("Charm Quark")
    elif c == "-1/3":
        print("Strange Quark")
