# Definir el perfil del usuario con información básica
perfil_usuario = {

    "nombre": "Carlos",
    "edad": 30,
    "ciudad": "Barcelona",
    "amigos": [
        {"nombre": "Ana", "tiempo_amistad": "5 años"},
        {"nombre": "Luis", "tiempo_amistad": "3 años"},
        {"nombre": "Marta", "tiempo_amistad": "2 años"}
    ],
    "posts": [
        {
            "contenido": "¡Hola, mundo!",
            "likes": 10,
            "comentarios": ["Bien dicho!", "Me gusta"]
        },
        {
            "contenido": "Amo viajar",
            "likes": 25,
            "comentarios": ["¡Genial!", "¿A dónde fuiste?"]
        }
    ]
}

print(f"Nombre: {perfil_usuario['nombre']}")
print(f"Edad: {perfil_usuario['edad']}")
print(f"Ciudad: {perfil_usuario['ciudad']}\n")

print("Amigos:")
for amigos in perfil_usuario["amigos"]:
    print(f"- {amigos['nombre']} (Amigos desde hace {amigos['tiempo_amistad']})")

print("\nPosts:")
for post in perfil_usuario["posts"]:
    print(f"- {post['contenido']} ({post['likes']} likes)")
    print("  Comentarios:")
    for comentario in post["comentarios"]:
        print(f"    - {comentario}")
