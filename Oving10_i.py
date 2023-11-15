from Oppgave_e import diff
from Oving10_a_alternative import read_file
from datetime import datetime
import numpy as np

def avg_temp():
    d = read_file("snoedybder_vaer_en_stasjon_dogn.csv")
    date = list(d.keys())[2]
    temp = list(d.keys())[4]
    date_list = []
    temp_list = []
    avg_temp_dict = {}
    for i, date in enumerate(d[date]):
        date_list.append(datetime.strptime(date, '%d.%m.%Y'))
        temp_list.append(d[temp][i])
        year = date_list[i].year
        if year not in avg_temp_dict:
            avg_temp_dict[year] = []
    print(avg_temp_dict)



avg_temp()