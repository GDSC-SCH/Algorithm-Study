city_num = int(input())
bus_num = int(input())

bus_list = []

for _ in range(bus_num):
    start, destination, cost = map(int,input().split())
    bus_list.append([start,destination,cost])