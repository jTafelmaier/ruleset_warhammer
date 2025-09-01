

import typing

import bs4

from src import md_shared
from src import md_units




def get_text_html_faction_rules(
    list_dicts_factions:typing.List[typing.Dict],
    dict_descriptions_actions:typing.Dict):

    def get_text_html_button_show_faction(
        dict_faction:typing.Dict):

        name_faction = dict_faction \
            ["name"]

        path_image_faction = "/" \
            .join(
                [
                    md_shared.get_text_path_images_faction(name_faction),
                    "faction.png"])

        return "<div class=\"container_faction_button " \
            + name_faction \
            + "\"><a class=\"preview_faction_button\" href=\"index_" \
            + name_faction \
            + ".html\" style=\"background-image: url('" \
            + path_image_faction \
            + "')\">" \
            + name_faction \
            + "</a></div>"

    def create_html_faction(
        dict_faction:typing.Dict):

        name_faction = dict_faction \
            ["name"]

        def get_text_html_unit(
            dict_unit:typing.Dict):

            return md_units.get_text_html_data_unit(
                    dict_unit=dict_unit,
                    dict_descriptions_actions=dict_descriptions_actions,
                    name_faction=name_faction,
                    list_indices_enhancements=list(range(len(dict_unit["actions"]))),
                    bool_show_invisible_enhancements=True)

        text_html_faction = "" \
            .join(
                map(
                    get_text_html_unit,
                    dict_faction \
                        ["units"]))

        text_html = "<!DOCTYPE html><html><body><div class=\"faction_rules " \
            + name_faction \
            + "\">" \
            + text_html_faction \
            + "</div></body></html>"

        # TODO refactor: duplicate
        soup_faction = bs4.BeautifulSoup(
                markup=text_html,
                features="html.parser")

        text_html_template = md_shared.get_text_file(
            [
                "src",
                "data",
                "template_faction.html"])

        soup_full = bs4.BeautifulSoup(
                markup=text_html_template,
                features="html.parser")

        soup_full \
            .find(
                name="placeholder",
                id="id_faction") \
            .replace_with(soup_faction)

        with open("index_" + name_faction + ".html", mode="w", encoding="utf-8") as file_html:
            file_html \
                .write(
                    soup_full \
                        .prettify())

        return

    # TODO refactor
    list(
        map(
            create_html_faction,
            list_dicts_factions))

    return "<div class=\"selection_factions\">" \
        + "" \
            .join(
                map(
                    get_text_html_button_show_faction,
                    list_dicts_factions)) \
        + "</div>"

