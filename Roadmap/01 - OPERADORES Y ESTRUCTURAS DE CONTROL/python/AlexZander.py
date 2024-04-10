# Operadores aritmeticos

print("Operadores aritmeticos")
suma           = 1 + 1
resta          = 2 - 1
multiplicacion = 2 * 2
division       = 2 / 2
modulo         = 2 % 2
exponente      = 2 ** 2
cociente       = 10 // 2

print(suma)
print(resta)
print(multiplicacion)
print(division)
print(modulo)
print(exponente)
print(cociente)

# Operadores logicos

print("Operadores logicos")
print(True and True) # and
print(True or False) # or
print(not True)      # not

# Operadores de comparacion

print("Operadores de comparación") 
print(2 == 2) 
print(2 != 2)
print(2 > 2)
print(2 < 2)
print(2 >= 2)

# Operadores de asignación

a=7; b=2
print("Operadores de asignación")
x=a; x+=b;  print("x+=", x)  # 9
x=a; x-=b;  print("x-=", x)  # 5
x=a; x*=b;  print("x*=", x)  # 14
x=a; x/=b;  print("x/=", x)  # 3.5
x=a; x%=b;  print("x%=", x)  # 1
x=a; x//=b; print("x//=", x) # 3
x=a; x**=b; print("x**=", x) # 49
x=a; x&=b;  print("x&=", x)  # 2
x=a; x|=b;  print("x|=", x)  # 7
x=a; x^=b; print("x^=", x)   # 5
x=a; x>>=b; print("x>>=", x) # 1
x=a; x<<=b; print("x<<=", x) # 28

# Operadores de identidad

print("Operadores de identidad")
a = 10
b = 12

print(a is b) # False
print(a is not b) # True

# Operadores de pertenencia

print("Operadores de pertenencia")
b = [1,2,3]

print(2 in b)     # True
print(4 not in b) # True

# operadores de bits

a = 5
b = 3
and_bits = a & b
or_bits = a | b
not_bits = ~a
xor_bits = a ^ b
desplazamiento_derecha = a >> b
desplazamiento_izquierda = a << b

print(and_bits)                 # 1
print(or_bits)                  # 7
print(not_bits)                 # -6
print(xor_bits)                 # 6
print(desplazamiento_derecha)   # 0
print(desplazamiento_izquierda) # 40


# Condicionales
# if 
edad = 20

if edad <= 18:
    print("Eres mayor de edad")
# elif
elif edad > 18:
    print("eres menor de edad")
# else
else:
    print("Eres un robot")
    
    
# Iterativas
# For

nombres = {"Alexander", "Manuel", "Jonathan"}

for nombre in nombres:
    print(f"El nombre es {nombre}")

# While    
i = 1

while i <= 5:
    print(f"El valor de i es {i}")
    i += 1

# Excepciones

n1 = 6
n2 = 2

try:
    print(n1 + n2)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: # opcional
    # Se ejecuta si no se produce excepcion
    print("La ejecucion continua correctamente")
finally: # Opcional
    # Se ejecuta siempre
    print("La ejecucion continua")            
    
    
# Reto extra

for i in range(10, 56):
    if i != 16:
        if i % 2 == 0 and i % 3 != 0:
            print(i)
    if i == 55:
        print(i)



    
  
            