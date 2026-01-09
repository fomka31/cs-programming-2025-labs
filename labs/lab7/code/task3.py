personnel = [
    {"name": "Dr. Klein", "clearance": 2},
    {"name": "Agent Brooks", "clearance": 4},
    {"name": "Technician Reed", "clearance": 1}
]

clearances = {
    1 : "Restricted",
    2 : "Confidential",
    3 : "Confidential",
    4 : "Top Secret"
}

lst = [*map(lambda x: clearances.get(x['clearance']), personnel)]
for i in range(len(lst)):
    personnel[i]['clearance'] = lst[i]