import shelve
import tkinter as tk

window_user = tk.Tk()
window_user.geometry('432x576+742+222')
window_user['bg'] = 'Yellow'
enter_name_label = tk.Label(text='Enter a name:', font=('Arial', 14))
user_name_entry = tk.Entry(font=('Arial', 14))


def ok_button_click():
    user_name = user_name_entry.get()
    user_name_entry['state'] = 'disabled'
    play_bt['state'] = 'active'
    with shelve.open('current_user') as file:
        file[user_name] = user_name
        file.close()


ok_bt = tk.Button(width=5, text='OK', command=ok_button_click, font=('Arial', 14))
play_bt = tk.Button(state='disabled', width=10, text='Play', command=lambda: window_user.destroy(), font=('Arial', 14))
anonim_bt = tk.Button(width=20, text='Play anonymously', command=lambda: window_user.destroy(), font=('Arial', 14))
enter_name_label.pack()
user_name_entry.pack()
ok_bt.place(x=290, y=20)
play_bt.place(x=20, y=60)
anonim_bt.place(x=20, y=100)
window_user.mainloop()


def stub():
    pass
