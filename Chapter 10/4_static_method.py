class company:
    name = 'Google'
    CEO = 'Sundar Pichai'
    salary = '1.2 Billion'
    product = 'Gemini'

    @staticmethod # we use it when a function dosen't use argument / no need of object.
    def greet():
        print('Good morning.')

a = company()
a.greet() # equivalent to company.greet(a)

print(f'{a.name}\n{a.salary}\n{a.product}')

