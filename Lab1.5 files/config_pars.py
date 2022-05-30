import glob

L_ip = []   # Список ip-адресов

for f in glob.glob('c:\\Python\\config_files\\*.txt'):
    with open(f) as textf:
        strings = list(textf)
        for line in strings:
            pos = line.find('ip address ')
            if pos >0 and 'prefix' not in line:
                ip_mask =  line[pos:-1].replace('ip address ','').strip()
                L_ip.append(ip_mask)

L_unique_ip = list(set(L_ip))       # Список уникальных ip-адресов
for ip in L_unique_ip: print(ip)    # Печать списка

# Печать статистики
print(
    '\nTotal IP entries found:', len(L_ip),
    '\nTotal unique IP found:', len(L_unique_ip)
    )
