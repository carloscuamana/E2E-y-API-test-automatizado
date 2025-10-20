Para realizar este ejercicio realize los siguientes pasos
  1 entre en en la pagina y busque los localizadores necesarios.
  2 cree un codigo de Python usando los frameworks: selenium y pytest
  3 cree una prueba que busca 2 productos: primero busca al "Samsung galaxy s6" espera 5 segundos para que aparesca la alerta de chrome y poder pasarla, y luego vuelve a ingresar en la pagina de inicio para buscar el segundo producto "Sony vaio i7"
  4 despues de agregar los productos el codigo le da clic a "cart" desde la pagina del segundo producto, una vez en la pagina se toma 30 segundos para visualizar el carrito
  5 al pasar los 30 segundos se da clic en "Place Order", espera a que cargue el formulario y lo llena
  6 una vez lleno el formulario se da clic en el boton "Purchase"
  7 el codigo confirma que la compra fue exitosa si aparace la ventana "Thank you for your purchase", que es reconocida si aparce el boton "ok"