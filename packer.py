import sys
import os

#USAGE: FIRST ARG INPUT FILENAME, ALL ZIP FILES WILL BE INSTALLED AFTER UNPACK. ZIP FILE MUST BE NAMED SAME AS THE DIR
inputFile = sys.argv[1]
print('Running: ')
hexdumpcommand = 'xxd --plain ' + inputFile + ' > tempr.txt'
os.system(hexdumpcommand)
file = open('tempr.txt', 'r')
data = file.read()
clean_data = data.replace('\n', '')
file.close()
stringg = clean_data.replace('5', 'g').replace('4', 'h').replace('3', 'i').replace('2', 'j').replace('1', 'k').replace('0', 'l').replace('9', 'm').replace('8', 'n').replace('7', 'o').replace('6', 'p')
exten = inputFile.split('.')
extend = exten[1]
print('Saving: ')
fileout = str(exten[0]) + '_' + extend + '.DAT'
with open(fileout, 'a') as f: f.write(stringg)
os.system('rm tempr.txt')
print('Done: ')
