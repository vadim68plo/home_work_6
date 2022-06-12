from flask import Flask, render_template, request
import utils

app = Flask(__name__)

@app.route("/")
def page_index():
    candidates = utils.load_candidates_from_json()

    return render_template("list.html", items=candidates)

@app.route("/candidates/<int:id>")
def page_candidat(id):
    candidat = utils.get_candidate(id)

    if candidat != "Кандидат не найден":
        candidat = candidat[0]
        return render_template("single.html", candidat=candidat)
    else:
        return candidat

@app.route("/search/<candidate_name>")
def page_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    len_candidates = len(candidates)

    if candidates != "Кандидат не найден":
        return render_template("search.html", len=len_candidates, candidates=candidates)
    else:
        return candidates

@app.route("/skill/<skill_name>")
def page_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    len_candidates = len(candidates)
    _skill = skill_name

    if candidates != "Кандидат не найден":
        return render_template("skill.html", len=len_candidates, candidates=candidates, skill=_skill)
    else:
        return candidates

app.run(host='0.0.0.0', port=800)

