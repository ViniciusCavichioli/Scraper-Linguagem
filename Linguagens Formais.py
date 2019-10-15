import requests
import re

# URLs
data = requests.get('http://ulbra-to.br/2011/02/05/Telefones-e-e-mails')
data1 = requests.get ('http://ulbra-to.br/espaco-academico/2011/02/07/Ouvidoria')

# Expressao regular
phones = re.findall (r'[0-9]{4}\-[0-9]{4}', data.text)
emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)

phones1 = re.findall (r'(?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}', data1.text)
emails1 = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data1.text)

#Prints

#URL DATA
print('Dados da URL data:')
print('   Telefones:\n')
print(phones,'\n')
print('   Emails:\n')
print(emails,'\n')

#URL DATA 1
print('Dados da URL data1:')
print('   Telefones:\n')
print(phones1,'\n')
print('   Emails:\n')
print(emails1,'\n')

