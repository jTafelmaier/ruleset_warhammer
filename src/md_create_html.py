

import bs4

from src import md_army_list
from src import md_faction_rules
from src import md_shared




def generate_htmls():

    text_html_template = md_shared.get_text_file(
        [
            "src",
            "data",
            "index_template.html"])

    dict_actions = {
            "teleportation": "This model's unit can perform the &quot;Setup teleportation&quot; and &quot;Recall&quot; actions.",
            "move": "This model can perform the &quot;Move&quot; action.",
            "scan": "This model can perform the &quot;Scan&quot; action.",
            "score": "This model's unit can perform the &quot;Score objective&quot; action.\nFurthermore, this unit can be attached to another friendly unit at deployment, if that unit does not have a higher armor characteristic than this unit. While this unit is attached to another unit, it cannot be selected as a target unit."
        }

    list_dicts_factions = md_shared.get_dict_setting("data_factions.json") \
        ["data"]

    soup_full = bs4.BeautifulSoup(
            markup=text_html_template,
            features="html.parser")

    soup_factions = bs4.BeautifulSoup(
            markup=md_faction_rules.get_text_html_faction_rules(
                list_dicts_factions=list_dicts_factions,
                dict_actions=dict_actions),
            features="html.parser")

    soup_army_list = bs4.BeautifulSoup(
            markup=md_army_list.get_text_html_army_lists(
                list_dicts_factions=list_dicts_factions,
                dict_actions=dict_actions),
            features="html.parser")

    dict_replacements = {
        "id_factions": soup_factions,
        "id_army_lists": soup_army_list}

    for id_placeholder, soup_replacement in dict_replacements.items():
        soup_full \
            .find(
                name="placeholder",
                id=id_placeholder) \
            .replace_with(soup_replacement)

    text_html_full = soup_full \
        .prettify()

    with open("index.html", mode="w", encoding="utf-8") as file_html:
        file_html \
            .write(text_html_full)

    return None

