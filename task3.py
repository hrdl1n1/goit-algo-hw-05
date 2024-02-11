import os
import sys
import pathlib
from collections import Counter

mistake_dict = {'ERROR','INFO','DEBUG','WARNING'}

def load_logs(file_path: str) -> list:
    list_logs = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            for line in f.readlines():
                list_logs.append(parse_log_line(line))
        return list_logs

    else:
        print('The specified file does NOT exist')


def parse_log_line(line: str)-> dict:

    date, time, log, *message = line.split()
    mistake = ' '.join(message)
    dict_={'date': date ,'time': time ,'type': log ,'mistake': mistake}
    return dict_


def count_logs_by_level(list) -> dict:
    errors_dict = Counter([d['type'] for d in list])
    return errors_dict


def display_log_counts(errors_dict):
    print(f'Рівень логування | Кількість')
    print('_ _ _ _ _ _ _ _ _| _ _ _ _ _ ') 
    for key, value in errors_dict.items():
        print(f'{key}\t\t | {value}')


def filter_logs_by_level(list, level):
    print(f'Деталі логів для рівня {level}:')
    for item in list:
        if item['type']==level:
            print(f'{item['date']} {item['time']} - {item['mistake']}')



try:
    input = sys.argv[1]
    adress= pathlib.Path(input)
    dict_lines = load_logs(adress)
    conuted_logs = count_logs_by_level(dict_lines)
    display_log_counts(conuted_logs)

    log_level = sys.argv[2]
    if log_level.upper() in mistake_dict:
        filter_logs_by_level(dict_lines, log_level.upper())
    else:
        print('Некоректний параметр логування')
except:
    pass