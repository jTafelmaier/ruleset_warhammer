

import bs4

from src import md_army_list
from src import md_faction_rules
from src import md_shared




def generate_htmls():

    text_html_template = md_shared.get_text_file(
        [
            "src",
            "data",
            "template_index.html"])

    list_dicts_factions = md_shared.get_dict_setting("data_factions.json") \
        ["data"]

    soup_full = md_shared.get_soup(text_html_template)

    soup_factions = md_shared.get_soup(md_faction_rules.get_text_html_faction_rules(list_dicts_factions))

    soup_army_list = md_shared.get_soup(md_army_list.get_text_html_army_lists(list_dicts_factions))

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

