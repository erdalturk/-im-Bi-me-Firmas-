#Merhaba
#Bu proje bir kişinin çim biçme işlemi için
#firmaya ödeyeceği fiyatı hesaplar.

customer_name = input("Please enter your name.")
print(f"{customer_name}, welcome!")

small = 50
medium = 75
large = 100
print(f"Weekly price list: \n Small area: {small} \n Mediuam area: {medium} \n Large area: {large} ")
#Burada  standart fiyat hesaplama listemizi gösterdik.

while True:
    try:
        area_length = int(input("Enter length: "))
        area_width = int(input("Enter width: "))
        if area_length <= 0 or area_width <= 0:
            print("Error: Length and width must be greater than zero.")
        else:
            break
    except ValueError:
        print("Error: Please enter numeric values only.")
#Burada kullanıcıdan arazi ölçülerini istedik ve
#hatalı bir giriş(sayısal olmayan vey sıfırdan küçük)
#yaptığında tekrar giriş yapabilmesini sağladık.

area_size = area_length * area_width
weekly_season_length = 20
#Burada alan hesabını yaptık ve çim biçme sezonunun uzunluğunu(haftalık) tanımladık.

if 0 < area_size < 400:
    weekly_price = area_size * small
elif 400 <= area_size < 600:
    weekly_price = area_size * medium
else:
    weekly_price = area_size * large
#Burada alan büyüklüğüne göre haftalık fiyatı hesapladık.

seasonal_price = weekly_price * weekly_season_length
print(f"Weekly price: {weekly_price} \nSeasonal price: {seasonal_price}")
#Burada haftalık fiyata göre sezonluk fiyatı hesapladık.
#Ve hem haftalık hem de sezonluk fiyatı müşteriye sunduk.