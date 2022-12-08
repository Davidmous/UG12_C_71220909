a=input('Masukan Angka : ')
ah=input('Masukan Angka Yang Dihitung : ')
d=0
for i in list(a):
    if i == ah:
        d = d + 1
print('Angka', ah, 'Muncul Sebanyak', d, 'kali')
