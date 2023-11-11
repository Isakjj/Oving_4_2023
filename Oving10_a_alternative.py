from Oppgave_d import ant_str
from datetime import datetime



def read_file(filename):
    #Open the file
    with open(filename, 'r', encoding="UTF-8-sig") as file:
        #Take the first line from the file, and make each value a key in a dictionary
        header = file.readline().strip().split(';')
        file_dict = {key: [] for key in header}

        #For the next lines, strip and split the lines.
        #Then for each value, assign it to the header in the same row.
        for line in file:
            values = line.strip().split(';')
            for i, value in enumerate(values):
                file_dict[header[i]].append(value)
                
    return file_dict


def check_snowdate(d):
    date = list(d.keys())[2]
    depth = list(d.keys())[3]
    depth_list = []
    print(date, depth)
    for i in zip(d[date]):
        check_date = datetime.strptime(i, '%d.%m.%Y')
#        check_depth = j
        if check_date.month <= 5 or check_date.month >= 10: 
            
            ant_str( ,20)

        
    
if __name__ == '__main__':
    filename = "snoedybder_vaer_en_stasjon_dogn.csv"
    d = read_file(filename)
    print(list(d.keys()))
    check_snowdate(d)

#specific_key = list(d.keys())
#for i, key in enumerate(specific_key):
#    print(key,": ", end="")
#    print(d[key][10200])

    
#Task b)
#Make a new list for each snow season
#Add the 
    