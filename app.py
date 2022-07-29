from pyshorteners import Shortener

s = Shortener()
choice = int(input("1 か 2 を入力してください (短縮化: 1, 元に戻す: 2) ---> "))

def short():
    link = input("短縮化したいURLを入力してください ---> ")
    short_link = s.tinyurl.short(link)
    print("短縮化したURL ---> " + short_link)

def expand():
    link = input("元に戻したいURLを入力してください ---> ")
    exp_link = s.tinyurl.expand(link)
    print("元のURL ---> " + exp_link)

if choice == 1:
    short()
elif choice == 2:
    expand()
else:
    print("1 か 2 を入力してください")