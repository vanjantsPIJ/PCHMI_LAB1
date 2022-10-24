import tkinter as tk


def fahrenheit_to_celsius():
    fahrenheit = fahr_ent_temperature.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    fahr_lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


def celsius_to_fahrenheit():
    celsius = cels_ent_temperature.get()
    fahrenheit = 32 + (float(celsius) * (9 / 5))
    cels_lbl_result["text"] = f"{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}"


def kelvin_to_celsius():
    kelvin = KelvCels_ent_temperature.get()
    celsius = float(kelvin) - 273.15
    KelvCels_lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


def kelvin_to_fahrenheit():
    kelvin = KelvFahr_ent_temperature.get()
    fahrenheit = (float(kelvin) - 273.15) * 9 / 5 + 32
    KelvFahr_lbl_result["text"] = f"{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}"


def celsium_to_kelvin():
    celsius = CelsKelv_ent_temperature.get()
    kelvin = float(celsius) + 273.15
    CelsKelv_lbl_result["text"] = f"{round(kelvin, 2)} \N{KELVIN SIGN}"


def fahrenheit_to_kelvin():
    fahrenheit = FahrKelv_ent_temperature.get()
    kelvin = (float(fahrenheit) - 32) * 5 / 9 + 273.15
    FahrKelv_lbl_result["text"] = f"{round(kelvin, 2)} \N{KELVIN SIGN}"


# Создание окна.
window = tk.Tk()
window.geometry("250x350")
window.title("Конвертер температуры")
window.resizable(width=False, height=False)

# Блок Фаренгейт -> Цельсий /////////////////////////////////////////////////
fahr_frm_entry = tk.Frame(master=window)
fahr_ent_temperature = tk.Entry(master=fahr_frm_entry, width=10)
fahr_lbl_temp = tk.Label(master=fahr_frm_entry, text="\N{DEGREE FAHRENHEIT}")


fahr_ent_temperature.grid(row=1, column=0, sticky="e")
fahr_lbl_temp.grid(row=1, column=1, sticky="w")


fahr_btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)
fahr_lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")


fahr_frm_entry.grid(row=1, column=0, padx=10)
fahr_btn_convert.grid(row=1, column=1, pady=10)
fahr_lbl_result.grid(row=1, column=2, padx=10)
# Блок Фаренгейт -> Цельсий закончен /////////////////////////////////////////

# Блок Цельсий -> Фаренгейт /////////////////////////////////////////////////////////
cels_frm_entry = tk.Frame(master=window)
cels_ent_temperature = tk.Entry(master=cels_frm_entry, width=10)
cels_lbl_temp = tk.Label(master=cels_frm_entry, text="\N{DEGREE CELSIUS}")

cels_ent_temperature.grid(row=2, column=0, sticky="e", pady=20)
cels_lbl_temp.grid(row=2, column=1, sticky="w")

cels_btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=celsius_to_fahrenheit
)
cels_lbl_result = tk.Label(master=window, text="\N{DEGREE FAHRENHEIT}")

cels_frm_entry.grid(row=2, column=0, padx=10,)
cels_btn_convert.grid(row=2, column=1, pady=10)
cels_lbl_result.grid(row=2, column=2, padx=10,)
# Окончание блока Цельсий -> Фаренгейт /////////////////////////////////////////////

# Блок Кельвин -> Цельсий ///////////////////////////////////////////////////////////
KelvCels_frm_entry = tk.Frame(master=window)
KelvCels_ent_temperature = tk.Entry(master=KelvCels_frm_entry, width=10)
KelvCels_lbl_temp = tk.Label(master=KelvCels_frm_entry, text="\N{KELVIN SIGN}")

KelvCels_ent_temperature.grid(row=3, column=0, sticky="e", pady=20)
KelvCels_lbl_temp.grid(row=3, column=1, sticky="w")

KelvCels_btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=kelvin_to_celsius
)
KelvCels_lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

KelvCels_frm_entry.grid(row=3, column=0, padx=10,)
KelvCels_btn_convert.grid(row=3, column=1, pady=10)
KelvCels_lbl_result.grid(row=3, column=2, padx=10,)
# Окончание блока Кельвин -> Цельсий ///////////////////////////////////////////////

# # Блок Кельвин -> Фаренгейт //////////////////////////////////////////////////////
KelvFahr_frm_entry = tk.Frame(master=window)
KelvFahr_ent_temperature = tk.Entry(master=KelvFahr_frm_entry, width=10)
KelvFahr_lbl_temp = tk.Label(master=KelvFahr_frm_entry, text="\N{KELVIN SIGN}")

KelvFahr_ent_temperature.grid(row=4, column=0, sticky="e", pady=20)
KelvFahr_lbl_temp.grid(row=4, column=1, sticky="w")

KelvFahr_btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=kelvin_to_fahrenheit
)
KelvFahr_lbl_result = tk.Label(master=window, text="\N{DEGREE FAHRENHEIT}")

KelvFahr_frm_entry.grid(row=4, column=0, padx=10,)
KelvFahr_btn_convert.grid(row=4, column=1, pady=10)
KelvFahr_lbl_result.grid(row=4, column=2, padx=10,)
# Окончание блока Кельвин -> Фаренгейт//////////////////////////////////////////

# Блок Цельсий -> Кельвин ///////////////////////////////////////////////////////////
CelsKelv_frm_entry = tk.Frame(master=window)
CelsKelv_ent_temperature = tk.Entry(master=CelsKelv_frm_entry, width=10)
CelsKelv_lbl_temp = tk.Label(master=CelsKelv_frm_entry, text="\N{DEGREE CELSIUS}")

CelsKelv_ent_temperature.grid(row=5, column=0, sticky="e", pady=20)
CelsKelv_lbl_temp.grid(row=5, column=1, sticky="w")

CelsKelv_btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=celsium_to_kelvin
)
CelsKelv_lbl_result = tk.Label(master=window, text="\N{KELVIN SIGN}")

CelsKelv_frm_entry.grid(row=5, column=0, padx=10,)
CelsKelv_btn_convert.grid(row=5, column=1, pady=10)
CelsKelv_lbl_result.grid(row=5, column=2, padx=10,)
# Окончание блока Цельсий -> Кельвин ///////////////////////////////////////////////

# # Блок Фаренгейт -> Кельвин //////////////////////////////////////////////////////
FahrKelv_frm_entry = tk.Frame(master=window)
FahrKelv_ent_temperature = tk.Entry(master=FahrKelv_frm_entry, width=10)
FahrKelv_lbl_temp = tk.Label(master=FahrKelv_frm_entry, text="\N{DEGREE FAHRENHEIT}")

FahrKelv_ent_temperature.grid(row=6, column=0, sticky="e", pady=20)
FahrKelv_lbl_temp.grid(row=6, column=1, sticky="w")

FahrKelv_btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_kelvin
)
FahrKelv_lbl_result = tk.Label(master=window, text="\N{KELVIN SIGN}")

FahrKelv_frm_entry.grid(row=6, column=0, padx=10,)
FahrKelv_btn_convert.grid(row=6, column=1, pady=10)
FahrKelv_lbl_result.grid(row=6, column=2, padx=10,)
# Окончание блока Фаренгейт -> Кельвин//////////////////////////////////////////

# Запуск приложения.
window.mainloop()
