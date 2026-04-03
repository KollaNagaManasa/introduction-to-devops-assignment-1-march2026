from flask import Flask, jsonify, request, render_template, Response
from flask_cors import CORS

# -----------------------------
# Program Data
# -----------------------------
PROGRAMS = {
    "Fat Loss (FL)": {
        "code": "FL",
        "calorie_factor": 22,
    },
    "Muscle Gain (MG)": {
        "code": "MG",
        "calorie_factor": 35,
    },
    "Beginner (BG)": {
        "code": "BG",
        "calorie_factor": 26,
    },
}

GYM_METRICS = {
    "capacity": 150,
    "area_sqft": 10000,
    "breakeven_members": 250,
}

# -----------------------------
# App Factory
# -----------------------------
def create_app():
    app = Flask(__name__, template_folder="templates")
    CORS(app)

    app.config["WORKOUTS"] = []
    app.config["MEMBERS"] = []

    # -----------------------------
    # Routes
    # -----------------------------
    @app.route("/")
    def home():
        return jsonify({"message": "ACEest Fitness API running"}), 200

    @app.route("/health")
    def health():
        return jsonify({"status": "healthy"}), 200

    @app.route("/programs")
    def programs():
        return jsonify(PROGRAMS), 200

    @app.route("/calories", methods=["POST"])
    def calories():
        data = request.get_json()
        weight = data.get("weight_kg")
        code = data.get("program_code")

        for program in PROGRAMS.values():
            if program["code"] == code:
                calories = weight * program["calorie_factor"]
                return jsonify({"estimated_daily_kcal": calories}), 200

        return jsonify({"error": "Invalid program"}), 400

    @app.route("/gym-info")
    def gym_info():
        return jsonify(GYM_METRICS), 200

    return app


# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8080)
