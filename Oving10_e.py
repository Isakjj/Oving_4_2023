from Oppgave_h_l import growth
from Oving10_a_alt import read_file
import datetime as dt

data = read_file("snoedybder_vaer_en_stasjon_dogn.csv") # key 5 er middeltemp

def growth_per_year(data):
    dict_years = {}
    for i in range(len(data['Tid(norsk normaltid)'])):
        tid_dt = dt.datetime.strptime(data['Tid(norsk normaltid)'][i], '%d.%m.%Y')  
        year = tid_dt.year
        if year not in dict_years:
            dict_years[year] = []
        dict_years[year].append(data['Middeltemperatur (døgn)'][i])


    list_eligible_years = []   
    for j in dict_years:
        check_list = []
        for i in dict_years[j]:  
            if i == None:
                continue
            else:
                check_list.append(i)
        if len(check_list) >= 300:
            list_eligible_years.append(dict_years[j])
    sum_growth = []       

    for k in list_eligible_years:
        liste_float_k = []
        for i in k:
            try:
                liste_float_k.append(float(i.replace(',','.')))
            except:
                continue
        growth_year = growth(liste_float_k)
        sum_growth.append(growth_year)
    return sum_growth

if __name__ == '__main__':
    print(growth_per_year(data)) 

