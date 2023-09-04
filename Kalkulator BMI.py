import tkinter as tk

# Membuat jendela utama tkinter
root = tk.Tk()
root.geometry("800x450+370+125")
root.title("Kalkulator BMI Sederhana")
root.resizable(False, False)

# Mengubah warna latar belakang
root_warna = "#053B50"
root.configure(bg=root_warna)

# Mengubah ikon jendela tkinter menjadi kalkulator
profile_image_path = "icon2.png"
profile_img = tk.PhotoImage(file=profile_image_path)
root.iconphoto(True, profile_img)

# Membuat judul
Judul1 = tk.Label(root, text="Selamat Datang di Kalkulator BMI",font=("Impact", 25), fg="#64CCC5", bg=root_warna)
Judul1.pack()

# Membuat label dan entry untuk berat badan
label_berat = tk.Label(text="Berat badan  : ", fg="#64CCC5", bg=root_warna, font=("Impact", 15))
label_berat.place(x=20, y=100)

entry_berat = tk.Entry()
entry_berat.place(x=150, y=105)

# Membuat label dan entry untuk tinggi badan
label_tinggi = tk.Label(text="Tinggi badan :", fg="#64CCC5", bg=root_warna, font=("Impact", 15))
label_tinggi.place(x=20, y=150)

entry_tinggi = tk.Entry()
entry_tinggi.place(x=150, y=155)


# Membuat frame untuk memprint hasil
frame_hasil = tk.Frame(width=400, height=150, bg=root_warna)
frame_hasil.place(x=380, y=100)

#menjelaskan nilai bmi
penjelasan_bmi = "Kurang dari 18,5 berarti berat badan kurang (underweight).\nAntara 18,5 - 24,9 berarti berat badan normal\nAntara 25-29,9 berarti berat badan berlebih (overweight).\nDi atas 30 berarti obesitas"
penjelasan = tk.Label(root, text=penjelasan_bmi, font=("Impact", 15), bg=root_warna, fg="#64CCC5")
penjelasan.place(x=300, y= 190)

# Membuat fungsi tombol submit
# Membuat fungsi tombol submit
def tombol_submit():
    berat = float(entry_berat.get())
    tinggi = float(entry_tinggi.get())/100 

    try:
        if tinggi != 0:
            # Hitung BMI
            bmi = berat / tinggi**2

            # Format hasil BMI
            hasil_bmi = "Hasil BMI Anda adalah {:.2f}".format(bmi)
            print(bmi)

            #menghapus hasil yang lama
            for widget in frame_hasil.winfo_children():
                widget.destroy()

            # Tambahkan label baru setelah label_hasil
            label_hasil_baru = tk.Label(frame_hasil, text=hasil_bmi, font=("Impact", 15), bg=root_warna, fg="#64CCC5")
            label_hasil_baru.pack()
            
 

        else:
            # Tangani kasus ketika tinggi = 0
            label_hasil_baru = tk.Label(frame_hasil, text="Tinggi badan tidak boleh nol.", font=("Impact", 15), bg=root_warna, fg="#64CCC5")
            label_hasil_baru.pack()
    except ValueError:
        label_hasil_baru = tk.Label(frame_hasil, text="Masukan berat dan tinggi harus berupa angka.", font=("Impact", 15), bg=root_warna, fg="#64CCC5")
        label_hasil_baru.pack()



# Membuat Tombol Submit
tombol_submit = tk.Button(text="Submit", font=("Impact", 13), padx=7, pady=3, bg="#EEEEEE", fg=root_warna, command=tombol_submit)
tombol_submit.place(x=20, y=200)

root.mainloop()
