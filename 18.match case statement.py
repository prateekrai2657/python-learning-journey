# Match case statement  = An alternative to using many elif statements 
# execute some code if a value matches a 'case'
# benifits:cleaner and syntax is more readable

def day_of_week(day):
    match day:
        case 1:
            return "It is sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Wednesday"
        case 4:
            return "It is Thrusday"
        case 5:
            return "It is Friday"
        case 6:
            return "It is Saturday"
        case _:
            return "Not a valid date"
print(day_of_week(3))
         