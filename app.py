from flask import (Flask, 
                   jsonify, 
                   request, 
                   render_template, 
                   redirect, 
                   url_for, 
                   send_from_directory, 
                   make_response,
                   abort)



app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def register():
    return render_template('register.html')

# Route for the root URL ("/")
@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html', title="Jelwery", active_page="main")

# Route for /products/
@app.route('/products/', methods=['GET'])
def product_page():
    return render_template('products.html', title="Products", active_page="product")

# Route for /contact
@app.route('/contact/', methods=['GET'])
def contact_page():
    return render_template('contact.html', title="Contact", active_page="contact")


ALLOWED_EXTENSIONS = {'webp', 'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/static/images/<path:file_name>')
def server_image(file_name):
    if allowed_file(file_name):
        return send_from_directory('static/images', file_name, mimetype=f'image/{file_name.rsplit(".", 1)[1]}')
    else:
        return 'Invalid image format', 404

@app.route('/about/', methods=['GET'])
def about_page():
    return render_template('about.html', title="About us", active_page="about")

@app.route('/cart/', methods=['GET'])
def cart_page():    
    return render_template('cart.html', title="Your cart")

# Route for handling invalid URLs
@app.errorhandler(404)
def page_not_found(error):
    # Redirect to the root URL ("/")
    return redirect(url_for('main_page'))

if __name__ == '__main__':
    app.run(host="0.0.0.0")