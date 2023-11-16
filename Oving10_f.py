from Oppgave_f import finn_sekvens
from Oving10_a_alt import read_file
from find_eligible_years import find_eligible_years
import matplotlib.pyplot as plt
import datetime as dt
data = read_file("snoedybder_vaer_en_stasjon_dogn.csv")

def max_periode_tørke_peraar(data,sekvens_nr,time_key,main_key, min_value):
    list = find_eligible_years(data,time_key, main_key, min_value)
    
    ferdig_liste = []
    for i in list:
       temp = finn_sekvens(i,sekvens_nr)
       ferdig_liste.append(temp)
    return ferdig_liste



def finne_x_koordinater(data, time_key):
    x_koordinater = []
    for i in range(len(data[time_key])):
        tid_dt = dt.datetime.strptime(data[time_key][i], '%d.%m.%Y')  
        year = tid_dt.year
        if year not in x_koordinater:
           x_koordinater.append(year)
        else:
            continue
    return x_koordinater


if __name__ == "__main__":
    """
    print(max_periode_tørke_peraar(data,"0",'Tid(norsk normaltid)', 'Nedbør (døgn)', 300))
    plt.plot(x_koordinater , y_koordinater, "o-")
    plt.title('Lengste sekvens av antall dager med tørke på rad')
    plt.xlabel('År')
    plt.ylabel("Tørke")
    plt.show()
    """
    y_koordinater = max_periode_tørke_peraar(data,"0",'Tid(norsk normaltid)', 'Nedbør (døgn)', 300)
    x_koordinater = finne_x_koordinater(data,'Tid(norsk normaltid)')
    print(x_koordinater)
    print(y_koordinater)
    print(len(x_koordinater))
    print(len(y_koordinater))


    