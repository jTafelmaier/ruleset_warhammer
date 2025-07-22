

import typing

from lib.unary import _dicts
from lib.unary import _iters

from src import md_shared
from src import md_units




def get_text_html_faction_rules(
    dict_factions:typing.Dict,
    dict_keywords:typing.Dict,
    name_setting:str):

    def get_text_html_faction_list_building(
        dict_faction:typing.Dict):

        name_faction = dict_faction \
            ["name"]

        name_directory_faction = md_shared.get_text_name_directory_faction(name_faction)

        def get_text_html_unit(
            dict_unit:typing.Dict):

            return md_units.get_text_html_unit(
                    dict_unit=dict_unit,
                    dict_keywords=dict_keywords,
                    name_setting=name_setting,
                    name_directory_faction=name_directory_faction,
                    bool_show_inactive_information=True)

        return "" \
            .join(
                map(
                    get_text_html_unit,
                    dict_faction \
                        ["units"]))

    def get_text_html_button_show_faction(
        dict_faction:typing.Dict):

        name_faction = dict_faction \
            ["name"]

        name_directory_faction = md_shared.get_text_name_directory_faction(name_faction)

        text_id_faction = "id_faction_" \
            + name_directory_faction

        path_image_faction = "/" \
            .join(
                [
                    md_shared.get_text_path_images_faction(
                        name_setting=name_setting,
                        name_directory_faction=name_directory_faction),
                    "background.png"])

        return "<div class=\"div_container_faction_rules " \
            + text_id_faction \
            + "\"><div class=\"div_button_faction_rules\" onclick=\"display_faction('" \
            + text_id_faction \
            + "')\" style=\"background-image: url('" \
            + path_image_faction \
            + "')\"><div class=\"div_faction_name\">" \
            + name_faction \
            + "</div></div></div>"

    def get_text_div_faction(
        dict_faction:typing.Dict):

        name_faction = dict_faction \
            ["name"]

        name_directory_faction = md_shared.get_text_name_directory_faction(name_faction)

        text_id_faction = "id_faction_" \
            + name_directory_faction

        text_html_faction = get_text_html_faction_list_building(dict_faction)

        return "<div class=\"div_faction " \
            + name_directory_faction \
            + "\" id=\"" \
            + text_id_faction \
            + "\" style=\"display: none;\">" \
            + text_html_faction \
            + "</div>"

    list_dicts_factions = dict_factions \
        >> _dicts.to_iterable_values() \
        >> _iters.to_iterable_chained() \
        >> _iters.to_list()

    text_html_buttons_factions = "\n" \
        .join(
            map(
                get_text_html_button_show_faction,
                list_dicts_factions))

    return "<div class=\"div_buttons_factions\">" \
        + text_html_buttons_factions \
        + "</div><div class=\"div_faction_content\">" \
        + "\n" \
            .join(
                map(
                    get_text_div_faction,
                    list_dicts_factions)) \
        + "</div>"

