from typing import List 
from questions import questions
from solutions import solutions

class BookSolutions:
    def __init__(self):
        self.questions = questions
        self.solutions = solutions

    def find_solution(self, query: str) -> List[tuple[str, str, str]] | str|None:
        query_lower = query.lower()
        matching_solutions: List[tuple[str, str, str]] = []
        for key, value in self.questions.items():
            if len(query_lower) > 10 and query_lower in value.lower():
                matching_solutions.append((key, value, self.solutions[key]))
            elif query_lower == key:
                matching_solutions.append((key, value, self.solutions[key]))

        if matching_solutions:
            for key, question, value in matching_solutions:
                print(f"Question: {key} {question} \nSolution:\n{value}\n")
        return "Solution not found" if not matching_solutions else None

book_solutions = BookSolutions()
book_solutions.find_solution('')
