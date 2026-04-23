import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

# if __name__ =="__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

    # small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20

def selection_sort(cisla_seznam):
    seznamicik = cisla_seznam.copy()
    cisilka = len(seznamicik)
    for i in range(cisilka):
        index_nejmensi = i
        for j in range(i + 1, cisilka):
            if seznamicik[j] < seznamicik[index_nejmensi]:
                index_nejmensi = j
        seznamicik[i], seznamicik[index_nejmensi] = seznamicik[index_nejmensi], seznamicik[i]
    return seznamicik

#     novy_seznam = cisla_seznam.copy()
#     novy_seznam.sort()
#     return novy_seznam
#
if __name__ =="__main__":
    kratky = [5, 1, 4, 2, 8]
    print(kratky)
    print(f"{selection_sort(kratky)}")
    puvodni = (selection_sort(random_numbers(20)))
    print(f"{selection_sort(puvodni)}")
    # values = random_numbers(20)  #
    # serazena = selection_sort(values)
    # print(serazena)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]