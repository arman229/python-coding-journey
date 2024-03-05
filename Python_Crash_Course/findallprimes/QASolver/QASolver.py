class BookSolutions:
    def __init__(self):
        from questions import questions
        from solutions import solutions
        self.questions = questions
        self.solutions = solutions

    def find_solution(self, query):
        query_lower = query.lower()
        matching_solutions = []
        for key, value in self.questions.items():
            if query_lower in value.lower() or query_lower == key:
                matching_solutions.append((key, value, self.solutions[key]))
        return matching_solutions if matching_solutions else "Solution not found"

book_solutions = BookSolutions()
query = input("Enter the query: ")
solution = book_solutions.find_solution(query)
if solution == "Solution not found":
    print(solution)
else:
    for key, question, value in solution:
        print(f"Question: {key}\nComplete Question: {question}\nSolution:\n{value}\n")
