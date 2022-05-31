import glob
import re
import ipaddress
import time
d

def classify(l):
    line = l.strip()
    while '  ' in line: line = line.replace('  ', ' ')
    m1 = re.match('^ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)',line)
    m2 = re.match('^interface (.+)', line)
    m3 = re.match('^hostname (.+)', line)
    if bool(m1): return {"ip":ipaddress.IPv4Interface(str(m1.group(1)) + '/' + str(m1.group(2)))}
    if bool(m2): return {"int":m2.group(1)}
    if bool(m3): return {"host":m3.group(1)}
    return 'n/a'

time_start = time.perf_counter()

L_ip = []   # Список ip-адресов
L_int = []
L_host = []

for f in glob.glob('c:\\Python\\config_files\\*.txt'):      # Список файлов *.txt
    with open(f) as text_file:
        strings = list(text_file)                           # Читаем текстовый файл из списка
        for line in strings:                                # Цикл по строкам
            c = classify(line)
            if 'ip' in c: L_ip.append(c)
            if 'int' in c: L_int.append(c)
            if 'host' in c: L_host.append(c)

print(L_ip)
print(L_int)
print(L_host)

# Печать статистики
total_time_text = '{0:0.2f}'.format(time.perf_counter()-time_start)

print(
    '\nTotal IP entries found:', len(L_ip),
    '\nTotal interfaces found:', len(L_int),
    '\nTotal hosts found:', len(L_int),
    '\n',
    '\nTotal Parsing Time: ' + str(total_time_text) + ' seconds'
)