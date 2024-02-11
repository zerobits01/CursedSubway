'''
1. i have a global time(it changes 6 minutes 6 minutes) 
    it increases if and only if the 4 lines have generated the data
2. i can use 4 threads for each line => so i have to use a kinda mutex 
    or sth like that to generate values and ...
2.1. all of the arrays are shared buffers so that we can use them 
      for checking the hub stations
      people from input rate shouldnt be outputed
      so maximumly at each state we can have output rate of last station
3. each line checks the time if the time is changed the main thread increases the time
4. these are the base ideas


1  => 2  => 3  => 4  => 5  => 6
0  => 6  => 12 => 18 => 24 => 30
6  => 12 => 18 => 24 => 30 => 36

tajrish => shariati => beheshti => dolat      => mohammadie => kaharizak
sanaat  => valiasr  => teatr    => mohammadie => molavi     => basij
satari  => valiasr  => jahad    => beheshti   => heravi     => ghaem
azadi   => teatr    => ferdowsi => dolat      => shemiran   => bouali

dolat      => hub 1_4
mohammadie => hub 1_2
teatr      => hub 2_4
valiasr    => hub 2_3
beheshti   => hub 1_3


what can be the problems:
1. output more than input
2. hub station distribution to other stations
3. ....

#implementing that
#implement the graph design => #done
#implement dataset for 30 days, i gave the idea with 
    # shared arrays and also multithreaded(start from 6 last subway starts since 21:30)

#implement: for each statation train a model to predict output
#implement: " " input
#implement: " " at each time predict the people inside of metro
#implement: " " the poasson rate for each station
#implement: choose a good validation param test it and show why its good
'''

from classes.global_time import GlobalTime
from classes.stations import *
from classes.subway_month import *
from utility.graphical_mode import visualize_subway_lines
from utility.dataset import SubwayDataset


def define_lines():

    ################################### Global ###################################
    global tajrish, shariati, beheshti, dolat, mohammadie, kaharizak, \
        sanaat, valiasr, teatr, molavi, basij, satari, jahad, heravi, ghaem, \
            azadi, ferdowsi, shemiran, bouali, line1, line2, line3, line4
    ################################### LINE 1 ################################### 
    tajrish = SubwayStartStation('tajrish')
    shariati = SubwayNormalStation('shariati')
    beheshti = SubwayHubStation('beheshti')
    # prev stations = jahad, shariati / next stations = heravi, dolat
    dolat = SubwayHubStation('dolat')
    # prev stations = ferdowsi, beheshti / next stations = shemiran, mohammadie
    mohammadie = SubwayHubStation('mohammadie')
    # prev stations = teatr, dolat / next stations = molavi, kahrizak
    kaharizak = SubwayLastStation('kaharizak')
    
    ################################### LINE 2 ###################################
    sanaat = SubwayStartStation('sanaat')
    valiasr = SubwayHubStation('valiasr')
    # prev stations = sanaat, satari / next stations = teatr, jahad
    teatr = SubwayHubStation('teatr')
    # prev stations = valiasr, azadi/ next stations = ferdowsi, mohammadie
    # mohammadie = defined before
    molavi = SubwayNormalStation('molavi')
    basij = SubwayLastStation('basij')
    
    ################################### LINE 3 ###################################
    satari = SubwayStartStation('satari')
    # valiasr = defined before
    jahad = SubwayNormalStation('jahad')
    # beheshti = defined before
    heravi = SubwayNormalStation('heravi')
    ghaem = SubwayLastStation('ghaem')
    
    ################################### LINE 4 ###################################
    azadi = SubwayStartStation('azadi')
    # teatr = defined before
    ferdowsi = SubwayNormalStation('ferdowsi')
    # dolat = defined before
    shemiran = SubwayNormalStation('shemiran')
    bouali = SubwayLastStation('bouali')


    ######################## defining connections ########################
    beheshti.set_prev_stations([jahad, shariati])
    beheshti.set_next_stations([heravi, dolat])

    dolat.set_prev_stations([ferdowsi, beheshti])
    dolat.set_next_stations([shemiran, mohammadie])

    mohammadie.set_prev_stations([teatr, dolat])
    mohammadie.set_next_stations([molavi, kaharizak])

    valiasr.set_prev_stations([sanaat, satari])
    valiasr.set_next_stations([teatr, jahad])

    teatr.set_prev_stations([valiasr, azadi])
    teatr.set_next_stations([ferdowsi, mohammadie])

    tajrish.set_next_stations([shariati])
    shariati.set_prev_stations([tajrish])
    shariati.set_next_stations([beheshti])
    kaharizak.set_prev_stations([mohammadie])
    sanaat.set_next_stations([valiasr])
    molavi.set_prev_stations([mohammadie])
    molavi.set_next_stations([basij])
    basij.set_prev_stations([molavi])
    satari.set_next_stations([valiasr])
    jahad.set_prev_stations([valiasr])
    jahad.set_next_stations([beheshti])
    heravi.set_prev_stations([beheshti])
    heravi.set_next_stations([ghaem])
    ghaem.set_prev_stations([heravi])
    azadi.set_next_stations([teatr])
    ferdowsi.set_prev_stations([teatr])
    ferdowsi.set_next_stations([dolat])
    shemiran.set_prev_stations([dolat])
    shemiran.set_next_stations([bouali])
    bouali.set_prev_stations([shemiran])
    ####################### defining line objects ########################
    line1 = SubwayLine('line1', [tajrish, shariati, beheshti, dolat, mohammadie, kaharizak])
    line2 = SubwayLine('line2', [sanaat, valiasr, teatr, mohammadie, molavi, basij])
    line3 = SubwayLine('line3', [satari, valiasr, jahad, beheshti, heravi, ghaem])
    line4 = SubwayLine('line4', [azadi, teatr, ferdowsi, dolat, shemiran, bouali])


def main():
    define_lines()
    lines = [line1, line2, line3, line4]
    visualize_subway_lines(lines)
    global glob_time
    glob_time = GlobalTime()
    subway_ds = SubwayDataset()
    run_subway_lines(global_time=glob_time, lines=lines, subway_ds=subway_ds)
    subway_ds.describe()
    subway_ds.save("subway_dataset.csv")

if __name__ == "__main__":
    main()