import numpy as np
from random import randint
import math

rus_alp = "а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я".split()

###############################################   GRID   #########################################################

def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


def sorted_matrix(a, N, M):
    k = M-1
    while k > 0:
        ind = 0
        for j in range(k+1):
            if a[N-1][j] > a[N-1][ind]:
                ind = j
        for i in range(N):
            m = a[i][ind]
            a[i][ind] = a[i][k]
            a[i][k] = m
        k -= 1

    return a


def encrypt_with_grid(k):
    encrypted = np.zeros((2*k, 2*k))

    for _ in range(4):
        for i in range(k):
            for j in range(k):
                encrypted[i][j] = i * k + j + 1

        encrypted = np.rot90(encrypted)
        print(encrypted)
        print()
    uniq = [num for num in range(1, k**2+1)]
    indexes = []
    while len(uniq) > 0:
        for i, lst in enumerate(encrypted):
            if len(uniq) == 0:
                break
            index = np.where(lst == uniq[0])
            index = index[0]
            if len(index) == 1:
                indexes.append((i, index[0]))
                uniq.pop(0)
            elif len(index) > 1:
                prob = randint(0, 1)
                if prob == 1:
                    indexes.append((i, index[-1]))
                else:
                    indexes.append((i, index[0]))
                uniq.pop(0)
    print("indexes: ", indexes)
    print()
    encrypted_matrix = np.chararray((k * 2, k * 2), unicode=True)
    ind_text = 0
    for _ in range(k*2):
        for ind in indexes:
            encrypted_matrix[ind[0]][ind[1]] = text[ind_text]
            ind_text += 1
        encrypted_matrix = np.rot90(encrypted_matrix)
        print(encrypted_matrix)
        print()

    order_passw = []
    for letter in password:
        order_passw.append(rus_alp.index(letter))
    matrix = [np.ndarray.tolist(row) for row in encrypted_matrix]
    matrix.append(order_passw)
    print_matrix(matrix)
    sorted_matrix(matrix, len(matrix), len(matrix[0]))
    print_matrix(matrix)
    shifr = ""
    for i in range(len(matrix) - 1):
        for j in range(len(matrix) - 1):
            shifr += matrix[j][i]

    print("encrypted message: ", shifr)


def encrypt(text, password):
    k = int(len(text)**0.25)
    if k**4 != len(text):
        raise ValueError("Length of the text should be a perfect square.")

    if len(password) != k**2:
        raise ValueError(f"Length of the password should be {k}.")

    encrypt_with_grid(2)


text = "договор подписали".replace(" ", "")
password = "шифр"
# encrypt(text, password)


##################################################   ROUTE   ###########################################################
text_2 = "нельзя недооценивать противника".replace(" ", "")
password_2 = "пароль"


def fill_matrix(text, num_cols):
    num_rows = math.ceil(int(len(text)) / int(num_cols))
    matrix = []
    for i in range(num_rows):
        matrix.append([letter for letter in text_2[num_cols * i:num_cols * (i + 1)]])

    while len(matrix[-1]) != num_cols:
        matrix[-1].append("a")

    return matrix


def encrypt_route(text, num_cols):
    matrix = fill_matrix(text, num_cols)
    print_matrix(matrix)
    matrix.append([letter for letter in password_2])
    print_matrix(matrix)
    sorted_matrix(matrix, len(matrix), len(matrix[0]))
    print_matrix(matrix)
    shifr = ""

    for i in range(len(matrix)):
        for j in range(len(matrix) - 1):
            shifr += matrix[j][i]

    print("encrypted message: ", shifr)

# encrypt_route(text_2, 6)


#########################################################   VIZHENERA   ################################################
alph = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
def vigenere_encrypt(text, key):
    encrypted_text = ''

    # размерность пароля = размерности текста
    key_expanded = ''
    while len(key_expanded) < len(text):
        key_expanded += key
    key_expanded = key_expanded[:len(text)]

    alph_matrix = create_alf(alph)

    # сравниваем по таблице и получаем на пересечении букву
    for t, k in zip(text, key_expanded):
        encrypted_text += alph_matrix[alph.index(k)][alph.index(t)]

    return encrypted_text


def create_alf(alph):
    alph_matrix = []
    for i in range(len(alph)):
        new_row = alph[i:] + alph[:i]
        alph_matrix.append([letter for letter in new_row])

    return alph_matrix

text_3 = "криптография серьезная наука".replace(" ", "")
password_3 = "математика"
encrypted_text = vigenere_encrypt(text_3, password_3)
print(encrypted_text)
