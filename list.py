countries = ['United Kingdom', 'Ghana', 'Nigeria', 'Australia', 'New Zealand']
print(countries)
print(countries[:])
print(countries[0])
print(countries[0:-1])
print(countries[2][0])
print(type(countries), len(countries))

# Changing element in a list

countries[0] = 'United State'
print(countries)
countries[3] = 'Canada'
print(countries)

# Getting only the end of the lists
print(countries[-1])
print(countries[-2])
print(countries[-3])
print(countries[-4])
print(countries[-5])


mixed = ['United Kingdom', 'Ghana', 2, True, 'New Zealand']
print(type(mixed), mixed)
print(type(mixed[2]), type(mixed[3]), type(mixed[0]), mixed)


# Other way of making a list
sports = list(('Football', 'Basketball', 'Volleyball', 34))
print(type(sports), sports)