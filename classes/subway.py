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


    def get_values(self):
        # for each station read all values and put them in a list and return them
        # returning three lists
        pass


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
    line1 = lines[0].stations
    line2 = lines[1].stations
    line3 = lines[2].stations
    line4 = lines[3].stations
    
    while True:
        
        ############################### 06:00 to 06:30 ###############################
        '''
            its 06:00
            i have only input rate accumulated on stations 
            which train didnt come yet no people to next stations and no one out 
        '''
        for i in range(0,5):
            ######################################
            for j in range(0,6):
                # we have accumulation inside
                line1[j].generate_current_input()
            ######################################
            # i have to read the input rate from here
            print(global_time.get_date_time())
            print_people_info([lines[0]])
            # if i == 0:
                # it means it's 06:00
                # dont get the value for this state from prev_station.people_inside get it from prev_station.to_next
                # line1[0].people_inside = line1[0].input_value # after this i have defined the method put_people_inside
                # pass
            if i == 0:
                # it means it's 06:06
                line1[0].put_people_inside()
                line1[0].define_people_to_next()
                line1[1].put_people_inside()
                if line1[1].prev_stations.__len__() == 1:
                    line1[1].people_inside = \
                        line1[1].people_inside + line1[1-1].people_to_next[line1[1].name]
                else:
                    # here i am sure that i have two trains but if i had more i could write a for loop
                    line1[1].people_inside = \
                        line1[1].people_inside + \
                            line1[1].prev_stations[0].people_to_next[line1[1].name] + \
                            line1[1].prev_stations[1].people_to_next[line1[1].name]
                line1[1].define_people_to_next()
                # then clearing the before people inside
                line1[0].put_people_inside()
                line1[0].define_people_to_next()
            elif i == 1:
                # it means it's 06:12
                ######### for i in reversed(range(3))
                line1[2].put_people_inside()
                if line1[2].prev_stations.__len__() == 1:
                    line1[2].people_inside = \
                        line1[2].people_inside + line1[2-1].people_to_next[line1[2].name]
                else:
                    # here i am sure that i have two trains but if i had more i could write a for loop
                    line1[2].people_inside = \
                        line1[2].people_inside + \
                            line1[2].prev_stations[0].people_to_next[line1[2].name] + \
                            line1[2].prev_stations[1].people_to_next[line1[2].name]
                line1[2].define_people_to_next()
                #
                line1[1].put_people_inside()
                if line1[1].prev_stations.__len__() == 1:
                    line1[1].people_inside = \
                        line1[1].people_inside + \
                            line1[1].prev_stations[0].people_to_next[line1[1].name]
                else:
                    # here i am sure that i have two trains but if i had more i could write a for loop
                    line1[1].people_inside = \
                        line1[1].people_inside + \
                            line1[1].prev_stations[0].people_to_next[line1[1].name] + \
                            line1[1].prev_stations[1].people_to_next[line1[1].name]
                line1[1].define_people_to_next()
                # then clearing the before people inside
                line1[0].put_people_inside()
                line1[0].define_people_to_next()
            elif i == 2:
                # it means it's 06:18
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
                # it means it's 06:24
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
                # it means it's 06:30
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
            print(global_time.get_date_time())
            print_people_info([lines[0]])
            if global_time.hour == 21 and global_time.minute == 30:
                break
            for j in range(0,6):
                line1[j].generate_current_input()
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
        ############################### 21:30 to 22:00 ###############################
        for k in range(5):
            print(global_time.get_date_time())
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
            print_people_info([lines[0]])
            global_time.increase_time()
        else:
            print(global_time.get_date_time())
            print_people_info([lines[0]])
            print(5*'#')
            if global_time.day == 1 and global_time.hour == 22:
                break
