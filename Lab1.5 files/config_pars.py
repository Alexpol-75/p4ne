import glob
import time

time_start = time.perf_counter()
L_ip = []   # Список ip-адресов

for f in glob.glob('c:\\Python\\config_files\\*.txt'):      # Список файлов *.txt
    with open(f) as text_file:
        strings = list(text_file)                           # Читаем текстовый файл из списка
        for line in strings:                                # Цикл по строкам
            pos = line.find('ip address ')                  # Ищем признак ip-адреса и
            if pos > 0 and ('prefix' not in line) and ('dhcp' not in line):
                ip_mask =  line[pos:-1].replace('ip address ','').strip()   # Оставляем нужное
                L_ip.append(ip_mask)                                        # Добавляем адрес в список

L_unique_ip = list(set(L_ip))       # Список уникальных ip-адресов
for ip in L_unique_ip: print(ip)    # Печать списка

# Печать статистики
time_end = time.perf_counter()      # Время окончания программы
total_time = time_end - time_start  # Длительность исполнения программы в секундах
total_time_text = '{0:0.2f}'.format(total_time)

print(
    '\nTotal IP entries found:', len(L_ip),
    '\nTotal unique IP found:', len(L_unique_ip),
    '\n',
    '\nTotal Parsing Time: ' + str(total_time_text) + ' seconds'
)

