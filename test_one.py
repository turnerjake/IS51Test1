"""
EXAM END
"""

def option1():
    daily_pay = 100
    work_days = 10
    total_pay = daily_pay * work_days
    return total_pay
def option2():
    day_specific_pay = 1
    work_days = 9
    day_counter = 0
    total_pay = 1
    while day_counter < work_days:
        day_counter += 1
        day_specific_pay = 2**day_counter
        total_pay += day_specific_pay
    return total_pay
def main():
    option1_pay = option1()
    option2_pay = option2()
    print(("Option 1 pays: ${0:.2f}").format(option1_pay))
    print(("Option 2 pays: ${0:.2f}").format(option2_pay))
    if option1_pay > option2_pay:
        print("Option 1 is better.")
    elif option1_pay < option2_pay:
        print("Option 2 is better.")
    else:
        print("Option 1 and Option 2 pay the same ")

main()