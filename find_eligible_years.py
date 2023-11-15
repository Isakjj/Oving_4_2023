from Oving10_a_alternative import read_file
import datetime as dt


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


if __name__ == "__main__":
    data = read_file("snoedybder_vaer_en_stasjon_dogn.csv")
    print(find_eligible_years(data,'Tid(norsk normaltid)', 'Nedbør (døgn)', 300))