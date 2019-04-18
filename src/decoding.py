import files
dict = {}

def decoding():
    data = files.json_load('exams_dates')
    for m in data.keys():
        a = input(m+'\n')
        dict[m] = a
    files.json_save('decoding_exams', dict)

def zamena():
    data = files.json_load('decoding_exams')
    for x in data.keys():
        dict[data[x]] = x
    files.json_save('decoding_exams', dict)

zamena()
    
