import json

CANDIDATES_JSON_PATH = "candidates.json"


def load_candidates_from_json(path):
    """Возвращает список всех кандидатов"""
    candidates = {}
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
        for candidate in data:
            candidates[candidate["id"]] = candidate
        return candidates


def get_candidate(path, candidate_id):
    """Возвращает одного кандидата по его id"""
    candidates = load_candidates_from_json(path)
    candidate = candidates[candidate_id]
    return candidate


def get_candidates_by_name(path, candidate_name):
    """Возвращает кандидатов по имени"""
    candidates = load_candidates_from_json(path)
    candidate_full_name = []

    candidates_search = {}
    candidates_count = 0
    for candidate in candidates.values():
        candidate_full_name = candidate["name"].split()
        candidate_full_name = [x.lower() for x in candidate_full_name]
        if candidate_name in candidate_full_name:
            candidates_search[candidate["id"]] = candidate
            candidates_count += 1
    return candidates_search.values(), candidates_count


def get_candidates_by_skill(skill_name):
    """Возвращает кандидатов по навыку"""
    candidates = load_candidates_from_json(CANDIDATES_JSON_PATH)
    candidates_skills = []

    for candidate in candidates.values():
        candidate_skills = candidate['skills'].split(', ')
        candidate_skills = [x.lower() for x in candidate_skills]
        if skill_name in candidate_skills:
            candidates_skills.append(candidate)

    return candidates_skills
