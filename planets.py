def weight_on_planets():
   # write your code here
   earth_weight = int(input('What do you weigh on earth? '))
   # earth_weight = 136
   output = f'\nOn Mars you would weigh {earth_weight * .38} pounds.\nOn Jupiter you would weigh {earth_weight*2.34} pounds.'
   
   print(output)

   return output
   
if __name__ == '__main__':
   weight_on_planets()