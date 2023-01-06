# Nama : Fara Deviana
# NIM : 312010407
# Kelas : TI.E1
# Mata Kuliah : Kriptografi


def encrypt(text, key):
  # membuat string kosong untuk menampung hasil enkripsi
  encrypted_text = ""
  
  # mengulangi setiap karakter dalam string
  for i in range(len(text)):
    # menambahkan hasil XOR antara karakter dengan kunci ke string yang telah dienkripsi
    encrypted_text += chr(ord(text[i]) ^ key)
  
  # mengembalikan hasil enkripsi
  return encrypted_text

def decrypt(encrypted_text, key):
  # membuat string kosong untuk menampung hasil dekripsi
  text = ""
  
  # mengulangi setiap karakter dalam string yang telah dienkripsi
  for i in range(len(encrypted_text)):
    # menambahkan hasil XOR antara karakter dengan kunci ke string yang telah didekripsi
    text += chr(ord(encrypted_text[i]) ^ key)
  
  # mengembalikan hasil dekripsi
  return text

# mencoba enkripsi dan dekripsi
text = "Saya harus lulus tepat waktu dan menjadi sarjana"
key = 10

encrypted_text = encrypt(text, key)
print(encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print(decrypted_text)
