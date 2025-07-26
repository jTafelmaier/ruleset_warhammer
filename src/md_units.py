

import typing

from src import md_shared




def get_text_html_data_unit(
    dict_unit:typing.Dict,
    dict_keywords:typing.Dict,
    name_faction:str):

    def get_text_html_keywords(
        text_category:str):

        def get_text_html_keyword(
            text_keyword:str):

            text_name_keyword, \
            _, \
            text_parameters = text_keyword \
                .partition(" ")

            return "<div class=\"unit_property " \
                + text_name_keyword \
                + "\"title=\"" \
                + dict_keywords \
                    [text_category] \
                    [text_name_keyword] \
                + "\"><span>" \
                + text_name_keyword \
                + "</span> " \
                + text_parameters \
                + "</div>"

        return "<br/>" \
            .join(
                map(
                    get_text_html_keyword,
                    dict_unit \
                        [text_category]))

    path_image_unit = "/" \
        .join(
            [
                md_shared.get_text_path_images_faction(name_faction),
                "units",
                dict_unit \
                    ["name"] \
                    + ".png"])

    def get_text_html_row_action(
        dict_action:typing.Dict):

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

        return "<div class=\"unit_property\"><span>" \
            + dict_action \
                ["range"] \
            + "</span>" \
            + " " \
                .join(
                    dict_action \
                        ["keywords_weapon"]) \
            + " " \
            + str(dict_action["hits"]) \
            + "x 💥" \
            + get_text_strength() \
            + "</div>"

    text_html_rows_actions = "<br/>" \
        .join(
            map(
                get_text_html_row_action,
                dict_unit
                    ["actions"]))

    return "<div class=\"unit\" title=\"" \
        + str(
            dict_unit \
                ["points_per_model"]) \
        + " points per model.\" style=\"background-image: url('resources/background.png')\"><div class=\"image_unit\" style=\"background-image: url('" \
        + path_image_unit \
        + "')\"><div class=\"header_unit\"><div class=\"armor\">⛊" \
        + str(
            dict_unit \
                ["armor"]) \
        + "</div><h3 class=\"name_unit\">" \
        + dict_unit \
            ["name"] \
        + "</h3></div><div class=\"model_properties\"><div class=\"model_property keywords\">" \
        + get_text_html_keywords("keywords_model") \
        + "<br/>" \
        + text_html_rows_actions \
        + "</div></div></div></div>"

