import os

def read_text():
    current_path = os.getcwd()
    quetes = open(r''+current_path+'\movie_quotes.txt');
    contents_of_file = quetes.read()
    print contents_of_file
    quetes.close()

read_text()
