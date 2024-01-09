import os
import shelve
import tkinter as tk


def best_count(file_name):
    count_dict = dict()
    with shelve.open(file_name, 'r') as file:
        for key, value in file.items():
            count_dict[key] = value
    file.close()
    combo_list = list()
    for count in count_dict.values():
        count: list
        combo_list.extend(count)
    combo_list.sort()
    interval = 5
    best_results_list = combo_list[0:interval]
    _best_results_dict = {}
    for result in best_results_list:
        for key, value in count_dict.items():
            if result in value:
                _best_results_dict[result] = key
    return _best_results_dict, interval


def del_click(file_name):
    os.remove(f'{file_name}.bak')
    os.remove(f'{file_name}.dat')
    os.remove(f'{file_name}.dir')
    return print('data deleted')


def final_widow(file_name, time_s):
    best_results_dict, interval = best_count(file_name)
    user = list(best_results_dict.values())
    time = list(best_results_dict.keys())

    window_res = tk.Tk()
    window_res.geometry('332x376+50+192')
    top_label = tk.Label(text=f'Your time: {int(time_s) // 60} min {int(time_s) % 60} sec', font=('Arial', 14))
    best_label = tk.Label(text='Best results:', font=('Arial', 14))
    first_label = tk.Label(text=f'1) {user[0]}:  {int(time[0]) // 60} min {int(time[0]) % 60} sec', font=('Arial', 14))
    if time[0] == time_s:
        first_label['bg'] = 'Yellow'
    try:
        second_label = tk.Label(text=f'2) {user[1]}:  {int(time[1]) // 60} min {int(time[1]) % 60} sec',
                                font=('Arial', 14))
    except IndexError:
        second_label = tk.Label(text='2) --- :   ---', font=('Arial', 14))
    if time[1] == time_s:
        second_label['bg'] = 'Yellow'
    try:
        third_label = tk.Label(text=f'3) {user[2]}:  {int(time[2]) // 60} min {int(time[2]) % 60} sec',
                               font=('Arial', 14))
    except IndexError:
        third_label = tk.Label(text='3) --- :   ---', font=('Arial', 14))
    if time[2] == time_s:
        third_label['bg'] = 'Yellow'
    try:
        fourth_label = tk.Label(text=f'4) {user[3]}:  {int(time[3]) // 60} min {int(time[3]) % 60} sec',
                                font=('Arial', 14))
    except IndexError:
        fourth_label = tk.Label(text='4) --- :   ---', font=('Arial', 14))
    if time[3] == time_s:
        fourth_label['bg'] = 'Yellow'
    try:
        fifth_label = tk.Label(text=f'5) {user[4]}:  {int(time[4]) // 60} min {int(time[4]) % 60} sec',
                               font=('Arial', 14))
    except IndexError:
        fifth_label = tk.Label(text='5) --- :   ---', font=('Arial', 14))
    if time[4] == time_s:
        fifth_label['bg'] = 'Yellow'
    del_button = tk.Button(text='Delete data', command=lambda: del_click(file_name))
    top_label.pack()
    best_label.pack()
    first_label.pack()
    second_label.pack()
    third_label.pack()
    fourth_label.pack()
    fifth_label.pack()
    del_button.pack()
    window_res.mainloop()
