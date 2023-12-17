import shelve
import tkinter as tk

window_user = tk.Tk()
window_user.geometry('200x100')
window_user['bg'] = 'Yellow'
enter_name_label = tk.Label(text='Enter a name:')
user_name_entry = tk.Entry()


def ok_button_click():
    user_name = user_name_entry.get()
    user_name_entry['state'] = 'disabled'
    with shelve.open('current_user') as file:
        file[user_name] = user_name
        file.close()


def anonim_button_click():
    window_user.destroy()


ok_bt = tk.Button(width=5, text='OK', command=ok_button_click)
play_bt = tk.Button(width=10, text='Play', command=anonim_button_click)
anonim_bt = tk.Button(width=20, text='Play anonymously', command=anonim_button_click)
enter_name_label.pack()
user_name_entry.pack()
ok_bt.place(x=160, y=18)
play_bt.place(x=20, y=43)
anonim_bt.place(x=20, y=70)
window_user.mainloop()
