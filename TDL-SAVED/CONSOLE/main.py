import json

FILE_NAME = "todolist.json"

def cargar_tareas():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_tareas(tareas):
    with open(FILE_NAME, "w") as file:
        json.dump(tareas, file, indent=4)

def mostrar_tareas(tareas):
    print("\nLista de Tareas:")
    for i, tarea in enumerate(tareas):
        estado = "✔" if tarea["completada"] else "✘"
        print(f"{i + 1}. [{estado}] {tarea['descripcion']}")
    print()

def agregar_tarea(tareas):
    descripcion = input("Descripción de la nueva tarea: ")
    tareas.append({"descripcion": descripcion, "completada": False})
    guardar_tareas(tareas)
    print("Tarea agregada.")

def marcar_completada(tareas):
    mostrar_tareas(tareas)
    try:
        indice = int(input("Número de la tarea a marcar como completada: ")) - 1
        if 0 <= indice < len(tareas):
            tareas[indice]["completada"] = True
            guardar_tareas(tareas)
            print("Tarea marcada como completada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada no válida.")

def menu():
    tareas = cargar_tareas()
    while True:
        print("\nMenú:")
        print("1. Mostrar tareas")
        print("2. Agregar tarea")
        print("3. Marcar tarea como completada")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            marcar_completada(tareas)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()