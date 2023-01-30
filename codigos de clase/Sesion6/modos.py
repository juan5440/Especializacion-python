
def main():
    print(f"el valor de __name__ es: {repr(__name__)}")
    print("dentro de main")

if __name__=="__main__":
    for i in range(20):
        print(i)

# modo de ejecucion script asigna a la variable __name__ el valor de __main__