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


def get_candidates_by_skill(path, skill_name):
    """Возвращает кандидатов по навыку"""
    candidates = load_candidates_from_json(path)
    candidates_by_skill = {}
    candidates_skills = []
    candidates_count = 0
    for candidate in candidates.values():
        candidates_skills = candidate["skills"].split(", ")
        candidates_skills = [x.lower() for x in candidates_skills]
        if skill_name in candidates_skills:
            candidates_by_skill[candidate["id"]] = candidate
            candidates_count += 1

    return candidates_by_skill.values(), candidates_count
