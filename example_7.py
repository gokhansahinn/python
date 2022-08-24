ogrenciler={
    '120':{
        'ad':'Ali',
        'soyad': 'Yılmaz',
        'telefon':'0532054565646'

    },
    '125':{
        'ad':'Can',
        'soyad':'Kormaz',
        'telefon':'0545524554554'
        
    },
    '128':{
        'ad':'Volkan',
        'soyad':'Yükselen',
        'telefon':'54632785415665'
    }
}
#1- Bilgileri verilen öğrencilerin kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
student_number=input('enter student number: ')
student_name=input('enter student name: ')
student_surname= input('enter student surname: ')
student_telephone= input('enter student tel_no: ')

# ogrenciler[student_number]={
#     'ad':student_name,
#     'soyad':student_surname,
#     'telefon':student_telephone
# }
ogrenciler.update({
    student_number:{
        'ad':student_name,
        'soyad':student_surname,
        'telefon':student_telephone
    }
})
print(ogrenciler)

#2 -Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.

student_no= input('enter student no to find information')
print(ogrenciler[student_no])
