import numpy as np
import random as rnd
import datetime

# seeding the random with time value to get real random values
rnd.seed(datetime.time())


# now we can rnd.randint(start, end) to get the random values
class SubwayStation:
    '''this is the base class of subway stations
    '''
    
    def __init__(self, name):
        self.name = name
        self.input_value = 0
        self.output_value = 0
        self.people_to_next = {} # if its hub or its normal and etc
        # then they can read this value by their name as key # this is more secure
        self.input_poisson_rate = 0
        self.output_poisson_rate = 0
        self.model = None
        
        self.people_inside = 0 # prev to next plus input minus output
        self.prev_stations = []
        self.next_stations = []

    
    def set_next_stations(self, next_stations):
        if type(next_stations) is not list:
            raise ValueError("next stations should be type of list")
        for item in next_stations:
            # print(type(item), SubwayStation)
            if not issubclass(type(item), SubwayStation):
                raise ValueError("stations in next_stations list should be subclass of SubwayStation")
        self.next_stations = next_stations
        if len(next_stations) != 0:
            for station in next_stations:
                self.people_to_next[station.name] = 0
    
    
    def set_prev_stations(self, prev_stations):
        if type(prev_stations) is not list:
            raise ValueError("prev stations should be type of list")
        for item in prev_stations:
            if not issubclass(type(item), SubwayStation):
                raise ValueError("stations in prev_stations list should be subclass of SubwayStation")
        self.prev_stations = prev_stations
    
    
    def get_next_stations(self):
        return self.next_stations
    
    
    def get_prev_stations(self):
        return self.prev_stations


    def set_model(self, model):
        # validate whether its a polinomial regression
        self.model = model


    def generate_current_input(self):
        self.input_value = self.input_value + np.random.poisson(self.input_poisson_rate)
        return self.input_value


    def generate_current_output(self):
        self.output_value = np.random.poisson(self.input_poisson_rate)
        if self.output_value > self.people_inside:
            self.output_value = self.people_inside
        return self.output_value


    def put_people_inside(self):
        # here i can get the before station
        self.people_inside = self.input_value
        self.input_value = 0
        # self.define_people_to_next()


    def define_people_to_next(self):
        if len(self.next_stations) == 2:
            if (self.people_inside/2).is_integer():
                self.people_to_next[self.next_stations[0].name] = self.people_inside/2
                self.people_to_next[self.next_stations[1].name] = self.people_inside/2
            else:
                self.people_to_next[self.next_stations[0].name] = int(self.people_inside/2)
                self.people_to_next[self.next_stations[1].name] = int(self.people_inside/2) + 1
                #Problem
        else:
            self.people_to_next[self.next_stations[0].name] = self.people_inside


    def get_model(self):
        return self.model
    # TODO: defining the methods of update like output range and etc
    # then overwriting them in special Stations like hubs and start and last
    # e.g for last we dont have input so we overwrite to pass!

    def __str__(self) -> str:
        return self.name


class SubwayStartStation(SubwayStation):
    '''this is about Start Stations which they dont have output
    '''
    
    def __init__(self, name):
        super().__init__(name)
        self.input_poisson_rate = rnd.randint(30, 40)


class SubwayLastStation(SubwayStation):
    '''this is for last stations which dont have input
    and the output is exactly the value of people inside the train
    '''
    
    def __init__(self, name):
        super().__init__(name)

    # this has been overwritten for last stations
    def generate_current_output(self):
        return self.people_inside
    
    def define_people_to_next(self):
        self.output_value = self.people_inside
        self.people_inside = 0


class SubwayHubStation(SubwayStation):
    '''it's about hub stations which have input, output
    and they have hub mode of 50% output to their next stations
    '''
    
    def __init__(self, name):
        super().__init__(name)
        self.input_poisson_rate = rnd.randint(10,14)
        self.output_poisson_rate = rnd.randint(15,20)
        # we have to control the output which should be only from the train incoming value
        # poeple_to_next with rate 50 percent will be distributed but we have to pay attention to odds


class SubwayNormalStation(SubwayStation):
    '''this is about normal stations which only have input and output
    '''
    
    def __init__(self, name):
        super().__init__(name)
        self.input_poisson_rate = rnd.randint(10,14)
        self.output_poisson_rate = rnd.randint(8,12)
        # we have to control the output which should be only from the train incoming value

