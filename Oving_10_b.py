from datetime import datetime
from Oppgave_d import ant_str
from Oving10_a_alternative import read_file

def check_snowdate(d):
    #Make 2 variables, one for the date and one for the depth.
    #Make a dictionary for the seasons.
    date = list(d.keys())[2]
    depth = list(d.keys())[3]
    season_dict = {}
    #Take the date from the dictionary and make it a datetime object.
    for i, date in enumerate(d[date]):
        check_date = datetime.strptime(date, '%d.%m.%Y')
        #Check if the date is in the winter season between 1.10 and 31.05.
        #If it is thake the start year and the end year and make it a season.
        if check_date.month <= 5 or check_date.month >= 10:
            season_start_year = check_date.year
            season_end_year = check_date.year + 1
            season = f"Season {season_start_year}-{season_end_year}"
            #If the season is not in the dictionary, add it.
            if season not in season_dict:
                season_dict[season] = []
            season_dict[season].append(d[depth][i])
    #Make a list of tuples with the season as the key and the depth as the value.
    snow_days = [(key, [ant_str(value, 20)]) for key, value in season_dict.items()]

    return snow_days

if __name__ == '__main__':
    print(check_snowdate(read_file("snoedybder_vaer_en_stasjon_dogn.csv")))
    print()
    print()
    test = check_snowdate(read_file("snoedybder_vaer_en_stasjon_dogn.csv"))
    print(test[1][0])   
    print(test[1][1])
    
#   for key in depth_dict:
#      snow_days[key] = []
#      snow_days[key].append(ant_str(depth_dict[key], 20))   