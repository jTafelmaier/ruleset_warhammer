

import typing

from src import md_shared




def get_text_html_health_bar(
    dict_unit:typing.Dict,
    text_id:str):

    text_onclick = " onclick=\"reduce_health('" + text_id + "')\"" if text_id is not None else ""

    return "<div class=\"health_bar\"" \
        + text_onclick \
        + "><div class=\"token next\" />" \
        + ("<div class=\"token\" />" \
            * (dict_unit \
                ["health_points"] - 1)) \
        + "</div>"


def get_text_html_unit(
    dict_unit:typing.Dict,
    dict_keywords:typing.Dict,
    name_directory_faction:str,
    bool_show_inactive_information:bool):

    def get_text_html_keywords(
        dict_entity:typing.Dict,
        text_category:str):

        def get_text_html_keyword(
            text_keyword:str):

            text_name_keyword, \
            _, \
            text_parameters = text_keyword \
                .partition(" ")

            return "<div class=\"keyword " \
                + text_category \
                + "\"title=\"" \
                + dict_keywords \
                    [text_category] \
                    [text_name_keyword] \
                + "\"><span>" \
                + text_name_keyword \
                + "</span> " \
                + text_parameters \
                + "</div>"

        return "" \
            .join(
                map(
                    get_text_html_keyword,
                    dict_entity \
                        [text_category]))

    path_image_unit = "/" \
        .join(
            [
                md_shared.get_text_path_images_faction(name_directory_faction),
                "units",
                dict_unit \
                    ["name"] \
                    + ".png"])

    def get_text_html_row_action(
        dict_action:typing.Dict):

        text_hits = str(dict_action["hits"]) + "x " if dict_action["hits"] > 1 else ""

        return "<tr><td class=\"range\">" \
            + dict_action \
                ["range"] \
            + "</td><td class=\"keywords\">" \
            + get_text_html_keywords(
                dict_entity=dict_action,
                text_category="keywords_weapon") \
            + "</td><td class=\"strength\">" \
            + text_hits \
            + "💥" \
            + str(
                dict_action \
                    ["strength"]) \
            + "</td></tr>"

    def get_text_html_inactive_information():

        if not bool_show_inactive_information:
            return ""

        return "<div class=\"inactive_data\"><div>" \
            + get_text_html_health_bar(
                dict_unit=dict_unit,
                text_id=None) \
            + "<div class=\"points_cost\">" \
            + str(
                dict_unit \
                    ["points_per_model"]) \
            + " points</div></div><div class=\"list_building\">" \
            + get_text_html_keywords(
                dict_entity=dict_unit,
                text_category="keywords_deployment") \
            + "</div></div>"

    text_html_rows_actions = "\n" \
        .join(
            map(
                get_text_html_row_action,
                dict_unit
                    ["actions"]))

    return "<div class=\"container_unit\">" \
        + get_text_html_inactive_information() \
        + "<div class=\"unit\" style=\"background-image: url('resources/background.png')\"><div class=\"image_unit\" style=\"background-image: url('" \
        + path_image_unit \
        + "')\"><div class=\"header_unit\"><h3 class=\"name_unit\">" \
        + dict_unit \
            ["name"] \
        + "</h3><div class=\"armor\">⛊" \
        + str(
            dict_unit \
                ["armor"]) \
        + "</div></div><div class=\"model_properties\"><div class=\"model_property keywords\">" \
        + get_text_html_keywords(
            dict_entity=dict_unit,
            text_category="keywords_model") \
        + "</div><div class=\"model_property weapons\"><table class=\"table_default fullwidth\"><tbody><tr><th/><th/><th/></tr>" \
        + text_html_rows_actions \
        + "</tbody></table></div></div></div></div></div>"

