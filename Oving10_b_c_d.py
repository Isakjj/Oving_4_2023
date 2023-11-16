from datetime import datetime
from Oppgave_d import ant_str
from Oving10_a_alt import read_file
from Oppgave_g import trend
from matplotlib import pyplot as plt
import numpy as np


def check_snowdate(d):
    #Makes 2 variables, one for the date and one for the depth.
    #Makes a dictionary for the seasons that will contain seasons as key and snow days as value.
    #Make a list for the start year of the season.
    #Make a list for the snow days.
    date = list(d.keys())[2]
    depth = list(d.keys())[3]
    season_dict = {}
    start_year_list = []
    snow_days_list = []
    #Takes the date from the dictionary and makes it a datetime object.
    for i, date in enumerate(d[date]):
        check_date = datetime.strptime(date, '%d.%m.%Y')
        #Checks if the date is in the winter season, between 1.10 and 31.05.
        #If it is, take the start year and the end year and makes it a season.
        if check_date.month <= 5 or check_date.month >= 10:
            season = check_date.year
            #season_start_year = check_date.year
            #season_end_year = check_date.year + 1
            #season = f"Season {season_start_year}-{season_end_year}"
            #If the season is not in the dictionary, adds it.
            if season not in season_dict:
                season_dict[season] = []
            season_dict[season].append(d[depth][i])
    for key in season_dict:
        if len(season_dict[key]) >= 200:
            snow_days_list.append(ant_str(season_dict[key], 20))
            start_year_list.append(key)

    return start_year_list, snow_days_list

if __name__ == '__main__':
    a, b= check_snowdate(read_file("snoedybder_vaer_en_stasjon_dogn.csv"))
    print(a)
    print(b)
    plt.plot(a, b)             
    x, y = trend(a, b)
    plt.xticks(np.arange(a[0], a[-1]+1, 1))
    plt.xlim(a[0]-1, a[-1]+1)
    plt.ylim(0, max(b)+10)
    x_akse = np.linspace(a[0]-1, a[-1]+1)
    y_akse = x_akse*x+y
    plt.plot(x_akse, y_akse)
    plt.show()
