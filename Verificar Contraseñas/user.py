#Usuario
def nickname(user):
 long = len(user)
 k = user.isalnum()

 if k == False:
  print ("El nombre de usuario solo puede contener letras y numeros")

 if long > 16:
  print ("El nombre de usuario no puede contener mas de 16 caracteres")

 if long < 8:
  print ("El nombre de usuario no puede contener menos de 8 caracteres")

 if long > 7 and long < 17 and k == True:
  return True
