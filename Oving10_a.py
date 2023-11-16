import datetime as dt
# Første linje i excelfila er navn på kolonnene 
# hvordan får vi ignorert disse datapunktene?

def vaerstasjon_data(filnavn):
    # Make a dictionary with the keys as the different types of data
    vaerdata = {
        'Navn': [],
        'StasjonsID' : [],
        'Dato': [],
        'Snodybde (cm)': [],
        'Nedbor (mm)': [],
        'Middeltemp': [],
        'Skydekke': [],
        'Middelvind (m/s)': [],
     }
    # Open the file and split the lines into datapoints
    # Append the datapoints to the dictionary
    with open(filnavn, 'r') as fil:
       fil.readline()
       for linje in fil:
           deler = linje.strip().split(';')
           navn, stasjonsID, dato, snodybde, nedbor, middeltemp, skydekke, middelvind = deler

           vaerdata['Navn'].append(navn)
           vaerdata['StasjonsID'].append(stasjonsID)
           dato_dt = dt.datetime.strptime(dato, '%d.%m.%Y')
           vaerdata['Dato'].append(dato_dt)
           vaerdata['Snodybde (cm)'].append(snodybde if snodybde !='-' else None)
           vaerdata['Nedbor (mm)'].append(nedbor if nedbor !='-' else None)
           vaerdata['Middeltemp'].append(middeltemp if middeltemp !='-' else None)
           vaerdata['Skydekke'].append(skydekke if skydekke !='-' else None)
           vaerdata['Middelvind (m/s)'].append(middelvind if middelvind !='-' else None)
    # Return the dictionary    
    return vaerdata


if __name__ == '__main__':
    data = vaerstasjon_data("snoedybder_vaer_en_stasjon_dogn.csv")

    print(data['Snodybde (cm)'])