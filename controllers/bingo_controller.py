import random
from typing import Union, List

class Bingo:
    def __init__(self):
        self.__drawn_numbers = []

    def get_bingo(self):
        return {"Hello": "World"}
    
    def __get_numbers(self, start: int, end: int) -> List[int]:
        numbers_list = []
        while True:
            number = random.randint(start, end)
            if number not in numbers_list: numbers_list.append(number)
            if len(numbers_list) == 5: break
        return sorted(numbers_list)

    def get_card(self) -> List[list]:
        card = [
            self.__get_numbers(1, 15),
            self.__get_numbers(16, 30),
            self.__get_numbers(31, 45),
            self.__get_numbers(46, 60),
            self.__get_numbers(61, 75)
        ]
        return card
    
    def get_drawn_numbers(self, start: int = 1, end: int = 75) -> int:
        if len(self.__drawn_numbers) >= end:
            return 0
        number = random.randint(start, end)
        if number in self.__drawn_numbers:
            return self.get_drawn_numbers(start, end)
        self.__drawn_numbers.append(number)
        return number
    
    def get_drawn_numbers_list_and_percentage(self, total_bingo_numbers: int = 75) -> List[int]:
        percentage = (len(self.__drawn_numbers)/total_bingo_numbers) * 100
        return self.__drawn_numbers, round(percentage, 2)


if __name__ == "__main__":
    instance = Bingo()
    print(instance.get_card())