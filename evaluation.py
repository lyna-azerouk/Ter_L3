from understand import heuristique
from string import digits
import sys

sys.stdout = open('resultat.txt', 'w', encoding = 'utf-8')

my_file = open("exemples.txt", "r", encoding = 'utf-8')
content = my_file.readlines()
for line in content:
    line = line.replace("{","")
    line = line.replace("}","")
    remove_digits = str.maketrans('', '', digits)
    line = line.translate(remove_digits)
    line = line.replace(".","")
    line = line.replace("-","")
    line = line.replace("\n","")
    text = 'View from '+ line +'is so beautifaul today'
    heuristique(text)
sys.stdout.close()