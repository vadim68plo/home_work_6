import json
from config import DATA

def load_candidates_from_json(path=DATA):

    '''Возвращает список всех кандидатов'''

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_candidate(candidate_id):

    '''Загружает список кандидатов по номеру id'''

    candidates = load_candidates_from_json()
    candidat_list = []

    for candidat in candidates:
        if candidat["id"] == candidate_id:
            candidat_list.append(candidat)

    if len(candidat_list) == 0:
        return "Кандидат не найден"

    return candidat_list


def get_candidates_by_name(name):

    '''Возвращает кандидата по имяни или фамилии'''

    candidates = load_candidates_from_json()
    candidat_list = []

    for candidat in candidates:
        for _candidat_name in candidat["name"].split(" "):
            if _candidat_name.lower() == name.lower():
                candidat_list.append(candidat)

    if len(candidat_list) == 0:
        return "Кандидат не найден"

    return candidat_list


def get_candidates_by_skill(skill_name):

    '''Возвращает кандидатов по навыку'''

    candidates = load_candidates_from_json()
    candidat_list = []

    for candidat in candidates:
        for skill in candidat["skills"].split(", "):
            if skill.lower() == skill_name.lower():
                candidat_list.append(candidat)

    if len(candidat_list) == 0:
        return "Кандидат не найден"

    return candidat_list






