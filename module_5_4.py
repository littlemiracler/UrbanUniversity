# В задании опечатка в слове Bui(l)ding для класса, позволила себе исправить :)
class Building:
    total = 0
    def __init__(self):
        Building.total += 1

for k in range(40):
    building_following = Building()
    print(k + 1)

print('Всего объектов:')
print(Building.total)
