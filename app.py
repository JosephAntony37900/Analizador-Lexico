from flask import Flask, render_template, request
import re

app = Flask(__name__)

ARCHIVO_SALIDA = 'tokens_salida.txt'
palabras_clave_map = {}

mapa_tipos = {
    "variable": "KW_VARIABLE",
    "constante": "KW_CONSTANTE",
    "funcion": "KW_FUNCION",
    "procedimiento": "KW_PROCEDIMIENTO",
    "clase": "KW_CLASE",
    "objeto": "KW_OBJETO",
    "verdadero": "KW_VERDADERO",
    "falso": "KW_FALSO",
    "nulo": "KW_NULO",
    "importar": "KW_IMPORTAR",
}

def cargar_diccionario():
    try:
        with open('diccionario.txt', 'r', encoding='utf-8') as f:
            for linea in f:
                palabra = linea.strip()
                if not palabra:
                    continue
                key = palabra.lower()
                if key in mapa_tipos:
                    palabras_clave_map[key] = mapa_tipos[key]
    except FileNotFoundError:
        pass

cargar_diccionario()

# - Puede empezar con letra minúscula (a-z) O mayúscula (A-Z) O guion bajo (_)
# - Pueden seguir letras, números o guiones bajos.
patron_identificador = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')

def obtener_token(lexema):
    key = lexema.lower()
    if key in palabras_clave_map:
        return palabras_clave_map[key]
    
    if patron_identificador.match(lexema):
        return "IDENTIFICADOR"
    
    return "ERROR_LEXICO"

@app.route('/', methods=['GET', 'POST'])
def index():
    resultados = []
    texto_entrada = ""
    
    if request.method == 'POST':
        texto_entrada = request.form.get('texto', '')
        lexemas = texto_entrada.split()
        contenido_archivo = "Token,Lexema\n"
        
        for lexema in lexemas:
            tipo_token = obtener_token(lexema)
            resultados.append({
                'token': tipo_token, 
                'lexema': lexema
            })
            contenido_archivo += f"{tipo_token},{lexema}\n"
            
        with open(ARCHIVO_SALIDA, 'w', encoding='utf-8') as f:
            f.write(contenido_archivo)

    return render_template('index.html', resultados=resultados, texto=texto_entrada)

if __name__ == '__main__':
    app.run(debug=True)