from typing import List
from repository.interfaces.bingo_repository_interface import BingoRepositoryInterface


class BingoReposository(BingoRepositoryInterface):
    def __init__(self):
        ...

    def insert_card(self, card: list) -> None:
        ...

    def get_all_cards(self) -> List[list] | List:
        ...
    
    def insert_drawn_number(self, number: int) -> None:
        ...
    
    def get_drawn_numbers(self) -> list[int] | List:
        ...


class BingoInMemoryReposository(BingoRepositoryInterface):
    def __init__(self):
        self.__drawn_numbers = []
        self.__cards_list = []

    def insert_card(self, card: list) -> None:
        self.__cards_list.append(card)

    def get_all_cards(self) -> List[list] | List:
        return self.__cards_list
    
    def insert_drawn_number(self, number: int) -> None:
        return self.__drawn_numbers.append(number)

    def get_drawn_numbers(self) -> list[int] | List:
        return self.__drawn_numbers