import requests
from bs4 import BeautifulSoup

login = int(input("""Türkçe sonuçlar için 1'e basınız.
for English press 2.\n"""))


def Login():
    if login == 1:
        return Turkish()
    elif login == 2:
        return English()
    else:
        print("""   Lütfen geçerli bir tercih yapınız! \n   Please make a valid choose""")



def Turkish():
    url = "https://tr.azrhymes.com/?tekerlemeler" #kafiyeli kelimeleri oluşturan site
    word = input("Kafiye için bir kelime giriniz :  ")
    count = int(input("Kaç adet kelime istiyorsunuz :  ")) 
    url_req = url+"="+word 
    content = requests.get(url_req).content
    soup = BeautifulSoup(content,'html.parser')

    def rhyme_maker(soup): # 
    
        rhyme = soup.find_all("span" , {"class" : "result"}) # kafiyeli sözcükler html içinden çekiliyor, burada site üzerinde ögeyi denetle yaparak gerekli kısmı daha kolay bulabiliriz
    
        return rhyme

    kafiye = rhyme_maker(soup)

    take_them = kafiye[0:count+1]
    i = 0
    for a in take_them:
        print(i,"- ",end="") #çıktının okunaklı olması için numaralandırma yapıyoruz
        print(a.text.replace(",","")) # azrhymes sözcükleri virgül kullanarak ayırdığı için çıktıda bunu silmemiz gerekiyor
        i = i+1



def English():
    url = "https://azrhymes.com/?rhymes" #kafiyeli kelimeleri oluşturan site
    word = input("Write a word to rhyme :  ")
    count = int(input("How many words do you want :  ")) 
    url_req = url+"="+word 
    content = requests.get(url_req).content
    soup = BeautifulSoup(content,'html.parser')

    def rhyme_maker(soup): # 
        
        rhyme = soup.find_all("span" , {"class" : "result"}) # kafiyeli sözcükler html içinden çekiliyor, burada site üzerinde ögeyi denetle yaparak gerekli kısmı daha kolay bulabiliriz
        
        return rhyme

    kafiye = rhyme_maker(soup)

    take_them = kafiye[0:count+1]
    i = 0
    for a in take_them:
        print(i,"- ",end="") #çıktının okunaklı olması için numaralandırma yapıyoruz
        print(a.text.replace(",","")) # azrhymes sözcükleri virgül kullanarak ayırdığı için çıktıda bunu silmemiz gerekiyor
        i = i+1



Login()