"""
    1-Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

        Müşteri adı
        Müşteri soyadı
        Müşteri ad+ soyad
        Müşteri cinsiyet
        Müşteri tc kimlik numarası
        Müşteri doğum yılı
        Müşteri adres bilgisi
        Müşteri yaşı
"""    
"""
    2- Aşağıdaki toplam bilgisini hesaplayınız
            Sipariş 1=> 110 TL
            Sipariş 2=> 1100.5 TL
            Sipariş 3=> 356.95 TL
            
"""
#1. Soru Çözümü

Customer_name="Muhammed"
Customer_lastname="\tŞentop"
Customer_name_last_name=Customer_name+Customer_lastname
Customer_gender="Male"
Customer_ID=123456789
Customer_birthday=1997
Customer_adress="Bornova/IZMIR"
date=2022
Custemer_age=date-1997

print(Custemer_age)
#2.SORU ÇÖZÜMÜ

order1,order2,order3=(110,1100.5,356.95)
total_receipt=order1+order2+order3
print(total_receipt)

