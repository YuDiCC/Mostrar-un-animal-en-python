import sys

print("")
print("-------------------- ¡MUESTRAME UN ANIMAL! --------------------")

menu = """
1. Perro
2. Gato
3. Vaca
4. Oso
0. Salir
""" 

while True:
    print("Selecciona una opción:")
    print(menu)
    opc = int(input("Porfavor elije un animal: "))
    if opc == 1:
        print("""
,-.___,-.
\_/_ _\_/
  )O_O(
 { (_) }
  `-^-'   

""")

        
    elif opc == 2:
        print("""

      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)  

""")

        
    elif opc == 3:
        print("""
((...))
( O O ) 
 \   /   
 (`_`)  

""")

        
    elif opc == 4:
        print("""
  _      _                        
 : `.--.' ;              _....,_  
 .'      `.      _..--'"'       `-._
:          :_.-'"                  .`.
:  6    6  :                     :  '.;
:          :                      `..';
`: .----. :'                          ;
  `._Y _.'               '           ;
    'U'      .'          `.         ; 
       `:   ;`-..___       `.     .'`.
       _:   :  :    ```"''"'``.    `.  `.
     .'     ;..'            .'       `.'`
    `.......'              `........-'`
       
""")

        
    elif opc == 0:
        sys.exit()


