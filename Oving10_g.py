### Den vil ikke importere find_eligible_years...?
### må finne en måte å finne ut hvilke år som er med å ikke (dictionary kanskje?)
#from find_eligible_years import find_eligible_years
from Oving10_a_alt import read_file
import datetime as dt
import matplotlib.pyplot as plt

data = read_file("snoedybder_vaer_en_stasjon_dogn.csv")

#Bare frem til jeg får til å importere find_eligible_years:
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

# Den faktiske oppgaven:
def antall_penvaersdager(data):
    bruksdata = find_eligible_years(data, 'Tid(norsk normaltid)', "Gjennomsnittlig skydekke (døgn)", 300)
    penvaersdager_tot= []
    for i in bruksdata:
        penvaersdager_aar = 0
        for j in i:
            try:
                tall_istedetfor_string = float(j.replace(',', '.'))
            except:
                continue
            if tall_istedetfor_string <= 3:
                penvaersdager_aar += 1
            else:  
                continue
        penvaersdager_tot.append(penvaersdager_aar)
    return penvaersdager_tot

if __name__ == "__main__":
    #print(antall_penvaersdager(data))
    x = list(i for i in range(1980,2022)) # not final
    y = antall_penvaersdager(data)
    #print(len(x), len(y))
    plt.plot(x,y, "o-")
    plt.xlabel("År")
    plt.ylabel("Antall penværsdager")
    plt.show()
            
