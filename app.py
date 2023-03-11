from flask import Flask, render_template
from utils import load_candidates_from_json, CANDIDATES_JSON_PATH, get_candidate

app = Flask(__name__)

@app.route("/")
def page_index():
    candidates = load_candidates_from_json(CANDIDATES_JSON_PATH).values()
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:candidate_id>")
def page_candidate(candidate_id):
    candidate = get_candidate(CANDIDATES_JSON_PATH, candidate_id)
    return render_template("card.html", candidate=candidate)

app.run()
