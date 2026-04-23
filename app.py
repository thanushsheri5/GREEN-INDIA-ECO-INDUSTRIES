from flask import Flask, render_template, session, redirect
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

# ---------------- DATABASE ----------------
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# ---------------- HOME ----------------
@app.route('/')
def home():
    db = get_db()
    products = db.execute("SELECT * FROM products").fetchall()
    return render_template('index.html', products=products)

# ---------------- ADD TO CART ----------------
@app.route('/add/<int:id>')
def add_to_cart(id):
    if 'cart' not in session:
        session['cart'] = []

    session['cart'].append(id)
    session.modified = True

    return redirect('/')

# ---------------- VIEW CART ----------------
@app.route('/cart')
def cart():
    if 'cart' not in session or len(session['cart']) == 0:
        return "Cart is empty"

    db = get_db()
    items = []

    for pid in session['cart']:
        product = db.execute("SELECT * FROM products WHERE id=?", (pid,)).fetchone()
        if product:
            items.append(product)

    return render_template('cart.html', items=items)

# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(debug=True)