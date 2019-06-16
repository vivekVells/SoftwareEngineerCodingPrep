"""
A -> Person List | B -> Target Floor
M -> total Floors
X -> max ppl | Y -> max weight

select X people whose weight <= Y
floor target matters. it is the one that helps to get stop count value

"""


def person_select_based_on_allowed_weight(person, max_ppl_per_ride, max_weight_per_ride):
    selected_ppl = []
    rider_weight = 0

    i = 0
    while i < max_ppl_per_ride:
        i += 1

        for item_index in range(len(person)):
            if item_index < max_ppl_per_ride:
                rider_weight += person[item_index]
                if rider_weight <= max_weight_per_ride:
                    selected_ppl.append(person[item_index])


    print("se ", person, selected_ppl)


def solution(person, target_floor, total_floor, max_ppl_per_ride, max_weight_per_ride):
    person_select_based_on_allowed_weight(person, max_ppl_per_ride, max_weight_per_ride)


    print(person)
    return person


A = [60, 80, 40]
B = [2, 3, 5]
X = 2
Y = 200
M = 5
print(solution(A, B, M, X, Y))


"""

def solution(A, B, M, X, Y):
    currentPerson = 0
    totalPersonCount = len(A)
    destinationFloors = []
    totalWeightTwoPersons = 0
    maxPersonCount = 0
    totalTrips = 0
    startElevator = False

    while currentPerson < totalPersonCount:
        if maxPersonCount + 1 <= X and totalWeightTwoPersons + A[currentPerson] <= Y:
            destinationFloors.append(B[currentPerson])
            totalWeightTwoPersons += A[currentPerson]
        if currentPerson == totalPersonCount - 1:
            startElevator = True
            maxPersonCount += 1
            currentPerson += 1
        else:
            startElevator = True
        if startElevator:
            if len(destinationFloors) == 2 and destinationFloors[0] == destinationFloors[1]:
                totalTrips += 1
                destinationFloors[: ] = []
        else:
            totalTrips += len(destinationFloors)
            destinationFloors[: ] = []
            startElevator = False
            maxPersonCount = 0
            totalWeightTwoPersons = 0
        if len(destinationFloors) == 0:
            totalTrips += 1

    return totalTrips

A = [60, 80, 40]
B = [2, 3, 5]
X = 2
Y = 200
M = 5
print(solution(A, B, M, X, Y))
"""