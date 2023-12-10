"""Day 5, part 1, what kind of dataset is this!"""
import itertools
from collections import OrderedDict

Temperature_to_humidity=[2742352899, 2748429907, 2756722033, 2782815442, 2785799700, 827680287, 
                         2593529505, 2596541796, 2393751907, 2449232611, 4242986636, 132385762, 
                         1383547122, 1806713128, 586927875, 3287902362, 2931950845, 1244574328, 787747552, 1997540813]
def dict_map(slines):
    """This function takes a range of strings and creates the source to destiontion dictionary
    where the key is the source, the value contains a list, whose first element is the destination
    and the 2nd element is the range for both source and destination"""
    d = {}
    for line in slines:
        dl = line.split()
        d[int(dl[1])] = [int(dl[0]),int(dl[2])]
        sorted_dict=OrderedDict(sorted(d.items()))
    return sorted_dict

def mapping(source,map_dict):
    destination=[]
    for s in source:
        if s in map_dict:
            destination.append(map_dict[s][0])
            continue
        for key,value in map_dict.items():
            end = key+value[1]+1
            if s in range(key,end):
                for i,x in enumerate(range(key,end)):
                    if x == s:
                        destination.append(value[0]+i)
                        break
                break
        else: destination.append(s)
    return destination

with open("hl.txt", "r") as file:
    hl=dict_map(file)
Humidity_to_location = mapping(Temperature_to_humidity,hl)

#print(Initial_seeds)
#print(Seed_to_soil)
#print(Soil_to_fertilizer)
#print(Fertilizer_to_water)
#print(Water_to_light)
#print(Light_to_temperature)
#print(Temperature_to_humidity)
print(Humidity_to_location)
#End-of-file(EOF)