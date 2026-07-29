import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen('http://www.pudim.com.br', timeout=5)
except urllib.error.URLError:
    print('O site não está disponível no momento.')
else:
    print('Consegui acesso ao site!')
    site.close()