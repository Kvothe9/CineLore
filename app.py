from flask import Flask, render_template
import requests

app = Flask(__name__)

# Aquí estará tu lógica de Python, por ejemplo:
url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=true&language=en-US&page=1&sort_by=popularity.desc"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMDI3MWEwZjY1MzkzYThkZGU2ZDUxMTVhMTExMzk4MCIsIm5iZiI6MTcyNjc3MzQ2OC42NTY1ODgsInN1YiI6IjY2ZWM1ODJhNGEyY2QzZGM4ZDQ2YzUwMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.rU2nSqxlObQqHiN2IDk8SV6A6qbFsFszd5huwSfghh0"
}

@app.route('/')
def index():
    # Hacer la solicitud a la API
    response = requests.get(url, headers=headers)
    
    # Convertir la respuesta a JSON
    data = response.json()

    peliculas = []

    # Obtener películas de la primera y segunda página
    for page in range(1, 7):  # Cambia 3 por el número de páginas que desees obtener
        response = requests.get(f"{url}&page={page}", headers=headers)
        data = response.json()

        # Añadir los detalles de las películas a la lista
        peliculas.extend([
            {
                "titulo": movie["title"],
                "imagen": movie["poster_path"],
                "descripcion": movie["overview"],
                "fecha_estreno": movie["release_date"],
                "calificacion": movie["vote_average"]
            }
            for movie in data["results"]
        ])

    # Renderizar la página HTML y pasar la lista completa al template
    return render_template('index.html', peliculas=peliculas)
    

if __name__ == '__main__':
    app.run(debug=True)
