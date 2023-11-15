from flask import Flask, render_template
import requests

app = Flask(__name__)
ALIADOS_HOST = 'http://127.0.0.1:80'
PRODUCTOS_HOST = 'http://127.0.0.1:81'

@app.route('/api/v1/gateway/aliados/<string:url>', methods=['GET'])
def get_aliado_html(url):
    aliados=obtener_aliado(url)
    aliado=None
    if aliados:
        aliado=aliados[0]
    print(aliado)
    return render_template('aliado_template.html', aliado=aliado)

def obtener_aliado(url):
    response = requests.get(f"{ALIADOS_HOST}/api/v1/aliados/{url}")
    if response.status_code == 200:
        return response.json()
    return None

@app.route('/api/v1/gateway/productos/<string:url>', methods=['GET'])
def get_producto_html(url):
    productos = obtener_producto(url)
    producto = None
    if productos:
        producto = productos[0]  
    print(producto)
    return render_template('producto_template.html', producto=producto)

def obtener_producto(url):
    response = requests.get(f"{PRODUCTOS_HOST}/api/v1/productos/{url}")
    if response.status_code == 200:
        return response.json()
    return None

app.run(host='0.0.0.0', port=82, debug=True)