
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

judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 16, "bold"),
    bg="#202b68",
    fg="white"
)
judul.pack(pady=20)


frame_input = tk.Frame(root, bg="#202b68")
frame_input.pack(padx=40, fill="x")

input_nilai = []

for i in range(1, 11):
    baris = tk.Frame(frame_input, bg="#202b68")
    baris.pack(fill="x", pady=4)

    tk.Label(
        baris,
        text=f"Nilai Mata Pelajaran {i}:",
        font=("Arial", 10),
        bg="#202b68",
        fg="white",
        width=25,
        anchor="w"
    ).pack(side="left")


    entry_nilai = tk.Entry(
        baris,
        font=("Arial", 10),
        width=20
    )
    entry_nilai.pack(side="right")

    input_nilai.append(entry_nilai)


tk.Label(
    root,
    text="Pilihan Jurusan Anda:",
    font=("Arial", 10, "bold"),
    bg="#202b68",
    fg="white"
).pack(pady=(15, 5))


pilihan_jurusan = tk.StringVar(
    value="Teknologi Informasi"
)
dropdown_jurusan = ttk.Combobox(
    root,
    textvariable=pilihan_jurusan,
    values=[
        "Teknologi Informasi",
        "Informatika",
        "Sistem Informasi",
        "Teknik Komputer",
        "Manajemen Informatika"
    ],
    state="readonly",
    width=27
)
dropdown_jurusan.pack()

tk.Button(
    root,
    text="Hasil Prediksi",
    command=hasil_prediksi,
    font=("Arial", 11, "bold"),
    bg="#e3e9ff",
    fg="#202b68",
    padx=15,
    pady=6,
    cursor="hand2"
).pack(pady=22)

root.mainloop()


