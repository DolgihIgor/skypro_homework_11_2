from flask import Flask, render_template
from utils import load_candidates_from_json, CANDIDATES_JSON_PATH, get_candidate, get_candidates_by_name, \
    get_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates = load_candidates_from_json(CANDIDATES_JSON_PATH).values()
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:candidate_id>")
def page_candidate(candidate_id):
    candidate = get_candidate(CANDIDATES_JSON_PATH, candidate_id)
    return render_template("card.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def page_search(candidate_name):
    candidates_search, candidates_count = get_candidates_by_name(CANDIDATES_JSON_PATH, candidate_name)
    return render_template("search.html", candidates_search=candidates_search, candidates_count=candidates_count)


@app.route("/skill/<skill_name>")
def page_skill(skill_name):
    candidates_skill, candidates_count = get_candidates_by_skill(CANDIDATES_JSON_PATH, skill_name)
    return render_template("skill.html", candidates_skill=candidates_skill, candidates_count=candidates_count,
                           skill_name=skill_name)


app.run()
