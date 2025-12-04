# Proyecto Final: Analizador Léxico (Scanner)

Este proyecto implementa la **Práctica 1** de la materia Lenguajes y Autómatas. Es una aplicación web construida con **Python (Flask)** que simula la primera fase de un compilador.

El programa analiza un texto de entrada ("código fuente") y clasifica cada palabra en tres categorías:

1. **Palabra Clave (KW):** Si pertenece al diccionario definido
2. **Identificador:** Si cumple con la expresión regular `^[a-zA-Z_][a-zA-Z0-9_]*$` (Permite mayúsculas y guiones bajos).
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
    q0((Inicio)) -->|v| q_v
    q0 -->|c| q_c
    q0 -->|f| q_f
    q0 -->|p| q_p
    q0 -->|o| q_o
    q0 -->|n| q_n
    q0 -->|i| q_i

    %% Rama VARIABLE
    q_v -->|a| q_va
    q_va -->|r| q_var
    q_var -->|i| q_vari
    q_vari -->|a| q_varia
    q_varia -->|b| q_variab
    q_variab -->|l| q_variabl
    q_variabl -->|e| q_variable(((KW_VARIABLE)))

    %% Rama VERDADERO
    q_v -->|e| q_ve
    q_ve -->|r| q_ver
    q_ver -->|d| q_verd
    q_verd -->|a| q_verda
    q_verda -->|d| q_verdad
    q_verdad -->|e| q_verdade
    q_verdade -->|r| q_verdader
    q_verdader -->|o| q_verdadero(((KW_VERDADERO)))

    %% Rama CONSTANTE / CLASE
    q_c -->|o| q_co
    q_co -->|n| q_con
    q_con -->|s| q_cons
    q_cons -->|t| q_const
    q_const -->|a| q_consta
    q_consta -->|n| q_constan
    q_constan -->|t| q_constant
    q_constant -->|e| q_constante(((KW_CONSTANTE)))

    q_c -->|l| q_cl
    q_cl -->|a| q_cla
    q_cla -->|s| q_clas
    q_clas -->|e| q_clase(((KW_CLASE)))

    %% Rama FUNCION / FALSO
    q_f -->|u| q_fu
    q_fu -->|n| q_fun
    q_fun -->|c| q_func
    q_func -->|i| q_funci
    q_funci -->|o| q_funcio
    q_funcio -->|n| q_funcion(((KW_FUNCION)))

    q_f -->|a| q_fa
    q_fa -->|l| q_fal
    q_fal -->|s| q_fals
    q_fals -->|o| q_falso(((KW_FALSO)))

    %% Rama PROCEDIMIENTO
    q_p -->|r| q_pr
    q_pr -->|o| q_pro
    q_pro -->|c| q_proc
    q_proc -->|e| q_proce
    q_proce -->|d| q_proced
    q_proced -->|i| q_procedi
    q_procedi -->|m| q_procedim
    q_procedim -->|i| q_procedimi
    q_procedimi -->|e| q_procedimie
    q_procedimie -->|n| q_procedimien
    q_procedimien -->|t| q_procedimient
    q_procedimient -->|o| q_procedimiento(((KW_PROCEDIMIENTO)))

    %% Rama OBJETO
    q_o -->|b| q_ob
    q_ob -->|j| q_obj
    q_obj -->|e| q_obje
    q_obje -->|t| q_objet
    q_objet -->|o| q_objeto(((KW_OBJETO)))

    %% Rama NULO
    q_n -->|u| q_nu
    q_nu -->|l| q_nul
    q_nul -->|o| q_nulo(((KW_NULO)))

    %% Rama IMPORTAR
    q_i -->|m| q_im
    q_im -->|p| q_imp
    q_imp -->|o| q_impo
    q_impo -->|r| q_impor
    q_impor -->|t| q_import
    q_import -->|a| q_importa
    q_importa -->|r| q_importar(((KW_IMPORTAR)))
```

---

## Expresiones Regulares Utilizadas

### Identificador
```regex
^[a-zA-Z_][a-zA-Z0-9_]*$
```

**Reglas:**
- Debe comenzar con una letra (minúscula o mayúscula) o un guion bajo _
- Puede continuar con cualquier cantidad de letras, dígitos o guiones bajos
- Diferencia: Acepta mayúsculas y formato snake_case

**Ejemplos válidos:** `variable`, `Mi_Dato`, `_privado`, `Contador123`

**Ejemplos inválidos:** `var-dato`, `1dato`, `@user`

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

- `variable`
- `constante`
- `funcion`
- `procedimiento`
- `clase`
- `objeto`
- `verdadero`
- `falso`
- `nulo`
- `importar`

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