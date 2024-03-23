import os
from github import Github

def ingresar_productos():
    lista_compras = []
    while True:
        producto = input("Ingrese el nombre del producto (o 'terminar' para finalizar): ")
        if producto.lower() == "terminar":
            break
        else:
            lista_compras.append(producto)
    return lista_compras

def mostrar_lista_compras(lista_compras):
    print("Lista de compras:")
    for producto in lista_compras:
        print(producto)

def subir_a_github(lista_compras):

    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        print("No se ha encontrado el token de acceso de GitHub en las variables de entorno.")
        return
    

    g = Github(token)


    user = g.get_user()
    
    repo_name = "lista_de_compras"
    repo = user.create_repo(repo_name)

    
    file_content = "\n".join(lista_compras)


    repo.create_file("lista_de_compras.txt", "Lista de compras", file_content)

    print(f"La lista de compras se ha subido correctamente al repositorio {repo_name} en GitHub.")

def main():
    lista_compras = ingresar_productos()
    mostrar_lista_compras(lista_compras)
    subir_a_github(lista_compras)

if __name__ == "__main__":
    main()