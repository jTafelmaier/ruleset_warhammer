

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

        dict_keyword = dict_keywords \
            [text_name_keyword]

        text_title = dict_keyword \
            ["function"] \
            .replace(
                "<br/>",
                "\n") \
            .replace(
                "\"",
                "&quot;")

        return "<div class=\"keyword" \
            + " " \
            + dict_keyword \
                ["type"] \
            + "\" title=\"" \
            + text_title \
            + "\"><span>" \
            + text_name_keyword \
            + "</span> " \
            + text_parameters \
            + "</div>"

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

        def get_text_weapon_range():

            if dict_action["range"] == 0:
                return "-"
            elif dict_action["range"] == 5:
                return "melee"
            else:
                return str(dict_action["range"]) \
                    + " cm"

        def get_text_html_keywords_weapon():

            return " " \
                .join(
                    map(
                        get_text_html_keyword,
                        dict_action \
                            ["keywords"]))

        def get_text_html_attack():

            int_hits = dict_action \
                ["hits"]

            int_damage = dict_action \
                ["strength"]

            return "<tr><td class=\"td_weapon_characteristic range\">" \
                + get_text_weapon_range() \
                + "</td><td class=\"td_keywords\">" \
                + get_text_html_keywords_weapon() \
                + "</td><td class=\"td_weapon_characteristic strength\">" \
                + str(int_hits) \
                + "x " \
                + str(int_damage) \
                + " st</td></tr>"

        return get_text_html_attack()

    SET_TEXTS_KEYWORDS_INACTIVE = {"attachable", "teleportation"}

    def get_text_html_keywords_model():

        return " " \
            .join(
                map(
                    get_text_html_keyword,
                    filter(
                        lambda text_keyword: text_keyword not in SET_TEXTS_KEYWORDS_INACTIVE,
                        dict_unit \
                            ["keywords"])))

    def get_text_html_model_characteristics():

        return "<div class=\"characteristics_model\"><div class=\"div_model_characteristic div_armor\"><div class=\"div_model_characteristic_name\">Armor</div><div class=\"div_model_characteristic_value\">" \
            + str(dict_unit["armor"]) \
            + "</div></div></div>"

    def get_text_html_inactive_information():

        text_inactive_keywords = "<br/>" \
            .join(
                map(
                    get_text_html_keyword,
                    filter(
                        lambda text_keyword: text_keyword in SET_TEXTS_KEYWORDS_INACTIVE,
                        dict_unit \
                            ["keywords"])))

        if bool_show_inactive_information:
            return "<div class=\"inactive_data\"><span class=\"points_cost\">" \
                + str(
                    dict_unit \
                        ["points_per_model"]) \
                + " points</span><br/><br/>Max health:<span class=\"max_health\">" \
                + str(
                    dict_unit \
                        ["health_points"]) \
                + "</span><br/><br/>" \
                + text_inactive_keywords \
                + "</div>"
        else:
            return ""

    text_html_rows_actions = "\n" \
        .join(
            map(
                get_text_html_row_action,
                dict_unit
                    ["actions"]))

    return "<div class=\"container_unit\"><div class=\"div_unit\"><div class=\"div_header_unit\"><h3 class=\"h3_name_unit\">" \
        + dict_unit \
            ["name"] \
        + "</h3>" \
        + get_text_html_model_characteristics() \
        + "</div><div class=\"div_content_unit\" style=\"background-image: url(resources/" \
        + name_setting \
        + "/general/background.png)\"><div class=\"div_image_unit\" style=\"background-image: url(" \
        + path_image_unit \
        + ")\"><div class=\"model_properties\"><div class=\"model_property keywords\">" \
        + get_text_html_keywords_model() \
        + "</div><div class=\"model_property actions\"><table class=\"table_default fullwidth\"><tbody><tr><th class=\"th_weapon_characteristic range\"><th class=\"th_weapon_characteristic keywords\"></th><th class=\"th_weapon_characteristic strength\"></th></tr>" \
        + text_html_rows_actions \
        + "</tbody></table></div></div></div></div></div>" \
        + get_text_html_inactive_information() \
        + "</div>"

