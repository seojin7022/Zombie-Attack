from csv import reader

import xml.etree.ElementTree as elemTree


def load_tilemap(path):
    with open(path, 'r') as tilemaps:
        tree = elemTree.fromstring(tilemaps.read())
        tilesets = []
        for i in tree.findall("tileset"):
            with open("./map/" + i.get("source"), 'r') as tileset:
            
                tilesets.insert(int(i.get("firstgid")), elemTree.fromstring(tileset.read()))

        layers = tree.findall("layer")
        
        for i in layers:
            data = i.find("data").text.split("\n")
            # print(data)

            for j in data:
                for k in j.split(","):
                    print(k)
            # for j in range(i.get("height")):
            #     for k in range(i.get("width")):
            #         pass

        
        


load_tilemap(f"./map/map.tmx")