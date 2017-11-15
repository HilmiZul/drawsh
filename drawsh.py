#!/usr/bin/env python
#
# July 27th 2016
# author: Zul Hilmi <netspytux@gmail.com
#
from Tkinter import *
#from tqdm import *
from time import *
import datetime
import tkMessageBox

root = Tk()
root.title(".: DRAWSH :.")

# Buat kanvas
kanvas = Canvas(root, width=800, height=500, bg="#fff")
kanvas.grid(row=12, column=0, columnspan=3)

# Func untuk membuat objek oval
def buat_oval():
  # jebak error
  try:
    xawal = float(entry_xawal.get())
    yawal = float(entry_yawal.get())
    xakhir = float(entry_xakhir.get())
    yakhir = float(entry_yakhir.get())
    coord = xawal,yawal,xakhir,yakhir # tangkap piksel xawal..yakhir
    warna_fill = entry_warna.get()

    print "Sedang membuat objek..."
    #waktu_awal = time() # waktu awal sebelum kanvas dibuat
    # ciptakan objek
    kanvas.create_oval(coord,fill=warna_fill)
    #waktu_eks = time() - waktu_awal
    #for i in tqdm(range(0,1)):
    #  sleep(waktu_eks)
    print "Objek telah dibuat.\n"
  except ValueError,e:
    print "Input gagal, karena:",e
    tkMessageBox.showerror("DUH!","Entri harus diisi angka :(")

  return

# Func untuk membuat garis
def buat_garis():
  try:
    xawal = float(entry_xawal.get())
    yawal = float(entry_yawal.get())
    xakhir = float(entry_xakhir.get())
    yakhir = float(entry_yakhir.get())
    coord = xawal,yawal,xakhir,yakhir # tangkap piksel xawal..yakhir
    warna_fill = entry_warna.get()

    print "Sedang membuat objek..."
    coord = xawal,yawal,xakhir,yakhir # tangkap piksel xawal..yakhir
    #waktu_awal = time() # waktu awal sebelum kanvas dibuat
    # ciptakan objek
    kanvas.create_line(coord,fill=warna_fill)
    #waktu_eks = time() - waktu_awal
    #for i in tqdm(range(0,1)):
    #  sleep(waktu_eks)
    print "Objek telah dibuat.\n"
  except ValueError,e:
    print "Input gagal, karena:",e
    tkMessageBox.showerror("DUH!","Entri harus diisi angka :(")

  return

# Prosedur hapus semua objek dikanvas untuk menggambar kembali
def hapus_objek():
  kanvas.delete(ALL)
  entry_xawal.delete(0,END)
  entry_yawal.delete(0,END)
  entry_xakhir.delete(0,END)
  entry_yakhir.delete(0,END)
  print "Semua Objek Telah dihapus"

# Prosedur memilih objek
def buat_objek():
  print "Halo :P"
  if varOps.get() == 'OVAL':
    print "Kamu memilih tipe: OVAL"
    buat_oval()
  elif varOps.get() == 'GARIS':
    print "Kamu memilih tipe: GARIS"
    buat_garis()


# Label
var1 = StringVar()
var1.set("X Awal:")
label1 = Label(root, textvariable=var1)
label1.grid(row=0,column=0, sticky=W)

var2 = StringVar()
var2.set("Y Awal:")
label2 = Label(root, textvariable=var2)
label2.grid(row=1,column=0, sticky=W)

var3 = StringVar()
var3.set("X Akhir:")
label3 = Label(root, textvariable=var3)
label3.grid(row=2,column=0, sticky=W)

var4 = StringVar()
var4.set("Y Akhir:")
label4 = Label(root, textvariable=var4)
label4.grid(row=3,column=0, sticky=W)

var5 = StringVar()
var5.set("Warna Fill:")
label5 = Label(root, textvariable=var5)
label5.grid(row=4,column=0, sticky=W)

var6 = StringVar()
var6.set("Tipe Objek:")
label6 = Label(root, textvariable=var6)
label6.grid(row=5, column=0, sticky=W)

# Entry objek oval
entry_xawal = Entry(root)
entry_xawal.grid(row=0, column=0)
entry_yawal = Entry(root)
entry_yawal.grid(row=1, column=0)
entry_xakhir = Entry(root)
entry_xakhir.grid(row=2, column=0)
entry_yakhir = Entry(root)
entry_yakhir.grid(row=3, column=0)
entry_warna = Entry(root)
entry_warna.grid(row=4, column=0)
# Opsi tipe objek
varOps = StringVar()
varOps.set("OVAL")
opsi = OptionMenu(root, varOps, "OVAL", "GARIS")
opsi.grid(row=5, column=0)

batas = Label(root)
batas.grid(row=6, pady=10)

# Tombol Buat Objek
tblBuatObjek = Button(root,text="Buat Objek",width=10, command=buat_objek)
tblBuatObjek.grid(row=0, column=1, rowspan=2, sticky=W)
# Tombol Hapus semua objek
tblHapusObjek = Button(root,text="Hapus Objek",width=10, command=hapus_objek)
tblHapusObjek.grid(row=2, column=1, rowspan=2, sticky=W)
# Tombol keluar
tblExit = Button(root,text="Keluar",width=10, command=quit)
tblExit.grid(row=4, column=1, rowspan=2, sticky=W)


# Jalankan programnya :D
if __name__ == '__main__':
  root.mainloop()
