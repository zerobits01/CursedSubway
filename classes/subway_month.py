from classes.global_time import GlobalTime
from utility.print_debugs import print_people_info


class SubwayLine:
    '''defining class of lines which they may have different stations
    each line should return a list of stations status if i want
    each station has some info like input_value, output_value, people_inside    
    '''
    def __init__(self, name, stations) -> None:
        self.name = name
        self.stations = stations



def ending_for(line_stations, ranging_value=6):
    for line1 in line_stations:
        for i in reversed(range(ranging_value)):
            line1[i].put_people_inside()
            # if line1[i].prev_stations.__len__() != 0:
            if line1[i].prev_stations.__len__() == 1:
                line1[i].people_inside = line1[i].people_inside +\
                    line1[i].prev_stations[0].people_to_next[line1[i].name]
            elif line1[i].prev_stations.__len__() == 2:
                # here i am sure that i have two trains but if i had more i could write a for loop
                line1[i].people_inside = \
                    line1[i].people_inside + \
                        line1[i].prev_stations[0].people_to_next[line1[i].name] + \
                        line1[i].prev_stations[1].people_to_next[line1[i].name]
            line1[i].define_people_to_next()


def run_subway_lines(global_time: GlobalTime, lines):
    '''what do i have from each station?
        station.name
        station.input_value
        station.output_value
        station.people_inside
        station.put_people_inside
        station.generate_current_input
        station.generate_current_output
        station.people_to_next : dictionary
        station.get_prev_stations also without get
        station.get_next_stations also without get
    '''
    '''what do i have from global time?
        gt.read_time => (hour, minute)
        gt.get_date_time => string of date time
        gt.increase_time => returns nothing but goes to next step 
    '''
    # line1 = lines[0].stations
    # line2 = lines[1].stations
    # line3 = lines[2].stations
    # line4 = lines[3].stations
    line_stations = [lines[0].stations, lines[1].stations, lines[2].stations,lines[3].stations]
    set_line_stations = set()
    for stations in line_stations:
        set_line_stations = set_line_stations.union(set(stations))
    while True:
        
        ############################### 06:00 to 06:30 ###############################
        '''
            its 06:00
            i have only input rate accumulated on stations 
            which train didnt come yet no people to next stations and no one out 
        '''
        
        for i in range(0,5):
            print(global_time.get_date_time())
            for station in set_line_stations:
                station.generate_current_input()
            for line1 in line_stations:
                print_people_info(line1)
            for line1 in line_stations:
                if i == 0:
                    # problem for people inside and people coming
                    # it means it's 06:00
                    for i in reversed(range(2)):
                        line1[i].put_people_inside()
                        if line1[i].prev_stations.__len__() == 1:
                            line1[i].people_inside = line1[i].people_inside +\
                                line1[i].prev_stations[0].people_to_next[line1[i].name]
                        elif line1[i].prev_stations.__len__() == 2:
                            # here i am sure that i have two trains but if i had more i could write a for loop
                            line1[i].people_inside = \
                                line1[i].people_inside + \
                                    line1[i].prev_stations[0].people_to_next[line1[i].name] + \
                                    line1[i].prev_stations[1].people_to_next[line1[i].name]
                        line1[i].define_people_to_next()
                elif i == 1:
                    # it means it's 06:06
                    for i in reversed(range(3)):
                        line1[i].put_people_inside()
                        # if line1[i].prev_stations.__len__() != 0:
                        if line1[i].prev_stations.__len__() == 1:
                            line1[i].people_inside = line1[i].people_inside +\
                                line1[i].prev_stations[0].people_to_next[line1[i].name]
                        elif line1[i].prev_stations.__len__() == 2:
                            # here i am sure that i have two trains but if i had more i could write a for loop
                            line1[i].people_inside = \
                                line1[i].people_inside + \
                                    line1[i].prev_stations[0].people_to_next[line1[i].name] + \
                                    line1[i].prev_stations[1].people_to_next[line1[i].name]
                        line1[i].define_people_to_next()
                elif i == 2:
                    # it means it's 06:12
                    for i in reversed(range(4)):
                        line1[i].put_people_inside()
                        # if line1[i].prev_stations.__len__() != 0:
                        if line1[i].prev_stations.__len__() == 1:
                            line1[i].people_inside = line1[i].people_inside +\
                                line1[i].prev_stations[0].people_to_next[line1[i].name]
                        elif line1[i].prev_stations.__len__() == 2:
                            # here i am sure that i have two trains but if i had more i could write a for loop
                            line1[i].people_inside = \
                                line1[i].people_inside + \
                                    line1[i].prev_stations[0].people_to_next[line1[i].name] + \
                                    line1[i].prev_stations[1].people_to_next[line1[i].name]
                        line1[i].define_people_to_next()
                elif i == 3:
                    # it means it's 06:18
                    for i in reversed(range(5)):
                        line1[i].put_people_inside()
                        # if line1[i].prev_stations.__len__() != 0:
                        if line1[i].prev_stations.__len__() == 1:
                            line1[i].people_inside = line1[i].people_inside +\
                                line1[i].prev_stations[0].people_to_next[line1[i].name]
                        elif line1[i].prev_stations.__len__() == 2:
                            # here i am sure that i have two trains but if i had more i could write a for loop
                            line1[i].people_inside = \
                                line1[i].people_inside + \
                                    line1[i].prev_stations[0].people_to_next[line1[i].name] + \
                                    line1[i].prev_stations[1].people_to_next[line1[i].name]
                        line1[i].define_people_to_next()
                elif i == 4:
                    # it means it's 06:24
                    for i in reversed(range(6)):
                        line1[i].put_people_inside()
                        # if line1[i].prev_stations.__len__() != 0:
                        if line1[i].prev_stations.__len__() == 1:
                            line1[i].people_inside = line1[i].people_inside +\
                                line1[i].prev_stations[0].people_to_next[line1[i].name]
                        elif line1[i].prev_stations.__len__() == 2:
                            # here i am sure that i have two trains but if i had more i could write a for loop
                            line1[i].people_inside = \
                                line1[i].people_inside + \
                                    line1[i].prev_stations[0].people_to_next[line1[i].name] + \
                                    line1[i].prev_stations[1].people_to_next[line1[i].name]
                        line1[i].define_people_to_next()

            global_time.increase_time()
                       
        print(5*'#')
        ############################### 06:30 to 21:30 ###############################
        while(True):
            if global_time.hour == 21 and global_time.minute == 30:
                break
            # print(global_time.get_date_time())
            # for station in set_line_stations:
            #     station.generate_current_input()
            # for line1 in line_stations:
            #     print_people_info(line1)
            # for line1 in line_stations:
            #     for i in reversed(range(6)):
            #             line1[i].put_people_inside()
            #             # if line1[i].prev_stations.__len__() != 0:
            #             if line1[i].prev_stations.__len__() == 1:
            #                 line1[i].people_inside = line1[i].people_inside +\
            #                     line1[i].prev_stations[0].people_to_next[line1[i].name]
            #             elif line1[i].prev_stations.__len__() == 2:
            #                 # here i am sure that i have two trains but if i had more i could write a for loop
            #                 line1[i].people_inside = \
            #                     line1[i].people_inside + \
            #                         line1[i].prev_stations[0].people_to_next[line1[i].name] + \
            #                         line1[i].prev_stations[1].people_to_next[line1[i].name]
            #             line1[i].define_people_to_next()
            global_time.increase_time()
        print(5*'#')
        ############################### 21:30 to 22:00 ###############################
        for k in range(5):
            print(global_time.get_date_time())
            for line1 in line_stations:
                print_people_info(line1)
            for line1 in line_stations:
                for i in reversed(range(6)):
                    line1[i].put_people_inside()
                    # if line1[i].prev_stations.__len__() != 0:
                    if line1[i].prev_stations.__len__() == 1:
                        line1[i].people_inside = line1[i].people_inside +\
                            line1[i].prev_stations[0].people_to_next[line1[i].name]
                    elif line1[i].prev_stations.__len__() == 2:
                        # here i am sure that i have two trains but if i had more i could write a for loop
                        line1[i].people_inside = \
                            line1[i].people_inside + \
                                line1[i].prev_stations[0].people_to_next[line1[i].name] + \
                                line1[i].prev_stations[1].people_to_next[line1[i].name]
                    line1[i].define_people_to_next()
            # ending_for(line_stations=line_stations)
            # if k == 0:
            #     ending_for(line_stations=line_stations, ranging_value=6)
            # elif k == 1:
            #     ending_for(line_stations=line_stations, ranging_value=5)
            # elif k == 2:
            #     ending_for(line_stations=line_stations, ranging_value=4)
            # elif k == 3:
            #     ending_for(line_stations=line_stations, ranging_value=3)
            # elif k == 4:
            #     ending_for(line_stations=line_stations, ranging_value=2)
            # elif k == 1:
            #     ending_for(line_stations=line_stations, ranging_value=1)
            global_time.increase_time()
        else:
            print(global_time.get_date_time())
            for stations in line_stations:
                print_people_info(stations=stations)
            print(5*'#')
            if global_time.day == 1 and global_time.hour == 22:
                global_time.increase_time()
                break
