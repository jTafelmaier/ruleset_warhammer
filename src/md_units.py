

import typing

from src import md_shared




def get_text_html_data_unit(
    dict_unit:typing.Dict,
    dict_actions:typing.Dict,
    name_faction:str):

    def get_text_html_action(
        text_action:str):

        text_name_action, \
        _, \
        text_parameters = text_action \
            .partition(" ")

        return "<div class=\"unit_property " \
            + text_name_action \
            + "\"title=\"" \
            + dict_actions \
                [text_name_action] \
            + "\"><span>" \
            + text_name_action \
            + "</span> " \
            + text_parameters \
            + "</div>"

    path_image_unit = "/" \
        .join(
            [
                md_shared.get_text_path_images_faction(name_faction),
                "units",
                dict_unit \
                    ["name"] \
                    + ".png"])

    def get_text_html_row_weapon(
        dict_action:typing.Dict):

        return "<div class=\"unit_property attack\"><span>⚔</span>" \
            + ("heavy " if dict_action["heavy"] else "") \
            + (dict_action["range"] + " " if dict_action["range"] != "rn" else "") \
            + str(dict_action["hits"]) \
            + "x 💥" \
            + str(dict_action["strength"]) \
            + "</div>"

    text_html_rows_actions = "<br/>" \
        .join(
            map(
                get_text_html_row_weapon,
                dict_unit
                    ["weapons"]))

    return "<div class=\"unit\" title=\"" \
        + str(
            dict_unit \
                ["points_per_model"]) \
        + " points per model.\"><div class=\"image_unit\" style=\"background-image: url('" \
        + path_image_unit \
        + "')\"><div class=\"header_unit\"><div class=\"unit_property\"><span>⛊</span>" \
        + str(
            dict_unit \
                ["armor"]) \
        + "</div><h3 class=\"name_unit\">" \
        + dict_unit \
            ["name"] \
        + "</h3></div><div class=\"model_properties\"><br/>" \
        + "<br/>" \
            .join(
                map(
                    get_text_html_action,
                    dict_unit \
                        ["actions"])) \
        + "<br/>" \
        + text_html_rows_actions \
        + "</div></div></div>"

