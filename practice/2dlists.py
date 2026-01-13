#2d lists

rake =    ["21 7.5", "21 6.5", "21 4.5", "21 3" ]
tension = [18,          19,        23,        25]
turns =   [-1,           0,         3,         4]

settings = [rake, tension, turns]

print(f"LIGHT SETTINGS\n Rake: {settings[0][0]} Tension: {settings[1][0]} Turns: {settings[2][0]}")

capitals = {}
capitals["Mexico"] = "CDMX"
capitals["USA"] = "Washington, DC"
capitals["Brazil"] = "Brasilia"
capitals["France"] = "Paris"
capitals["Spain"] = "Madrid"
print(capitals)
print(dir(capitals))