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
     
if __name__ == '__main__':
    filename = "snoedybder_vaer_en_stasjon_dogn.csv"
    d = read_file(filename)
    print(list(d.keys()))


 