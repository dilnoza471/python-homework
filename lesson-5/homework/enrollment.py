universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def enrollment_stats(a : [[]]):
    total_students = [] #list for students
    total_tuition = []#lists for tuition fees
    for x in a:
        total_students.append(x[1])
        total_tuition.append(x[2])
    return total_students, total_tuition
def mean(a:list):
    return sum(a) / len(a) #avg = sum /n
def median(a:list):
    sorted_a = sorted(a)
    if len(sorted_a) % 2 == 1: #when there's odd number of elements
        return sorted_a[len(sorted_a) // 2]
    return (sorted_a[len(sorted_a) // 2] + sorted_a[len(sorted_a) // 2 - 1])/2#when even

if __name__ == '__main__':
    students, tuition = enrollment_stats(universities)
    print(f"Total students: {sum(students):,}")
    print(f"Total tuition: $ {sum(tuition):,}")
    print()
    print(f"Student mean: {mean(students):,.2f}") #format to include commas and 2 dec place
    print(f"Student median: {median(students):,}")
    print()
    print(f"Tuition mean: ${mean(tuition):,.2f}")
    print(f"Tuition median: ${median(tuition):,}")