

import typing

from src import md_shared
from src import md_units




def get_text_html_faction_rules(
    list_dicts_factions:typing.List[typing.Dict],
    dict_keywords:typing.Dict):

    def get_text_html_button_show_faction(
        dict_faction:typing.Dict):

        name_faction = dict_faction \
            ["name"]

        text_id_faction = "id faction " \
            + name_faction

        path_image_faction = "/" \
            .join(
                [
                    md_shared.get_text_path_images_faction(name_faction),
                    "faction.png"])

        return "<div class=\"container_faction_rules " \
            + text_id_faction \
            + "\"><div class=\"preview_faction_rules\" onclick=\"display_faction('" \
            + text_id_faction \
            + "')\" style=\"background-image: url('" \
            + path_image_faction \
            + "')\"><div class=\"faction_name\">" \
            + name_faction \
            + "</div></div></div>"

    def get_text_div_faction(
        dict_faction:typing.Dict):

        name_faction = dict_faction \
            ["name"]

        def get_text_html_unit(
            dict_unit:typing.Dict):

            return md_units.get_text_html_data_unit(
                    dict_unit=dict_unit,
                    dict_keywords=dict_keywords,
                    name_faction=name_faction)

        text_id_faction = "id faction " \
            + name_faction

        text_html_faction = "" \
            .join(
                map(
                    get_text_html_unit,
                    dict_faction \
                        ["units"]))

        return "<div class=\"div_faction " \
            + name_faction \
            + "\" id=\"" \
            + text_id_faction \
            + "\" style=\"display: none;\">" \
            + text_html_faction \
            + "</div>"

    return "<div class=\"selection_factions\">" \
        + "\n" \
            .join(
                map(
                    get_text_html_button_show_faction,
                    list_dicts_factions)) \
        + "</div><div class=\"faction_content\">" \
        + "\n" \
            .join(
                map(
                    get_text_div_faction,
                    list_dicts_factions)) \
        + "</div>"

