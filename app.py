from flask import Flask, render_template, jsonify, request, session

app = Flask(__name__,static_folder='static')
app.secret_key = 'lullabynest-flask-secret'

PRODUCTS = [
    {"id":1, "name":"Wall Mounted Classic Cradle",  "price":1999, "original_price":2499, "badge":"Bestseller", "category":"cradle"},
    {"id":2, "name":"Window Mounted Classic Cradle",   "price":2100,  "original_price":2799, "badge":"Eco Pick(OUT-OF STOCK)",   "category":"bassinet"},
    {"id":3, "name":"Cradle Combo",    "price":2999, "original_price":3999, "badge":"Premium",    "category":"premium"},
]

OFFERS = [
    {"code":"LULLABY30","title":"Welcome Offer","discount":30, "desc":"30% off your first order"},
    {"code":"NESTFREE", "title":"Free Shipping","discount":0,  "desc":"Free delivery on ₹8,000+"},
    {"code":"ROYALE20", "title":"Luxury Deal",  "discount":20, "desc":"20% off Violet Royale"},
    {"code":"REFER500", "title":"Refer a Friend","discount":0, "desc":"₹500 cashback on referral"},
]

@app.route('/')
def home():
    return render_template('index.html', products=PRODUCTS[:3], offers=OFFERS[:2])

@app.route('/products')
def products():
    return render_template('products.html', products=PRODUCTS)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/offers')
def offers():
    return render_template('offers.html', offers=OFFERS)

@app.route('/api/cart/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    cart = session.get('cart', [])
    cart.append(data.get('product_id'))
    session['cart'] = cart
    return jsonify({"status":"ok","cart_count":len(cart)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
