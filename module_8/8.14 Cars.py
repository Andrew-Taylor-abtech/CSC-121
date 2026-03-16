def make_car(make, model, year, color='white', **car_misc):
    car = {'make': make, 
           'model': model, 
           'year': year, 
           'color': color}
    car.update(car_misc)
    return car

my_car = make_car('Ford', 
                  'F-150', 
                  '2020',
                  type='truck')
print(my_car)
my_van = make_car('Freightliner', 
                  'Sprinter', 
                  '2014', 
                   type='van',
                   name='Bubbles')
print(my_van)
