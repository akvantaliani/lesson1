#tasks for lists
print("#tasks for lists:")
number_list = [3, 5, 7, 9 , 10.5]

print(number_list)

number_list.append("Python")

number_list_len = len(number_list)
print(number_list_len)

print(number_list[0])

print(number_list[-1])

print(number_list[1:4])

number_list.remove("Python")

print(number_list)
print()
#tasks for dictionaries
print("#tasks for dictionaries:")
weather = {"city": "Москва", "temperature": "20"}

print(weather["city"])

weather["temperature"] = int(weather["temperature"]) - 5

print(weather)

print(weather.get("country"))

print(weather.get("country", "Россия"))

weather["date"] = "27.05.2019"

weather_len = len(weather)

print(weather_len)
