#Password
def contra(password):
 validar=False 
 long=len(password) 
 espacio=False  
 mayuscula=False 
 minuscula=False 
 numeros=False 
 y=password.isalnum()
 correcto=True 
        
 for cc in password: 

   if cc.isspace()==True: 
    espacio=True 

   if cc.isupper()== True:
    mayuscula=True
                
   if cc.islower()== True: 
    minuscula=True 
                 
   if cc.isdigit()== True: 
    numeros=True 
                            
 if espacio==True: 
  print("La contraseña no puede contener espacios")
 else:
  validar=True
                       
 if long <8 and validar==True:
  print("Minimo 8 caracteres")
  validar=False 

 if mayuscula == True and minuscula ==True and numeros == True and y== False and validar ==True:
  validar = True #Cumple el requisito de tener mayuscula, minuscula, numeros y no alfanuméricos
 else:
  correcto=False #uno o mas requisitos de mayuscula, minuscula, numeros y no alfanuméricos no se cumple
           
 if validar == True and correcto==False:
  print("La contraseña elegida no es segura: debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")

 elif validar == True and correcto ==True:
  return True
