from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk,Image

hunians = []
hunians.append(Apartemen("Nelly Joy", 3, 3, "assets/appartement1.jpg"))
hunians.append(Rumah("Sekar MK", 5, 2, "assets/house1.jpg"))
hunians.append(Indekos("Bp. Romi", "Cahya", "assets/kost1.jpg", 9000000))
hunians.append(Rumah("Satria", 1, 4, "assets/house2.jpeg"))

root = Tk()
root.title("LP DPBO: Python GUI")

def show_hunians():
    # Hapus landing frame
    landing_frame.pack_forget()

    # Munculkan frame berikutnya
    frame.pack(padx=10, pady=10)
    opts.pack(padx=10, pady=10)

# Landing farme

landing_frame = Frame(root, padx=10, pady=10)
landing_frame.pack(padx=10, pady=10)

landing_text = Label(landing_frame, text="Selamat Datang!")
landing_text.pack(pady=10)

landing_button = Button(landing_frame, text="Lanjut", command=show_hunians)
landing_button.pack()

def details(index):
    # Buat window baru
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    # Frame dalam window baru
    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    # Summary
    d_summary = Label(d_frame, text="Summary:\n" + hunians[index].get_detail() + hunians[index].get_summary() + "\n" + hunians[index].get_dokumen(), anchor="w", justify=LEFT)
    d_summary.grid(row=0, column=0, sticky="w")

    # Label gambar
    picture_label = Label(d_frame, text="Foto bangunan:")
    picture_label.grid(row=1, column=0, sticky="w")

    # Setup gambar
    foto = Image.open(hunians[index].get_foto_bangunan())
    width, height = foto.size
    new_width = 400
    ratio = new_width / width
    new_height = int(height * ratio)
    foto = foto.resize((new_width, new_height))

    # Display gambar
    foto = ImageTk.PhotoImage(foto)
    foto_label = Label(d_frame, image=foto)
    foto_label.grid(row=2, column=0, sticky="w")
    foto_label.image = foto

    btn = LabelFrame(top, padx=0, pady=0)
    btn.pack(padx=10, pady=10)
    b_close = Button(btn, text="Close", command=top.destroy)
    b_close.grid(row=0, column=0)

# Main frame

frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)

for index, h in enumerate(hunians):
    idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
    idx.grid(row=index, column=0)

    type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
    type.grid(row=index, column=1)

    if h.get_jenis() != "Indekos": 
        name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)
    else:
        name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)

    b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
    b_detail.grid(row=index, column=3)

# Opts frame

opts = LabelFrame(root, padx=10, pady=10)

b_add = Button(opts, text="Add Data", state="disabled")
b_add.grid(row=0, column=0)

b_exit = Button(opts, text="Exit", command=root.quit)
b_exit.grid(row=0, column=1)

root.mainloop()
