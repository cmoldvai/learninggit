cities = ['Novi Sad', 'Kitchener', 'Dublin']
states = ['Vojvodina', 'Ontario', 'California']
countries = ['Serbia', 'Canada', 'USA']

# [print(f'{city}, {state}, {country}') for city,state, country in zip(cities, states, countries)]

# for city,state,country in zip(cities, states, countries):
#     print(f'{city}, {state}, {country}')

for Tuple in zip(cities, states, countries):
    print(Tuple)
    # print(f'{city}, {state}, {country}')
print(type(Tuple))