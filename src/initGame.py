import os, json

if not os.path.exists(f"./data"):
    os.mkdir("./data")


def InspectData(data: dict, playerData: dict):
    for v in data.keys():
        if playerData[v] != None:
            if type(data[v]) == dict:
                playerData[v] = InspectData(data[v], playerData[v])
        else:
            print(v)
            playerData[v] = data[v]

    return playerData


datas = {
    "PlayerData": {
        "Stats": {
            "Attack": 1,
            "Defense": 1,
        },
        "Mastery": {},
        "Coin": 0,
        "ZombieStone": 0,
        "Equipments": [],
        "Magics": {},
    }
}

data = {}
isFirstStarter = True

if os.path.exists(f"./data/player-data.txt"):
    isFirstStarter = False
    with open(f"./data/player-data.txt", "r") as playerData:
        data = InspectData(datas, json.loads(playerData.read()))
else:
    with open(f"./data/player-data.txt", "w") as playerData:
        playerData.write(json.dumps(datas))

data["PlayerData"].update({"Hp": data["PlayerData"]["Stats"]["Defense"] * 100})

print("✅ Initialized Successfully")
