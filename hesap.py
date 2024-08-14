def toplama(a, b): 
return a + b 
def cikarma(a, b): 
return a - b 
def carpma(a, b): 
return a * b 
def bolme(a, b): 
if b == 0: 
return "Hata: Sıfıra bölme işlemi yapılamaz." 
return a / b 
def hesap_makinesi(): 
print("Basit Hesap Makinesi") 
print("1. Toplama") 
print("2. Çıkarma") 
print("3. Çarpma") 
print("4. Bölme") 
secim = input("İşlemi seçin (1/2/3/4): ") 
num1 = float(input("İlk sayıyı girin: ")) 
num2 = float(input("İkinci sayıyı girin: ")) 
  
    if secim == '1': 
        sonuc = toplama(num1, num2) 
    elif secim == '2': 
        sonuc = cikarma(num1, num2) 
    elif secim == '3': 
        sonuc = carpma(num1, num2) 
    elif secim == '4': 
        sonuc = bolme(num1, num2) 
    else: 
        sonuc = "Geçersiz bir seçim yaptınız." 
  
    print(f"Sonuç: {sonuc}") 
  
if __name__ == "__main__": 
    hesap_makinesi()
