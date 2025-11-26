# Proyecto Final: Analizador Léxico (Scanner)

Este proyecto implementa la **Práctica 1** de la materia Lenguajes y Autómatas. Es una aplicación web construida con **Python (Flask)** que simula la primera fase de un compilador.

El programa analiza un texto de entrada ("código fuente") y clasifica cada palabra en tres categorías:

1. **Palabra Clave (KW):** Si pertenece al diccionario definido
2. **Identificador:** Si cumple con la expresión regular `^[a-z][a-z0-9]*$`
3. **Error Léxico:** Si no cumple ninguna de las reglas anteriores

---

## Estructura del Proyecto

```text
/Proyecto1_Scanner
│
├── app.py                # Lógica del servidor Flask y Analizador
├── diccionario.txt       # Base de datos de palabras válidas
├── tokens_salida.txt     # Archivo generado automáticamente (Output)
├── .gitignore            # Archivos ignorados por Git
├── README.md             # Documentación del proyecto
│
├── static/
│   └── style.css         # Hoja de estilos (CSS)
│
└── templates/
    └── index.html        # Interfaz de usuario (HTML)
```

---

## Instalación y Ejecución

### Requisitos Previos
- Python 3.11 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio** (o descargar los archivos)
   ```bash
   git clone https://github.com/JosephAntony37900/Analizador-Lexico.git
   cd Proyecto1_Scanner
   ```

2. **Crear y activar el entorno virtual:**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install flask
   ```

4. **Ejecutar la aplicación:**
   ```bash
   python app.py
   ```

5. **Abrir en el navegador:**
   
   Visita `http://127.0.0.1:5000`

---

## Diseño del Autómata Finito Determinista (DFA)

El siguiente diagrama representa la lógica del autómata utilizado para reconocer las palabras clave. Se utiliza una estructura de árbol (Trie) para optimizar la búsqueda de prefijos comunes.

> **Nota:** Los círculos dobles `(((  )))` representan estados finales (Palabras aceptadas).

```mermaid
graph TD
    q0((Inicio)) -->|s| q_s
    q0 -->|m| q_m
    q0 -->|r| q_r
    q0 -->|h| q_h
    q0 -->|i| q_i
    q0 -->|f| q_f

    %% Rama SI / SINO
    q_s -->|i| q_si(((KW_SI)))
    q_si -->|n| q_sin
    q_sin -->|o| q_sino(((KW_SINO)))

    %% Rama FIN
    q_f -->|i| q_fi
    q_fi -->|n| q_fin(((KW_FIN)))

    %% Rama MIENTRAS
    q_m -->|i| q_mi
    q_mi -->|e| q_mie
    q_mie -->|n| q_mien
    q_mien -->|t| q_mient
    q_mient -->|r| q_mientr
    q_mientr -->|a| q_mientra
    q_mientra -->|s| q_mientras(((KW_MIENTRAS)))

    %% Rama REPITE
    q_r -->|e| q_re
    q_re -->|p| q_rep
    q_rep -->|i| q_repi
    q_repi -->|t| q_repit
    q_repit -->|e| q_repite(((KW_REPITE)))

    %% Rama HASTA
    q_h -->|a| q_ha
    q_ha -->|s| q_has
    q_has -->|t| q_hast
    q_hast -->|a| q_hasta(((KW_HASTA)))

    %% Rama INICIO / IMPRIMIR
    q_i -->|n| q_in
    q_in -->|i| q_ini
    q_ini -->|c| q_inic
    q_inic -->|i| q_inici
    q_inici -->|o| q_inicio(((KW_INICIO)))

    q_i -->|m| q_im
    q_im -->|p| q_imp
    q_imp -->|r| q_impr
    q_impr -->|i| q_impri
    q_impri -->|m| q_imprim
    q_imprim -->|i| q_imprimi
    q_imprimi -->|r| q_imprimir(((KW_IMPRIMIR)))
```

---

## Expresiones Regulares Utilizadas

### Identificador
```regex
^[a-z][a-z0-9]*$
```

**Reglas:**
- Debe comenzar con una letra minúscula `[a-z]`
- Puede continuar con cualquier cantidad de letras minúsculas o dígitos `[a-z0-9]*`
- No se permiten mayúsculas ni símbolos especiales (como `_`)

**Ejemplos válidos:** `variable`, `dato1`, `x`, `contador123`

**Ejemplos inválidos:** `Variable`, `1dato`, `dato_1`, `X`

---

## Funcionamiento

1. El usuario ingresa código fuente en el área de texto
2. El analizador divide el texto en tokens individuales
3. Cada token se evalúa contra:
   - El diccionario de palabras clave (usando el DFA/Trie)
   - La expresión regular de identificadores
4. Los resultados se clasifican y muestran en pantalla
5. Se genera automáticamente el archivo `tokens_salida.txt` con los resultados

---

## Palabras Clave Reconocidas

El archivo `diccionario.txt` contiene las siguientes palabras clave:

- `inicio`
- `fin`
- `si`
- `sino`
- `mientras`
- `repite`
- `hasta`
- `imprimir`

---

## Autores

- **José Antonio Pinto Aguilar - Ana Belen Núñez Hernandez - Hector Emilio Somer Velázquez**
- Matrículas: 233416 - 233385 - 233424
- Materia: Lenguajes y Autómatas
- Institución: UPChiapas

---

## Licencia

Este proyecto es de carácter académico y fue desarrollado con fines educativos.

---