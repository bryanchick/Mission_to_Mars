from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
# import mars_scrape

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/test_mars"
mongo = PyMongo(app)


@app.route("/")
def homepage():
    result = mongo.db.test_collection.find_one()
    return render_template("index.html", result = result)


# @app.route("/scrape")
# def scrape():
#     pass
#     # that function returns a dicitionary
#     result = mars_scrape.scrape_master()
#     mongo.db.test_collection.update({}, result, upsert=True)
#     return redirect("/", 302)

# @app.route('/images/<filename>')
# def image(filename):
#     fs = gridfs.GridFS(db)
#     gridout = fs.get_last_version(filename=filename)
#     response.content_type = 'image/jpeg'
#     return gridout



if __name__ == '__main__':
    app.run(debug=True, port=5544)