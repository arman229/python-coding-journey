from typing import List 
from qasolver.questions import questions
from qasolver.solutions import solutions

class BookSolutions:
    def __init__(self):
        self.questions = questions
        self.solutions = solutions

    def find_solution(self, query: str) -> List[tuple[str, str, str]] | str|None:
        query_lower = query.lower().strip()
        matching_solutions: List[tuple[str, str, str]] = []
        for key, value in self.questions.items():
            if len(query_lower) > 10 and query_lower in value.lower():
                matching_solutions.append((key, value, self.solutions[key]))
            elif query_lower == key:
                matching_solutions.append((key, value, self.solutions[key]))

        if matching_solutions:
            for key, question, value in matching_solutions:
                print(f"# {key} {question} \n# Solution:\n{value}\n")
        return "Solution not found" if not matching_solutions else None

book_solutions = BookSolutions()
 

 
 
 
 