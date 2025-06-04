from flask import Flask, render_template

# Membuat instance Flask
app = Flask(__name__)

# Rute untuk halaman utama
@app.route('/')
def home():
    return render_template('index.html')

# Menjalankan aplikasi Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

