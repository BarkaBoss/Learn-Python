import math


area_square = lambda a:  math.pow(a, 2)
area_rectangle = lambda l, b: l * b
area_triangle = lambda b, h: 0.5 * b * h
area_trapezoid = lambda b1, b2, h: 0.5 * (b1 + b2) * h
area_circle = lambda r: math.pi * math.pow(r, 2)
circum_circle = lambda r: 2 * math.pi * r
surface_area_cube = lambda a: 6 * math.pow(a, 2)
curve_surface_area_cylin = lambda r, h: 2 * math.pi * r * h
total_surface_area_cylin = lambda r, h: 2 * math.pi * r * (r + h)
volume_cylin = lambda r, h: math.pi * math.pow(r, 2) * h
acceleration = lambda v, u, t: (v - u) / t
density = lambda m, v: m / v
pressure = lambda f, a: f / a
kinetic_energy = lambda m, v: 0.5 * m * math.pow(v, 2)
voltage = lambda i, r: i * r

operations = {
    'area_square': area_square,
    'area_rectangle': area_rectangle,
    'area_triangle': area_triangle,
    'area_trapezoid': area_trapezoid,
    'area_circle': area_circle,
    'circum_circle': circum_circle,
    'surface_area_cube': surface_area_cube,
    'curve_surface_area_cylin': curve_surface_area_cylin,
    'total_surface_area_cylin': total_surface_area_cylin,
    'volume_cylin': volume_cylin,
    'acceleration': acceleration,
    'density': density,
    'pressure': pressure,
    'kinetic_energy': kinetic_energy,
    'voltage': voltage
}

set_parameters = lambda params: list(map(float, params.split(',')))

operations_format = ['area_square: a', 'area_rectangle: l, b', 'area_triangle: b, h', 'area_trapezoid: b1, b2, h',
                     'area_circle: r', 'circum_circle: r', 'surface_area_cube: a', 'curve_surface_area_cylin: r, h',
                     'total_surface_area_cylin: r, h', 'volume_cylin: r, h', 'acceleration: v, u, t', 'density: m, v',
                     'pressure: f, a', 'kinetic_energy: m, v', 'voltage: i, r']

print('all available operations are:\n')
print(*list(operations_format), sep='\n', end='\n\n')

print('usage: <operation_name> <parameter(s)>')
print('example: area_rectangle 5,10\n')

action = input("Enter operation:\n").split(' ')

operation, parameter = action[0], set_parameters(action[1])

print(operations[operation](*parameter))
