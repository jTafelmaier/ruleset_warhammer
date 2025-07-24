

import typing

from src import md_shared




def get_text_html_keywords(
    dict_entity:typing.Dict,
    dict_keywords:typing.Dict,
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


def get_text_html_unit(
    dict_unit:typing.Dict,
    dict_keywords:typing.Dict,
    name_directory_faction:str):

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

        def get_text_strength():

            if dict_action["strength_lower"] == dict_action["strength_upper"]:
                return str(dict_action["strength_lower"])
            else:
                return str(
                        dict_action \
                            ["strength_lower"]) \
                    + " - " \
                    + str(
                        dict_action \
                            ["strength_upper"])

        return "<tr><td class=\"range\">" \
            + dict_action \
                ["range"] \
            + "</td><td class=\"keywords\">" \
            + get_text_html_keywords(
                dict_entity=dict_action,
                dict_keywords=dict_keywords,
                text_category="keywords_weapon") \
            + "</td><td class=\"strength\">" \
            + text_hits \
            + "💥" \
            + get_text_strength() \
            + "</td></tr>"

    text_html_rows_actions = "\n" \
        .join(
            map(
                get_text_html_row_action,
                dict_unit
                    ["actions"]))

    return "<div class=\"unit\" style=\"background-image: url('resources/background.png')\"><div class=\"image_unit\" style=\"background-image: url('" \
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
            dict_keywords=dict_keywords,
            text_category="keywords_model") \
        + "</div><div class=\"model_property weapons\"><table class=\"table_default fullwidth\"><tbody><tr><th/><th/><th/></tr>" \
        + text_html_rows_actions \
        + "</tbody></table></div></div></div></div>"

