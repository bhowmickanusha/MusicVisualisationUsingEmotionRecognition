import os
def read_first_line(file):
    fd = open(r"C:\Users\Bhowmik\Downloads\\"+file, 'r')
    first_line = fd.readline() # could be write(), read(), readline(), etc...
    fd.close()
    
    return first_line

def get_filename():
    
    all_files = os.listdir(r"C:\Users\Bhowmik\Downloads")
    txt_files = list(filter(lambda x: x[-4:] == '.txt', all_files))
    text_list=sorted(txt_files)
    #print(text_list)

    s=len(text_list)
    for i in range(s-1):
        file=text_list[i]
        #print(file)

    output_strings = read_first_line(file) # apply read first line function all text files
    #print(output_strings)
    return output_strings

