

import copy
import typing

import bs4

from src import md_shared
from src import md_units




def get_text_html_faction_rules(
    list_dicts_factions:typing.List[typing.Dict]):

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

            def get_text_enhancement(
                dict_enhancement:typing.Dict):

                dict_enhancement_copy = copy.copy(dict_enhancement)

                dict_enhancement_copy["is_enhancement"] = True
                dict_enhancement_copy["is_revealable"] = False
                dict_enhancement_copy["to_replace"] = False

                return "<div class=\"enhancement_option\">" \
                    + md_units.get_text_html_action(dict_enhancement_copy) \
                    + ("<span>[invisible]</span>" if dict_enhancement["is_revealable"] else "") \
                    + ("<span>[replaces index " + str(dict_enhancement["replace_id"]) + "]</span>" if dict_enhancement["replace_id"] is not None else "") \
                    + "</div>"

            text_html_enhancements = "" \
                .join(
                    map(
                        get_text_enhancement,
                        dict_unit \
                            ["enhancements"]))

            return "<div class=\"unit_options\">" \
                + md_units.get_text_html_data_unit(
                    dict_unit=dict_unit,
                    name_faction=name_faction) \
                + "<div class=\"enhancement_options\"><div>Enhancements:</div><br/>" \
                + text_html_enhancements \
                + "</div></div>"

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

