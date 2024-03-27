import pickle

# biblioteka do serializacji i deserializacji danych

lista = [1, 2, 3, 4, 5]
print(type(lista))  # <class 'list'>

# context manager
# usprawnia działaniez pliki, dba o obsługę błedów
# with
# Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================

with open('lista.txt', 'w') as fh:  # filehandler do pliku - taka rura do pliku
    fh.write(str(lista))  # str() - rzutowanie na stringa

with open('lista.txt', 'r') as f:
    data = f.read()

print(data)  # [1, 2, 3, 4, 5]
print(data[0])  # [
print(type(data))  # <class 'str'>

with open('lista.pickle', "wb") as f:
    pickle.dump(lista, f)

with open('lista.pickle', 'rb') as file:
    p = pickle.load(file)

print(p)  # [1, 2, 3, 4, 5]
print(type(p))  # <class 'list'>
print(p[0])  # 1

# serializacja
lista_ser = pickle.dumps(lista)
print(lista_ser)
# b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05e.'
# b - zapis bajtowy (binarny)
# \x - liczba w sytemie szesnastkowym \x95 -> 149

# deserializacja
print(pickle.loads(lista_ser))  # [1, 2, 3, 4, 5]
