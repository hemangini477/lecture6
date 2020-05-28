from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

texts = ["Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima obcaecati dignissimos ratione blanditiis corrupti nemo maiores, ut voluptate ea fuga reiciendis accusantium molestiae iste animi voluptatem quae necessitatibus quisquam aspernatur exercitationem explicabo. Pariatur omnis unde dolor et ad accusantium necessitatibus harum, fugiat dolorem amet delectus, ab, aspernatur labore. Expedita provident quaerat assumenda veniam? Aperiam dolorum ratione nulla aspernatur omnis aut voluptate illo, obcaecati, at beatae asperiores exercitationem, fugit quam! Laborum voluptates blanditiis, ducimus qui minus, sapiente recusandae voluptate porro cum eum repudiandae laboriosam delectus sed culpa consectetur totam dolores mollitia hic ex! Voluptate at, animi quos libero unde quas culpa!",
"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis necessitatibus quasi vel assumenda natus voluptatem officia optio repudiandae soluta atque laborum ex labore, laboriosam tenetur nostrum ipsum ad, magni, at magnam eum. Molestiae, repudiandae! Nobis, molestiae, eaque quo recusandae laboriosam officia, accusantium animi possimus placeat corporis non suscipit. Facilis numquam natus impedit ducimus illo fugiat dolorum, earum cupiditate ipsam sapiente, at dolorem in, porro suscipit explicabo rem expedita maxime ad!",
"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolor recusandae eligendi exercitationem. Illo consequatur quod illum mollitia hic, maiores, ducimus quam quasi at obcaecati alias a inventore quia vitae, aspernatur unde aliquam repellat. Magni iusto asperiores laboriosam molestiae impedit, eaque itaque vitae maiores quidem fugiat quos aliquam commodi. Non, hic?"]

@app.route("/first")
def first():
    return texts[0]

@app.route("/second")
def second():
    return texts[1]

@app.route("/third")
def third():
    return texts[2]