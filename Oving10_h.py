#Vil heller ikke importere find eligible years her... idk koffer??
#from find_eligible_years import find_eligible_years
from Oving10_a_alt import read_file
import datetime as dt
import matplotlib.pyplot as plt

data = read_file("snoedybder_vaer_en_stasjon_dogn.csv")

def find_eligible_years(data,time_key,main_key, min_value):
    dict_years = {}
    for i in range(len(data[time_key])):
        tid_dt = dt.datetime.strptime(data[time_key][i], '%d.%m.%Y')  
        year = tid_dt.year
        if year not in dict_years:
            dict_years[year] = []
        dict_years[year].append(data[main_key][i]) 

    list_eligible_years = []   
    for j in dict_years:
        check_list = []
        for i in dict_years[j]:  
            if i == None:
                continue
            else:
                check_list.append(i)
        if len(check_list) >= min_value:
            list_eligible_years.append(dict_years[j])
    return list_eligible_years


def finn_max_middelvind_per_aar(data, time_key, main_key, min_value):
    bruksdata = find_eligible_years(data,time_key, main_key, min_value)
    max_vind = []
    for i in bruksdata:
        max_vind.append(max(i))
    return max_vind


def finn_median_middelvind(data, time_key, main_key, min_value):
    bruksdata = find_eligible_years(data,time_key, main_key, min_value)
    median_middelvind_per_aar = []
    for i in bruksdata:
        sort_list = i.sort()
        if len(sort_list) % 2 == 0:
            median =sort_list[len(sort_list)//2]
        else:
            median = (2*(sort_list[len(sort_list)//2-1]) / 2)
        median_middelvind_per_aar.append(median)

    return median_middelvind_per_aar


if __name__ == "__main__":
    print(finn_max_middelvind_per_aar(data, 'Tid(norsk normaltid)', "Høyeste middelvind (døgn)", 300))
    print(finn_median_middelvind(data, 'Tid(norsk normaltid)', "Høyeste middelvind (døgn)", 300))