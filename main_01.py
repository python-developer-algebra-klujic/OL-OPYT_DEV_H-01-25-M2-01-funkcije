

# Deklaracija funkcije welcome
# kljucna rijec def, yatimnayiv funkcije koji mi odredujemo
# te argumenti u obicnim zagradama i nakon toga : i tijelo funkcije
def welcome(first_name: str, last_name: str = '') -> None:
    '''
    Funkcija welcome ocekuje agrumente first_name i last_name za ime i prezime osobe
    za koju ce ispisati pozdravnu poruku
    '''

    if last_name != '':
        print()
        print(f'Pozdrav, {first_name} {last_name}!')
        print()
    else:
        print()
        print(f'Pozdrav, {first_name}!')
        print()



def simple_calculator(a: int, b: int, math_operation: str = '+'):
    '''
    Funkcija koja prima dva cijela broja kao argumente: a i b
    te simbol racunske operacije i vraca rezultat matematicke operacije ta dva broja
    Predefinirana operacija je zbrajanje
    '''
    match math_operation:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            if b != 0:
                return a / b
            else:
                return 0
        case '%':
            if b != 0:
                return a % b
            else:
                return 0































# "Poziv funkcije", odnosno pokretanje funkcije welcome()
welcome(last_name='Ivic', first_name='Iva')

welcome('Pero')

a = 3
b = 0

calc_result = simple_calculator(a, b)
print('Default', calc_result)

calc_result = simple_calculator(a, b, '+')
print('+', calc_result)

calc_result = simple_calculator(a, b, '-')
print('-', calc_result)

calc_result = simple_calculator(a, b, '*')
print('*', calc_result)

calc_result = simple_calculator(a, b, '/')
print('/', calc_result)

calc_result = simple_calculator(a, b, '%')
print('%', calc_result)
