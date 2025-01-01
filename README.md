# Urban Routes Automation Testing

## Descripción del Proyecto

Este proyecto está diseñado para realizar pruebas automatizadas sobre la funcionalidad de la aplicación **Urban Routes**, que es una plataforma para la solicitud de taxis. Las pruebas cubren desde la configuración de la dirección del usuario, la selección de la tarifa, la adición del número de teléfono, la adición de un método de pago, hasta la finalización del pedido de taxi.

### **Tecnologías Utilizadas**

- **Python**: Lenguaje de programación principal.
- **Selenium**: Herramienta para la automatización del navegador web.
- **Pytest**: Framework para escribir y ejecutar pruebas en Python.
- **Git**: Control de versiones para gestionar el código fuente.
- **WebDriver**: Para interactuar con el navegador web en las pruebas.
- **JSON**: Utilizado para manejar las respuestas de la API en el proceso de obtención de códigos de confirmación.

### **Instrucciones para Ejecutar las Pruebas**
Instala las dependencias necesarias:
    pip install -r requirements.txt

Ejecuta las pruebas con Pytest:
pytest main.py --no-header --no-summary -q

Las pruebas se ejecutarán y se mostrará un informe de los resultados en la terminal.