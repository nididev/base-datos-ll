from db.dbFunctions import get_data_from_table

def main():
    datos = get_data_from_table()
    if datos:
        for fila in datos:
            print(fila)
    else:
        print("No se encontraron datos.")

if __name__ == "__main__":
    main()
