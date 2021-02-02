PPAP = input()

while True:
    if "PPAP" in PPAP:
        PPAP = PPAP.replace("PPAP", "P")
        if PPAP == "PPAP":
            print(PPAP)
            break
    else:
        print("NP")
        break

