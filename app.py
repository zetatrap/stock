from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Configuración de la base de datos SQLite
def init_db():
    with sqlite3.connect("stock.db") as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        quantity INTEGER NOT NULL
                        )''')
init_db()

# Ruta principal que renderiza la página web
@app.route("/")
def index():
    return render_template("index.html")

# Endpoint para obtener el listado de productos
@app.route("/api/products", methods=["GET"])
def get_products():
    with sqlite3.connect("stock.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        return jsonify(products)

# Endpoint para agregar un nuevo producto
@app.route("/api/products", methods=["POST"])
def add_product():
    data = request.json
    name = data.get("name")
    quantity = data.get("quantity", 0)
    with sqlite3.connect("stock.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, quantity) VALUES (?, ?)", (name, quantity))
        conn.commit()
    return jsonify({"message": "Producto agregado correctamente"}), 201

# Endpoint para actualizar la cantidad de un producto
@app.route("/api/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.json
    quantity = data.get("quantity")
    with sqlite3.connect("stock.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (quantity, product_id))
        conn.commit()
    return jsonify({"message": "Cantidad actualizada correctamente"})

# Endpoint para eliminar un producto
@app.route("/api/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    with sqlite3.connect("stock.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        conn.commit()
    return jsonify({"message": "Producto eliminado correctamente"})

if __name__ == "__main__":
    app.run(debug=True)
