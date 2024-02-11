from classes.stations import *


def print_lines(lines):
    i = 1
    for line in lines:
        for station in line.stations:
            print(20*"#" + str(i))
            print(f"station name is: {station.name}")
            print(f"people to next station dict is: {station.people_to_next}")
            print(f"prev stations: {station.prev_stations}")
            print(f"next stations: {station.next_stations}")
            print(20*"#")
            i = i + 1


def print_start_stations(lines):
    i = 1
    for line in lines:
        for station in line.stations:
            if type(station) is SubwayStartStation:
                print(20*"#" + str(i))
                print(f"station name is: {station.name}")
                print(f"people to next station dict is: {station.people_to_next}")
                print(f"prev stations: {station.prev_stations}")
                print(f"next stations: {station.next_stations}")
                print(20*"#")
                i = i + 1
    

def print_people_info(stations, datetime, subway_ds):
    print(['name', 'input', 'output', 'people_inside', 'coming_from_prev', 'people_to_next'])
    for station in stations:
        coming_from_prev = {}
        for prev_stat in station.prev_stations:
            coming_from_prev[prev_stat.name] = prev_stat.people_to_next[station.name]
        # print(
        #     [
        #         station.name,
        #         station.input_value,
        #         station.output_value,
        #         station.people_inside,
        #         coming_from_prev,
        #         station.people_to_next,
        #     ]
        # )
        record = {
            "stationname": station.name,
            "datetime": datetime,
            "input": station.input_value,
            "output": station.output_value, 
            "peopleinsidetrain": station.people_inside
        }
        subway_ds.append(record)
    print(10*"#$")