"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)

def serialize_cupcakes():
        return {
            'id': cupcakes.id,
            'flavor': cupcakes.flavor,
            'size': cupcakes.size,
            'rating': cupcakes.rating
            'image': cupcakes.image
        }   

@app.route("/")
def root():
    """Render Homepage"""
    return render_template("index.html")

    
@app.route("/api/cupcakes")
def cupcake_data():
    all_cupcakes = Cupcake.query.all()
    serialized = [serialize_cupcakes(c) for c in cupcakes]
    return jsonify(all_cupcakes=serialized)

@app.route("/api/cupcakes/<int:id>")    
def one_cupcake(cupcake_id):
    """Return JSON"""

    cupcake = Cupcake.query.get(cupcake_id)
    serialized = serialize_cupcakes(cupcake)

    return jsonify(cupcake=serialized)
    #return serialized json of one cupcake

@app.route("/api/cupcakes" methods=["POST"])
def create_cupcake():
    """Create cupcake from data"""

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"]  

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = serialize_cupcakes(new_cupcake)

    return (jsonify(cupcake=serialized), 201)  

@app.route("/api/cupcakes/<int:id>", methods=["PATCH"])
def update_cupcakes():
    """Updates individual cupcake"""
    cupcake = Cupcake.query.get_or_404
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('size', cupcake.rating)
    db.session.commit()
    return jsonify(cupcake=serialized)

@app.route("/api/cupcakes/<int:id>", methods=["DELETE"])  
def delete_cupcake():
      """Deletes one cupcake"""
      cupcake = Cupcake.query.get_or_404(id)
      db.session.delete(cupcake)
      db.session.commit()
      return jsonify(message="Deleted")

