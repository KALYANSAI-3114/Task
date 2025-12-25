from flask import Flask, request, jsonify,render_template
from nlp_code import parse_query
from sql_builder import build_sql
from db import execute_query
from flask_cors import CORS

app = Flask(__name__,static_folder="static",template_folder="templates")
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")
#main api 
@app.route("/query", methods=["POST"])
def query():
    try:
        data = request.get_json()
        question = data.get("question", "")

        if not question:
            return jsonify({"error": "Question is required"}), 400

        # 1. NLP → extract intent & filters
        parsed = parse_query(question)

        # 2. Convert NLP to SQL
        sql = build_sql(parsed)

        # 3. Run SQL on MySQL Database
        result = execute_query(sql)

        return jsonify({
            "question": question,
            "parsed_intent": parsed,
            "generated_sql": sql,
            "result": result
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
