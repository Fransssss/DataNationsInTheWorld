#import request and use get to get data from a specified url
import requests     # to use get
print("\nThe Database has information about countries around the world")
print("   == Database Menu ==")
print("1. All Database")
print("2. Name of a country and its information")
print("3. Currency of countries")
print("4. Language of a country")
print("5. Capital of a country")
print("E. Exit")
choice = input("choice: ")
base_url = "https://restcountries.com/v3.1/"   # search will be based on this url

while choice != 'E' and choice != 'e':
    if choice == '1':
        print('\n')
        rp = requests.get(base_url + "all")
        print(rp.text)
    elif choice == '2':
        country = input("\nName of a country: ")
        rp = requests.get(base_url + "name/" + country)
        print("Information about \'" + country + "\': \n")
        print(rp.text)
    elif choice == '3':
        currency = input("\nName of currency: ")
        rp = requests.get(base_url + "currency/" + currency)
        print("Country/ies that use \'" + currency + "\' as its currency: \n")
        print(rp.text)
    elif choice == '4':
        language = input("\nName of a language: ")
        rp = requests.get(base_url + "lang/" + language)
        print("Country/ies that speak \'" + language + "\': \n")
        print(rp.text)
    elif choice == '5':
        capital = input("\nName of a capital: ")
        rp = requests.get(base_url + "capital/" + capital)
        print(rp.text)
    else:
        print("[Invalid input]")

    print("\n   == Database Menu ==")
    print("1. All Database")
    print("2. Name of a country and its information")
    print("3. Currency of countries")
    print("4. Language of a country")
    print("5. Capital of a country")
    print("E. Exit")
    choice = input("choice: ")
    base_url = "https://restcountries.com/v3.1/"

