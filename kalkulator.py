def user_input():
    num_one = int(input("Masukkan bilangan pertama: "))
    num_two = int(input("Masukkan bilangan kedua: "))
    return num_one, num_two
        

def kalkulator_opr(num1, num2, opr):
    if opr == '+': res = num1 + num2
    elif opr == '-': res = num1 - num2
    elif opr == '*': res = num1 * num2
    elif opr == '/': res = num1 / num2
    elif opr == '%': res = num1 % num2
    else: res = num1 ** num2
    return res

def kalkulator_main():
    while True:
        print("====================================")
        print("=== Program Kalkulator Sederhana ===")
        print("====================================")

        try:
            num_one, num_two = user_input()
        except ValueError:
            print("====================================")
            print("Mohon maaf! Invalid input! Silahkan coba lagi!!")
            print("====================================")
            continue
        
        print("====================================")
        print("Pilih operasi matematika: ")
        print("1. Penambahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Sisa Bagi")
        print("6. Pangkat")
        print("====================================")
        try:
            choice = int(input("Pilihan Anda (1/2/3/4/5/6): "))
            print("====================================")
            if 1 <= choice <= 6:
                if choice == 1: operator = '+'
                elif choice == 2: operator = '-'
                elif choice == 3: operator = '*'
                elif choice == 4: operator = '/'
                elif choice == 5: operator = '%'
                else: operator = '**'
                print(f"Hasil: {num_one} {operator} {num_two} ==> {kalkulator_opr(num_one, num_two, operator)}")
                print("====================================")
            else:
                print("Mohon maaf! Menu tidak tersedia, Silahkan coba lagi!!")
                print("====================================")
        except ValueError: 
            print("====================================")
            print("Mohon maaf! Invalid input! Silahkan coba lagi!!")
            print("====================================")
            

        try_again = input("Coba lagi? (ya/tidak): ")
        if try_again.lower() == 'ya': continue
        else: 
            print("Terima Kasih :)")
            print("====================================")
            break

kalkulator_main()