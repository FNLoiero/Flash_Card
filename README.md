# 🃏 Flash Card

Una aplicación de tarjetas didácticas desarrollada en Python con Tkinter. Ayuda a aprender vocabulario en distintos idiomas mostrando tarjetas con palabras en un idioma y su traducción al reverso.

## 🚀 Características

- **Interfaz intuitiva** basada en Tkinter.
- **Cambio automático de tarjetas** cada 3 segundos.
- **Botones para marcar palabras aprendidas** y eliminarlas del listado.
- **Almacenamiento de progreso** en un archivo CSV.

## 📷 Vista previa

![image](https://github.com/user-attachments/assets/a301451a-b1ee-40cf-a2e3-39496a6d8c03)

![image](https://github.com/user-attachments/assets/255aec93-f771-432f-90fa-9849bfdadc18)

## 🖥️ Uso

1. **Ejecutá la aplicación**.
2. **Observá la palabra en francés**.
3. **Esperá 3 segundos** para ver la traducción al inglés.
4. **Marcá la palabra como aprendida** si la recordaste correctamente.
5. **Seguí practicando** hasta aprender todas las palabras.

## 📋 Estructura del proyecto

```
flash-card/
├── main.py          # Código principal con Tkinter
├── data/
│   ├── french_words.csv  # Archivo con palabras en francés e inglés
│   ├── words_to_learn.csv  # Progreso del usuario
├── images/
│   ├── card_front.png  # Imagen del frente de la tarjeta
│   ├── card_back.png   # Imagen del reverso de la tarjeta
│   ├── right.png       # Botón de correcto
│   ├── wrong.png       # Botón de incorrecto
└── requirements.txt   # Dependencias necesarias
```
