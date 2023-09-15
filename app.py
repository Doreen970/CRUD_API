from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
db = SQLAlchemy(app)



class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)


@app.route("/api", methods=["POST"])
def create_person():
    data = request.get_json()
    name = data.get("name")
    person = Person(name=name)
    db.session.add(person)
    db.session.commit()
    return jsonify({'message': 'Person created successfully', 'person': {'id': person.id, 'name': person.name}}), 201



@app.route("/api/<int:id>", methods=["GET", "PUT", "DELETE"])
def manage_person(id):
    person = Person.query.get(id)
    if not person:
        return jsonify({"message": "Person not found"}), 404

    if request.method == "GET":
        return jsonify({"id": person.id, "name": person.name}), 200

    if request.method == "PUT":
        data = request.get_json()
        name = data.get("name")
        person.name = name
        db.session.commit()
        return jsonify({"message": "Person updated successfully"}), 200

    if request.method == "DELETE":
        db.session.delete(person)
        db.session.commit()
        return jsonify({"message": "Person deleted successfully"}), 204


if __name__ == "__main__":

    with app.app_context():
        db.create_all()
    app.run(debug=True)