# Bank OCR

Bank OCR es un script de Python diseñado para procesar archivos de texto que contienen representaciones de números de cuenta en un formato específico. Este proyecto se ha desarrollado como parte de un ejercicio para demostrar habilidades técnicas en el manejo de archivos y procesamiento de datos en Python.

## Cómo usar

1. Clona este repositorio en tu computadora usando `git clone https://github.com/dlucianop/bank-ocr`.
2. Navega hasta el directorio del proyecto `cd bank-ocr`.
3. Asegúrate de tener Python 3.x instalado en tu sistema.
4. Ejecuta el script `python bank_ocr.py`.

## Cómo funciona

1. Seleccionar archivo de texto: Al ejecutar el script, se abrirá una ventana que te permitirá seleccionar un archivo de texto que contenga las representaciones de los números de cuenta. Utiliza esta ventana para navegar hasta el archivo que deseas procesar y haz clic en "Abrir".

2. Procesamiento del archivo: Una vez seleccionado el archivo, el script procesará su contenido para identificar los números de cuenta. Utiliza una técnica de reconocimiento óptico de caracteres (OCR) para interpretar las representaciones de números en el archivo y convertirlas en números de cuenta legibles.

3. Validación de los números de cuenta: Después de identificar los números de cuenta, el script los valida para garantizar su precisión. Realiza comprobaciones adicionales para verificar la integridad de los números de cuenta.

4. Registro de resultados: Los resultados de las validaciones se muestran en la consola y también se registran en un archivo de reporte llamado reporte.txt. Este archivo contiene una lista de los números de cuenta procesados junto con su estado de validación (OK, ILL o ERR).

5. Finalización del proceso: Una vez completado el procesamiento del archivo, el script finaliza su ejecución. Puedes revisar el archivo de reporte para obtener una visión general de los resultados de la validación.

## Requisitos previos

- Python 3.x instalado en tu sistema.

## Licencia

Este proyecto se proporciona solo con fines educativos y de demostración. No tiene una licencia específica y está disponible para uso y revisión pública.

## Contacto

Para más información o preguntas, contáctame en [3112dlp@gmail.com].