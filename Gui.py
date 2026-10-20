
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("600x750")
root.resizable(False, False)
root.configure(bg="#202b68")


def hasil_prediksi():
    jendela_hasil = tk.Toplevel(root)
    jendela_hasil.title("Hasil Prediksi Prodi")
    jendela_hasil.geometry("420x220")
    jendela_hasil.resizable(False, False)
    jendela_hasil.configure(bg="#182653")

    tk.Label(
        jendela_hasil,
        text="HASIL PREDIKSI",
        font=("Arial", 16, "bold"),
        bg="#182653",
        fg="#42e8f5"
    ).pack(pady=(30, 20))

tk.Label(
        jendela_hasil,
        text="Prodi Pilihan: Teknologi Informasi",
        font=("Arial", 12, "bold"),
        bg="#182653",
        fg="white"
    ).pack(pady=10)

tk.Button(
        jendela_hasil,
        text="Tutup",
        command=jendela_hasil.destroy
    ).pack(pady=15)

# 3. Label judul aplikasi
judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 16, "bold"),
    bg="#202b68",
    fg="white"
)
judul.pack(pady=20)






   

