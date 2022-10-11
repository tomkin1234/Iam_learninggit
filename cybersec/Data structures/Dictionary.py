
print('hej, to program, który zbiera ile harcerze mają sprawości. domyślna ustawiona liczba harcerzy to 6 osób w zastępie.')
sprawności = {}

for i in range(6):
    imię = input("wprowadź imię harcerza: ")
    ilość = input("wprowadź, ile/jakie sprawności ma harcerz: ")

    sprawności[imię] = ilość


print(sprawności)