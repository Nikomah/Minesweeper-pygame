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
        combo_list.extend(count)
    combo_list.sort()
    best_results_list = combo_list[0:5]
    _best_results_dict = {}
    for result in best_results_list:
        for key, value in count_dict.items():
            if result in value:
                _best_results_dict[result] = key
    return _best_results_dict


def final_widow(file_name, time_s):
    best_results_dict = best_count(file_name)
    user = list(best_results_dict.values())
    time = list(best_results_dict.keys())

    window_res = tk.Tk()
    top_label = tk.Label(text=f'Your time: {time_s}')
    best_label = tk.Label(text='Best results:')
    first_label = tk.Label(text=f'1) {user[0]}:  {time[0]}')
    try:
        second_label = tk.Label(text=f'2) {user[1]}:  {time[1]}')
    except IndexError:
        second_label = tk.Label(text=' --- :   ---')
    try:
        third_label = tk.Label(text=f'3) {user[2]}:  {time[2]}')
    except IndexError:
        third_label = tk.Label(text=' --- :   ---')
    try:
        fourth_label = tk.Label(text=f'4) {user[3]}:  {time[3]}')
    except IndexError:
        fourth_label = tk.Label(text=' --- :   ---')
    try:
        fifth_label = tk.Label(text=f'5) {user[4]}:  {time[4]}')
    except IndexError:
        fifth_label = tk.Label(text=' --- :   ---')
    top_label.pack()
    best_label.pack()
    first_label.pack()
    second_label.pack()
    third_label.pack()
    fourth_label.pack()
    fifth_label.pack()
    window_res.mainloop()
