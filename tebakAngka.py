Nama = input("Nama : ")
A = [None]*7

print("1. Pertanyaan Pertama")
print("| |1| |3|4| |6| |8| |10|  |  |13|  |15|")
A[0] = int(input("Apakah angka yang " + Nama + " pilih ada di sini? "))

print("Pertanyaan Kedua")
print("| |1|2| | |5|6| |8| |  |11|12|  |  |15|")
A[1] = int(input("Apakah angka yang " + Nama + " pilih ada di sini? "))

print("Pertanyaan Ketiga")
print("| | | | | | | | |8|9|10|11|12|13|14|15|")
A[2] = int(input("Apakah angka yang " + Nama + " pilih ada di sini? "))

print("4. Pertanyaan Keempat")
print("| |1|2| |4| | |7| |9|10|  |12|  |  |15|")
A[3] = int(input("Apakah angka yang " + Nama + " pilih ada di sini? "))

print("5.Pertanyaan Kelima")
print("| | | | |4|5|6|7| | |  |  |12|13|14|15|")
A[4] = int(input("Apakah angka yang " + Nama + " pilih ada di sini? "))

print("6. Pertanyaan Keenam")
print("| | |2|3| | |6|7| | |10|11|  |  |14|15|")
A[5] = int(input("Apakah angka yang " + Nama + " pilih ada di sini? "))

print("7. Pertanyaan Ketujuh")
print("| |1| |3| |5| |7| |9|  |11|  |13|  |15|")
A[6] = int(input("Apakah angka yang " + Nama + " pilih ada di sini? "))

P1 = (A[0] + A[2] + A[4] + A[6]) % 2
P2 = (A[1] + A[2] + A[5] + A[6]) % 2
P3 = (A[3] + A[4] + A[5] + A[6]) % 2
Bohong = P1 + 2*P2 + 4*P3


if Bohong != 0:
    A[Bohong-1] = 1 - A[Bohong-1]

N = 8 * A[2] + 4 * A[4] + 2 * A[5] + A[6]

print('Angka yang kamu pilih adalah : ' + str(N))