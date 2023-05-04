import sys
import glob
import subprocess
import os
from pathlib import Path

#USAGE: FIRST ARG INPUT FILENAME, SECOND JUST FILENAME WITHOUT EXTENSION. ALL ZIP FILES WILL BE INSTALLED AFTER UNPACK. ZIP FILE MUST BE NAMED SAME AS THE DIR
inputFile = sys.argv[1]
extron = inputFile.split('_')
extron360 = extron[0]
ext =  inputFile.split('.')
extt = str(ext[0])
exttt = extt.split('_')
extttt = '.' + str(exttt[1])
print('Running: ')
file = open(inputFile, 'r')
data = file.read()
clean_data = data.replace('\n', '')
file.close()
stringg = clean_data.replace('g', '5').replace('h', '4').replace('i', '3').replace('j', '2').replace('k', '1').replace('l', '0').replace('m', '9').replace('n', '8').replace('o', '7').replace('p', '6')
filestrr = extron360 + extttt
with open('temp.txt', 'a') as f: f.write(stringg)
hexdumpcommand = 'xxd --revert --plain ' + 'temp.txt' + ' > ' + filestrr
print('Saving: ')
os.system(hexdumpcommand)
os.system('rm temp.txt')
if (extttt == '.zip'):
  tryu = 'unzip ' + filestrr
  os.system(tryu)
  trooo = 'cd ' + extron360 + ' && ' + 'sh main.sh'
  os.system(trooo)
  bronk = 'echo y | rm ' + filestrr
  os.system(bronk)
print('Done: ')
