import re

sw=0
while sw==0:
  texto = input("Introduce la secuencia h validar:\n")
  patron = "[A-Z]{3}[0-9]{3}"

  if len(texto) == 6:
    z = re.findall(patron, texto) 
   
    if len(z)== 0:
      print ("No se acepta\n") 
    else:
      print ("Se acepta\n")   
  else:
    print ("No se acepta\n") 

  ent =int(input("Desea seguir validando secuencias? 0=Si ; 1=No :\n"))
  if ent==1:
    sw=1
    print ("BYE BYE\n") 
  if ent==0:
    sw=0


