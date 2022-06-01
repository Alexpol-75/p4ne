from flask import Flask, jsonify
import glob
import re
import ipaddress
import pprint

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/configs')
def configs():
    return jsonify(hosts)

@app.route('/configs/<hostname>')
def configs_host(hostname):
    return jsonify(ip_by_host[hostname]['ip'])

def classify(l,f):
    line = l.strip()
    while '  ' in line: line = line.replace('  ', ' ')
    m = re.match('^ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)',line)
    if m: return {'ip': ipaddress.IPv4Interface(str(m.group(1)) + '/' + str(m.group(2))), 'file':f}

    m = re.match('^interface (.+)', line)
    if m: return {'int': m.group(1), 'file':f}

    m = re.match('^hostname (.+)', line)
    if m: return {'host':m.group(1), 'file':f}

    return 'n/a'

if __name__ == '__main__':
    L_ip = []
    L_int = []
    L_host = []
    ip_by_host = dict()

    for f in glob.glob('c:\\Python\\config_files\\*.txt'):  # Список файлов *.txt
        with open(f) as text_file:

            strings = list(text_file)  # Читаем текстовый файл из списка
            for line in strings:  # Цикл по строкам
                c = classify(line,f)
                if 'ip' in c: L_ip.append(c)
                if 'int' in c: L_int.append(c)
                if 'host' in c: L_host.append(c)

            host = L_host[-1]['host']
            ip = L_ip[-1]['ip']
            ip_by_host[host] = {'file':f, 'host':host, 'ip':str(ip)}

    #pprint.pprint(ip_by_host)

    hosts = []  # Список уникальных хостов
    for c in L_host:
        if c['host'] not in hosts: hosts.append(c['host'])

    app.run(debug=True)

