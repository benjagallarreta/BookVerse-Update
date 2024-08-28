from decimal import Decimal

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")  # Utilizar get en lugar de llamar a la sesión
        if not carrito:
            self.session["carrito"] = {}
        self.carrito = self.session["carrito"]

    def agregar(self, libro):
        isbn = str(libro.isbn)
        if isbn not in self.carrito:
            self.carrito[isbn] = { 
                "Libro_isbn": libro.isbn,
                "Titulo": libro.titulo,
                "Autor":libro.autor,
                "Portada":libro.portada.url,
                "Formato": libro.tipo,
                "Acumulado": str(libro.precio),
                "Cantidad": 1, 
            }
        else:
            self.carrito[isbn]["Cantidad"] += 1
            self.carrito[isbn]["Acumulado"] = str(
                Decimal(self.carrito[isbn]["Acumulado"]) + Decimal(libro.precio)
            )
        self.guardarCarrito()
    
    def guardarCarrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, libro):
        isbn = str(libro.isbn)
        if isbn in self.carrito:
            del self.carrito[isbn]
            self.guardarCarrito()

    def restar(self, libro):
        isbn = str(libro.isbn)
        if isbn in self.carrito:
            self.carrito[isbn]["Cantidad"] -= 1
            self.carrito[isbn]["Acumulado"] = str(
                Decimal(self.carrito[isbn]["Acumulado"]) - Decimal(libro.precio)
            )
            if self.carrito[isbn]["Cantidad"] <= 0:
                self.eliminar(libro)
            self.guardarCarrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True