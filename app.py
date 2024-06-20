from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    tips = [
        "Usa transporte público o comparte tu coche.",
        "Reduce, reutiliza y recicla.",
        "Apaga las luces y los aparatos electrónicos cuando no los uses.",
        "Come menos carne y más vegetales.",
        "Compra productos locales y de temporada.",
        "Usa bombillas de bajo consumo.",
        "Planta árboles y apoya la reforestación.",
        "Reduce el uso de agua caliente."
    ]
    return render_template('home.html', tips=tips)

if __name__ == '__main__':
    app.run(debug=True)
