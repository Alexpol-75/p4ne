import glob
import re
import ipaddress
import time

def classify(l):
    line = l.strip()
    while '  ' in line: line = line.replace('  ', ' ')
    m1 = re.match('^ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)',line)
    m2 = re.match('^interface (.+)', line)
    m3 = re.match('^hostname (.+)', line)
    if bool(m1): return {'ip':ipaddress.IPv4Interface(str(m1.group(1)) + '/' + str(m1.group(2)))}
    if bool(m2): return {'int':m2.group(1)}
    if bool(m3): return {'host':m3.group(1)}
    return 'n/a'

time_start = time.perf_counter()

L_ip = []
L_int = []
L_host = []
line_cnt = 0    # Счетчик файлов
file_cnt = 0    # Счетчик строк

for f in glob.glob('c:\\Python\\config_files\\*.txt'):      # Список файлов *.txt
    with open(f) as text_file:
        file_cnt += 1
        strings = list(text_file)                           # Читаем текстовый файл из списка
        for line in strings:                                # Цикл по строкам
            line_cnt += 1
            c = classify(line)
            if 'ip' in c: L_ip.append(c)
            if 'int' in c: L_int.append(c)
            if 'host' in c: L_host.append(c)

#print(L_ip)
#print(L_int)
#print(L_host)

ips = []                # Список уникальных IP
ints = []               # Список уникальных интерфейсов
hosts = []              # Список уникальных хостов

# Преобразуем словари в списки уникальных значений
for c in L_ip:
    if c['ip'] not in ips: ips.append(c['ip'])
for c in L_int:
    if c['int'] not in ints: ints.append(c['int'])
for c in L_host:
    if c['host'] not in hosts: hosts.append(c['host'])

print('\n***** IP-Addresses *****\n', sorted(ips))
print('\n***** Interfaces *****\n', sorted(ints))
print('\n***** Hosts *****\n', sorted(hosts))
#print(len(ips), len(ints), len(hosts))

# Печать статистики
total_time_text = '{0:0.2f}'.format(time.perf_counter()-time_start)
print(
    '\n# Total files processed:',           file_cnt,
    '\n# Total lines processed:',           line_cnt,
    '\n#    - unique IP entries found:',    len(ips),
    '\n#    - unique interfaces found:',    len(ints),
    '\n#    - unique hosts found:',         len(hosts),
    '\n# Total Parsing Time: ' + str(total_time_text) + ' seconds')