from flask import Flask, request, render_template_string

app = Flask(__name__)

# Kasıtlı olarak bırakılmış bir API anahtarı
SECRET_API_KEY = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ1234567890" 

@app.route('/search')
def search():
    query = request.args.get('query', '')
    # Kasıtlı olarak bırakılmış bir XSS zafiyeti
    # Gelen 'query' parametresi doğrudan HTML'e basılıyor.
    return render_template_string(f"<h1>Arama Sonuçları</h1><p>Aranan: {query}</p>")

if __name__ == '__main__':
    app.run(debug=True)
