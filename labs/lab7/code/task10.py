evaluations = [
    {"name": "Agent Cole", "score": 78},
    {"name": "Dr. Weiss", "score": 92},
    {"name": "Technician Moore", "score": 61},
    {"name": "Researcher Lin", "score": 88}
]

best_chel = max(evaluations, key=lambda x: x['score'])
print(f'Сотрудник {best_chel['name']} имеет высший балл равный {best_chel['score']}')