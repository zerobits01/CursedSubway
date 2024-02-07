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
    

def print_people_info(lines):
    for line in lines:
        print(['name', 'input', 'output', 'people_inside', 'people_to_next'])
        for station in line.stations:
            print(
                [
                    station.name,
                    station.input_value,
                    station.output_value,
                    station.people_inside,
                    station.people_to_next,
                ]
            )
        print(10*"#$")