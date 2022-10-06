def cube(num):
    cubes = {}
    for i in range(1,num+1):
        cubes[i] = i*i*i
    return cubes
print(cube(7))