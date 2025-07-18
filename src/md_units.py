

import typing

from src import md_shared




def get_text_html_unit(
    dict_unit:typing.Dict,
    dict_keywords:typing.Dict,
    text_side:str,
    name_setting:str,
    name_directory_faction:str,
    bool_show_inactive_information:bool):

    def get_text_html_keyword(
        dict_keyword:typing.Dict,
        text_parameters:str):

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
            + dict_keyword \
                ["name"] \
            + "</span> " \
            + text_parameters \
            + "</div>"

    dict_names_keywords_models = dict(
        map(
            lambda dict_keyword: (
                dict_keyword["name"],
                dict_keyword),
            dict_keywords \
                ["keywords_models"]))

    dict_names_keywords_weapons = dict(
        map(
            lambda dict_keyword: (
                dict_keyword["name"],
                dict_keyword),
            dict_keywords \
                ["keywords_weapons"]))

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

        def get_text_weapon_keywords():

            def get_text_html_keyword_weapon(
                text_name_keyword:str):

                return get_text_html_keyword(
                    dict_keyword=dict_names_keywords_weapons \
                        [text_name_keyword],
                    text_parameters="")

            return " " \
                .join(
                    map(
                        get_text_html_keyword_weapon,
                        dict_action \
                            ["keywords"]))

        def get_text_html_attack():

            int_hits = dict_action \
                ["hits"]

            int_damage = dict_action \
                ["strength"]

            return "<tr title=\"" \
                + dict_action \
                    ["name"] \
                + "\"><td class=\"td_weapon_characteristic range\">" \
                + get_text_weapon_range() \
                + "</td><td class=\"td_keywords\">" \
                + get_text_weapon_keywords() \
                + "</td><td class=\"td_weapon_characteristic strength\">" \
                + str(int_hits) \
                + "x " \
                + str(int_damage) \
                + " st</td></tr>"

        return get_text_html_attack()

    text_html_rows_actions = "\n" \
        .join(
            map(
                get_text_html_row_action,
                dict_unit
                    ["actions"]))

    def get_text_html_keyword_model(
        text_keyword:str):

        text_name_keyword, \
        _, \
        text_parameters = text_keyword \
            .partition(" ")

        return get_text_html_keyword(
            dict_keyword=dict_names_keywords_models \
                [text_name_keyword],
            text_parameters=text_parameters)

    def get_text_model_keywords():

        return " " \
            .join(
                map(
                    get_text_html_keyword_model,
                    filter(
                        lambda text_keyword: text_keyword not in {"teleportation"},
                        dict_unit \
                            ["keywords"])))

    def get_text_html_model_characteristics():

        return "<div class=\"characteristics_model\"><div class=\"div_model_characteristic div_armor\"><div class=\"div_model_characteristic_name\">Armor</div><div class=\"div_model_characteristic_value\">" \
            + str(dict_unit["armor"]) \
            + "</div></div><div class=\"div_model_characteristic div_health\"><div class=\"div_model_characteristic_value\">" \
            + str(dict_unit["health_points"]) \
            + "</div><div class=\"div_model_characteristic_name\">HP</div></div></div>"

    def get_text_html_inactive_information():

        def get_text_html_teleportation():

            if "teleportation" in dict_unit["keywords"]:
                return get_text_html_keyword(
                        dict_keyword=dict_names_keywords_models \
                            ["teleportation"],
                        text_parameters="")
            else:
                return ""

        if bool_show_inactive_information:
            return "<div class=\"inactive_data\"><span class=\"points_cost\">" \
                + str(dict_unit \
                    ["points_per_model"]) \
                + " points</span>" \
                + get_text_html_teleportation() \
                + "</div>"
        else:
            return ""

    return "<div class=\"container_unit\"><div class=\"div_unit\"><div class=\"div_header_unit\"><h3 class=\"h3_name_unit\">" \
        + dict_unit \
            ["name"] \
        + "</h3>" \
        + get_text_html_model_characteristics() \
        + "</div><div class=\"div_content_unit\" style=\"background-image: url(resources/" \
        + name_setting \
        + "/general/background.png)\"><div class=\"div_image_unit\"><img class=\"image_unit\" src=\"" \
        + path_image_unit \
        + "\"/></div><div class=\"model_properties\"><div class=\"model_property keywords\">" \
        + get_text_model_keywords() \
        + "</div><div class=\"model_property actions\"><table class=\"table_default fullwidth\"><tbody><tr><th class=\"th_weapon_characteristic range\"><th class=\"th_weapon_characteristic keywords\"></th><th class=\"th_weapon_characteristic strength\"></th></tr>" \
        + text_html_rows_actions \
        + "</tbody></table></div></div></div></div>" \
        + get_text_html_inactive_information() \
        + "</div>"

