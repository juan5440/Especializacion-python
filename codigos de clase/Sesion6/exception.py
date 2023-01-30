def main():
    # try:
    #     input("digite una palabra: ")
    # except:
    #     print("\nadios....")

    # try:
    #     4/0
    # except Exception as e:
    #     print("ocurrio error", e)
    input("digite una palabra: ")

if __name__=="__main__":
    try:
        # 4/0
        "hola" + 4
        main()
    except KeyboardInterrupt as e:
        print("saliendo....")
    except ZeroDivisionError as e:
        print("divsion entre cero no permitida")
    except TypeError as e:
        print("operacion no permitida")
    else:
        print("no hubo errores")
    finally:
        print("error o no aqui estoy")
    
    suma = 6+4
    print("la suma es: ",suma)
