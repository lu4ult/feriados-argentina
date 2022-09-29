# feriados-argentina

Este pequeño script busca obtener el listado de días feriados de Argentina desde la API de https://nolaborables.com.ar
para luego filtrar los datos que me interesan y reducir los caracteres de los índices, ya que el resultado será consumido por un microcontrolador ESP8266 el cuál posee memoria limitada y el uso de la API ya citada generaba fragmentación del HEAP.

Además, puedo de esta forma agregar feriados que no fueron agregados durante este año, como el del Censo en Mayo.
También se reemplazan los caracteres con tildes o la Ñ (Ejemplo año nuevo): &iacute, ya que se utilizarán estos datos dentro de un HTML.

Muestra JSON original:

![Json original](no-laborable.png)

Muestra JSON adaptado:

![Json Adapatado](adaptación.png)