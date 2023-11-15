from Oppgave_h_l import growth
from Oving10_a import vaerstasjon_data
import datetime as dt

data = vaerstasjon_data("snoedybder_vaer_en_stasjon_dogn.csv") # key 5 er middeltemp

def growth_per_year(data):
    list_years = []
    for i in range(len(data['Dato'])):
        year = data['Dato'][i].year
        if year not in list_years:
            list_years[year] = []
        list_years[year].append(data['Middeltemp'][i])

    list_eligible_years = []   
    for year in list_years:
        for i in list_years[year]:
            check_list = []
            if list_years[year][i] == None:
                continue
            else:
                check_list.append(list_years[year][i])
        if len(check_list) >= 300:
            list_eligible_years.append(list_years[year])
    sum_growth = 0        
    for i in list_eligible_years:
        temp_growth = growth(list_years[i])
        sum_growth += temp_growth
    return sum_growth

if __name__ == '__main__':
    print(growth_per_year(data)) 

