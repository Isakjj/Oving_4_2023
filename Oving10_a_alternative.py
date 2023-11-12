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
        lines = file.readlines()
        for line in lines[:-1]:
            values = line.strip().split(';')
            for i, value in enumerate(values):
                file_dict[header[i]].append(value)
                
    return file_dict

 
def check_snowdate(d):
    date = list(d.keys())[2]
    depth = list(d.keys())[3]
    depth_dict = {}
    print(date, depth)
    for i, date in enumerate(d[date]):
        check_date = datetime.strptime(date, '%d.%m.%Y')
        if check_date.month <= 5 or check_date.month >= 10:
            season_start_year = check_date.year
            season_end_year = check_date.year + 1
            season = f"Season {season_start_year}-{season_end_year}"
            if season not in depth_dict:
                depth_dict[season] = []
            depth_dict[season].append(d[depth][i])
    return depth_dict
        
    
if __name__ == '__main__':
    filename = "snoedybder_vaer_en_stasjon_dogn.csv"
    d = read_file(filename)
    print(list(d.keys()))
    snowdate = check_snowdate(d)

#specific_key = list(d.keys())
#for i, key in enumerate(specific_key):
#    print(key,": ", end="")
#    print(d[key][10200])

    
#Task b)
#Make a new list for each snow season
#Add the 
    