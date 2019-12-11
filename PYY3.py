Fl = open('file.txt', 'w')
for i in range(1, 10):
    Fl.write('a'*i + '\n')
Fl.close()
