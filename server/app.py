from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///heroes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/heroes", methods=["GET"])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([{"id": hero.id, "name": hero.name, "super_name": hero.super_name} for hero in heroes]), 200

@app.route("/heroes/<int:id>", methods=["GET"])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify({
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "hero_powers": [{"id": hp.id, "strength": hp.strength, "power_id": hp.power_id, "hero_id": hp.hero_id, 
                         "power": {"id": hp.power.id, "name": hp.power.name, "description": hp.power.description}} 
                         for hp in hero.hero_powers]
    }), 200

@app.route("/powers", methods=["GET"])
def get_powers():
    powers = Power.query.all()
    return jsonify([{"id": power.id, "name": power.name, "description": power.description} for power in powers]), 200

@app.route("/powers/<int:id>", methods=["GET"])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify({"id": power.id, "name": power.name, "description": power.description}), 200

@app.route("/powers/<int:id>", methods=["PATCH"])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    data = request.json
    if "description" in data:
        try:
            power.description = data["description"]
            db.session.commit()
            return jsonify({"id": power.id, "name": power.name, "description": power.description}), 200
        except ValueError as e:
            return jsonify({"errors": [str(e)]}), 400
    return jsonify({"error": "Invalid request"}), 400

@app.route("/hero_powers", methods=["POST"])
def create_hero_power():
    data = request.json
    try:
        hero_power = HeroPower(
            strength=data["strength"],
            hero_id=data["hero_id"],
            power_id=data["power_id"]
        )
        db.session.add(hero_power)
        db.session.commit()
        return jsonify({
            "id": hero_power.id,
            "strength": hero_power.strength,
            "hero_id": hero_power.hero_id,
            "power_id": hero_power.power_id,
            "hero": {"id": hero_power.hero.id, "name": hero_power.hero.name, "super_name": hero_power.hero.super_name},
            "power": {"id": hero_power.power.id, "name": hero_power.power.name, "description": hero_power.power.description}
        }), 201
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400
if __name__ == "__main__":
    app.run(debug=True)