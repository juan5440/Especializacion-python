def main(): 
    # try:
    #     input("digite una palabra: ")
    # except:
    #     print("\n adios...")

    # try:
    #     4/0
    # except:
    #     print("\n ocurio un error")
    input("Digite una palabra: ")

if __name__ == "__main__":
    try:
        #"hola" + 4
        main()
    except KeyboardInterrupt as e:
        print("Saliendo....")
    except ZeroDivisionError as e:
        print("division entre cero no permitida")
    except TypeError as e:  
        print("operacion no permitida")
    else:
        print("no hubo errores")
    finally:
        print("error o no estoy aqui..")
    suma = 6+4
    print("La suma es: ", suma)
