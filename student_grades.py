from email.quoprimime import body_check
from sorting import random_numbers

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)


    def get_grade(self, index):
        body =self.scores[index]
        if body >= 90:
            return "A"
        elif body >= 80:
            return "B"
        elif body >= 70:
            return "C"
        elif body >= 60:
            return "D"
        elif body >= 50:
            return "E"
        else:
            return "F"

    def find(self, hledane_body):
        index = []
        for i in range(len(self.scores)):
            if self.scores[i] == hledane_body:
                index.append(i)
        return index

    def get_sorted(self):
        seznam = self.scores.copy()
        cisilka = len(seznam)
        for i in range(cisilka):
            for j in range(0, cisilka - i - 1):
                if seznam[j] > seznam[j+1]:
                    seznam[j], seznam[j+1] = seznam[j+1], seznam[j]
        return seznam

def main():
    body_list = [85, 42, 91, 67, 50, 73, 100, 38, 58]
    results = StudentsGrades(body_list)
    print(f"Pocet studentu, co psali test: {results.count()}")
    for i in range(results.count()):
        body = results.scores[i]
        znamka = results.get_grade(i)
        print(f"Student {i}: {body} points – {znamka}")
    plny_pocet = results.get_sorted()
    print(f"indexy studentu s 100 body: {plny_pocet}")

    serazena = results.get_sorted()
    print(f"serazene vysledky: {serazena}")

if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    # print(results.count())          # 9
    # print(results.get_by_index(2))  # 91
    # print(results.scores)# [85, 42, 91, 67, 50, 73, 100, 38, 58]
    # print(results.get_grade(2))  # A (91 bodů)
    # print(results.get_grade(6))  # A (100 bodů)
    # print(results.get_grade(7))  # F (38 bodů)
    # print(results.find(100))  # [6]
    # print(results.find(50))  # [4]
    # print(results.find(77))  # []
    # print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    # print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny
    # random_results = StudentsGrades(random_numbers(30, 0, 100))
    # print(random_results.count())
    # print(random_results.get_sorted())
    main()