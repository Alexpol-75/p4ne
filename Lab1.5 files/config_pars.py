import glob

L_ip = []   # Список ip-адресов

for f in glob.glob('c:\\Python\\config_files\\*.txt'):      # Список файлов *.txt
    with open(f) as text_file:
        strings = list(text_file)                           # Читаем текстовый файл из списка
        for line in strings:                                # Цикл по строкам
            pos = line.find('ip address ')                  # Ищем признак ip-адреса и
            if pos > 0 and 'prefix' not in line:
                ip_mask =  line[pos:-1].replace('ip address ','').strip()   # Оставляем нужное
                L_ip.append(ip_mask)                                        # Добавляем адрес в список

L_unique_ip = list(set(L_ip))       # Список уникальных ip-адресов
for ip in L_unique_ip: print(ip)    # Печать списка

# Печать статистики
print(
    '\nTotal IP entries found:', len(L_ip),
    '\nTotal unique IP found:', len(L_unique_ip)
    )
