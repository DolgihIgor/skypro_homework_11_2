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


def get_candidate(candidate_id):
    """Возвращает одного кандидата по его id"""
    pass


def get_candidates_by_name(candidate_name):
    """Возвращает кандидатов по имени"""
    pass


def get_candidates_by_skill(skill_name):
    """Возвращает кандидатов по навыку"""
    pass


