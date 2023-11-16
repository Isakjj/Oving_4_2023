from Oppgave_e import diff
from Oving10_a_alternative import read_file
from datetime import datetime
import numpy as np
from matplotlib import pyplot as plt

def avg(list):
    avg = np.average(list)
    return(avg)

def avg_temp():
    d = read_file("snoedybder_vaer_en_stasjon_dogn.csv")
    date = list(d.keys())[2]
    temp = list(d.keys())[4]
    date_list = []
    temp_list = []
    avg_temp_dict = {}
    avg_temp_list = []
    diff_temp_list = []
    for i, date in enumerate(d[date]):
        date_list.append(datetime.strptime(date, '%d.%m.%Y'))
        temp_list.append(d[temp][i])
        month = date_list[i].year, date_list[i].month
        if month not in avg_temp_dict:
            avg_temp_dict[month] = []
        np.array(avg_temp_dict[month].append(float((d[temp][i]).replace(",",".").replace("-","0"))))
    for key, value in avg_temp_dict.items():
        avg_temp_list.append(round(np.average(value),4))
    diff_temp_list.append(diff(avg_temp_list))
    return(avg_temp_list, diff_temp_list, avg_temp_dict)


if __name__ == '__main__':
    a, b, c = avg_temp()
    plt.plot(a, c)
    plt.plot(b, c)
    plt.show()
