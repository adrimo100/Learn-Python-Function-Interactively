# Your code goes here:
def render_person(name, born_date, eyes_color, age, gender):
    return "%s is a %s years old %s born in %s with %s eyes" % (name, age, gender,born_date, eyes_color)


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))