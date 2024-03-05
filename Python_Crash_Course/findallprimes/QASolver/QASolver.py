from typing import List 
from questions import questions
from solutions import solutions

class BookSolutions:
    def __init__(self):
        self.questions  = questions
        self.solutions  = solutions

    def find_solution(self, query: str) -> List[tuple[str, str, str]]|str:
        query_lower = query.lower()
        matching_solutions: List[tuple[str, str, str]] = []
        for key, value in self.questions.items():
            if len(query_lower) > 10 and query_lower in value.lower():
                matching_solutions.append((key, value, self.solutions[key]))
            elif query_lower == key:
                matching_solutions.append((key, value, self.solutions[key]))
        return matching_solutions if matching_solutions else "Solution not found"

book_solutions = BookSolutions()
query = input("Enter the query: ")
solution = book_solutions.find_solution(query)
if isinstance(solution, list):
    for key, question, value in solution:
        print(f"\033[1;1mQuestion: {key}\033[0m\n\033[1mComplete Question:\033[0m {question}\n\033[1mSolution:\033[0m\n{value}\n")
 
else:
    print(solution)
