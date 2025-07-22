

import typing

from src import md_shared




def get_text_html_unit(
    dict_unit:typing.Dict,
    dict_keywords:typing.Dict,
    name_setting:str,
    name_directory_faction:str,
    bool_show_inactive_information:bool):

    def get_text_html_keyword(
        text_keyword:str):

        text_name_keyword, \
        _, \
        text_parameters = text_keyword \
            .partition(" ")

        text_title = dict_keywords \
            [text_name_keyword] \
            ["function"] \
            .replace(
                "\"",
                "&quot;")

        return "<div class=\"keyword\" title=\"" \
            + text_title \
            + "\"><span>" \
            + text_name_keyword \
            + "</span> " \
            + text_parameters \
            + "</div>"

    def get_iterable_texts_keywords(
        bool_inactive:bool):

        return map(
            get_text_html_keyword,
            filter(
                lambda text_keyword: bool_inactive == (text_keyword in {"attachable", "teleportation"}),
                dict_unit \
                    ["keywords"]))

    path_image_unit = "/" \
        .join(
            [
                md_shared.get_text_path_images_faction(
                    name_setting=name_setting,
                    name_directory_faction=name_directory_faction),
                "units",
                dict_unit \
                    ["name"] \
                    .lower() \
                    .replace(
                        " ",
                        "_") \
                    + ".png"])

    def get_text_html_row_action(
        dict_action:typing.Dict):

        def get_text_html_keywords_weapon():

            return " " \
                .join(
                    map(
                        get_text_html_keyword,
                        dict_action \
                            ["keywords"]))

        return "<tr><td class=\"td_weapon_characteristic range\">" \
            + dict_action \
                ["range"] \
            + "</td><td class=\"td_keywords\">" \
            + get_text_html_keywords_weapon() \
            + "</td><td class=\"td_weapon_characteristic strength\">" \
            + str(
                dict_action \
                    ["hits"]) \
            + "x " \
            + str(
                dict_action \
                    ["strength"]) \
            + " st</td></tr>"

    def get_text_html_inactive_information():

        if not bool_show_inactive_information:
            return ""

        return "<div class=\"inactive_data\"><span class=\"points_cost\">" \
            + str(
                dict_unit \
                    ["points_per_model"]) \
            + " points</span><br/><br/>Max health:<span class=\"max_health\">" \
            + str(
                dict_unit \
                    ["health_points"]) \
            + "</span><br/><br/>" \
            + "<br/>" \
                .join(get_iterable_texts_keywords(True)) \
            + "</div>"

    text_html_rows_actions = "\n" \
        .join(
            map(
                get_text_html_row_action,
                dict_unit
                    ["actions"]))

    return "<div class=\"container_unit\"><div class=\"div_unit\"><div class=\"div_header_unit\"><h3 class=\"h3_name_unit\">" \
        + dict_unit \
            ["name"] \
        + "</h3><div class=\"characteristics_model\"><div class=\"div_model_characteristic div_armor\"><div class=\"div_model_characteristic_name\">Armor</div><div class=\"div_model_characteristic_value\">" \
        + str(
            dict_unit \
                ["armor"]) \
        + "</div></div></div></div><div class=\"div_content_unit\" style=\"background-image: url(resources/" \
        + name_setting \
        + "/general/background.png)\"><div class=\"div_image_unit\" style=\"background-image: url(" \
        + path_image_unit \
        + ")\"><div class=\"model_properties\"><div class=\"model_property keywords\">" \
        + " " \
            .join(get_iterable_texts_keywords(False)) \
        + "</div><div class=\"model_property actions\"><table class=\"table_default fullwidth\"><tbody><tr><th class=\"th_weapon_characteristic range\"><th class=\"th_weapon_characteristic keywords\"></th><th class=\"th_weapon_characteristic strength\"></th></tr>" \
        + text_html_rows_actions \
        + "</tbody></table></div></div></div></div></div>" \
        + get_text_html_inactive_information() \
        + "</div>"

