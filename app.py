from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

filmes = [
    {"titulo": "Homem de Ferro", "ano": "2008", "nota": "7,9", "id": "0" },
    {"titulo": "Thor: O Mundo Sombrio", "ano": "2013", "nota": "6,8", "id": "1" },
    {"titulo": "Capitão América: O Soldado Invernal", "ano": "2014", "nota": "7,7", "id": "2" },
    {"titulo": "Vigadores: Era de Ultron", "ano": "2015", "nota": "7,3", "id": "3" },
    {"titulo": "Homem Aranha: Longe de Casa", "ano": "2019", "nota": "7,4", "id": "4" },
]

@app.route('/')
def index():
    return render_template("index.html", lista=filmes)

@app.route('/adicionar')
def adicionar():
    return render_template("adicionar.html")

@app.route('/salvar', methods=['POST'])
def save():
    titulo = request.form['titulo']
    ano = request.form['ano']
    nota = request.form['nota']
    for indice, i in enumerate(filmes):
        if int(indice) != int(i['id']):
            id = indice
        else:
            id = len(filmes)
    filme = { "titulo": titulo, "ano": ano, "nota": nota, "id": id}
    filmes.append(filme)
    return redirect('https://5000-silver-ferret-gf7d8nyr.ws-prod-ws-us19.gitpod.io/')

@app.route('/deletar', methods=['POST'])
def deletar():
    id = request.form['id']
    for i in filmes:
        if int(id) == int(i['id']):
            filmes.pop(int(id))
            break
    else:
        return render_template("erro.html")
    return redirect('https://5000-silver-ferret-gf7d8nyr.ws-prod-ws-us19.gitpod.io/')
   



app.run(debug=True)