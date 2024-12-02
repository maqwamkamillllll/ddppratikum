# bangun_datar.py
import math

# Fungsi untuk menghitung Luas dan Keliling Lingkaran
def luas_lingkaran(radius):
    return math.pi * (radius ** 2)

def keliling_lingkaran(radius):
    return 2 * math.pi * radius

# Fungsi untuk menghitung Luas dan Keliling Persegi
def luas_persegi(sisi):
    return sisi * sisi

def keliling_persegi(sisi):
    return 4 * sisi

# Fungsi untuk menghitung Luas dan Keliling Segitiga
def luas_segitiga(alas, tinggi):
    return (alas * tinggi) / 2

def keliling_segitiga(sisi1, sisi2, sisi3):
    return sisi1 + sisi2 + sisi3

# Fungsi untuk menghitung Luas dan Keliling Persegi Panjang
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

# Fungsi untuk menghitung Luas dan Keliling Jajar Genjang
def luas_jajar_genjang(alas, tinggi):
    return alas * tinggi

def keliling_jajar_genjang(sisi1, sisi2):
    return 2 * (sisi1 + sisi2)
