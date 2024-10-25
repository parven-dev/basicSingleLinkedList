
def  cal_avg_temp(user_input: int):
    
    temp_data = []
    if user_input > 1:
        for  user_data in range(1, user_input+ 1):
            days_input = int(input(f"Day {user_data}'s high temp: "))
            temp_data.append(days_input)
    
    average = sum(temp_data) / user_data
    for item in range(1, len(temp_data) +1):
        if temp_data[item] > average:
            print("Average = ", average)
            return f"{item} day(s) above average"
            

user_input = int(input("How many day's temperature? "))
print(cal_avg_temp(user_input))