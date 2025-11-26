from flask import Flask, render_template, request
import re

app = Flask(__name__)

ARCHIVO_SALIDA = 'tokens_salida.txt'
palabras_clave_map = {}

mapa_tipos = {
    "si": "KW_SI", "sino": "KW_SINO", "mientras": "KW_MIENTRAS",
    "repite": "KW_REPITE", "hasta": "KW_HASTA", "inicio": "KW_INICIO",
    "fin": "KW_FIN", "imprimir": "KW_IMPRIMIR"
}

def cargar_diccionario():
    try:
        with open('diccionario.txt', 'r', encoding='utf-8') as f:
            for linea in f:
                palabra = linea.strip()
                if palabra in mapa_tipos:
                    palabras_clave_map[palabra] = mapa_tipos[palabra]
    except FileNotFoundError:
        pass

cargar_diccionario()

patron_identificador = re.compile(r'^[a-z][a-z0-9]*$')

def obtener_token(lexema):
    if lexema in palabras_clave_map:
        return palabras_clave_map[lexema]
    
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