

import typing

from src import md_shared




def get_text_html_data_unit(
    dict_unit:typing.Dict,
    name_faction:str):

    def get_text_keywords(
        list_texts_keywords:typing.List[str]):

        if len(list_texts_keywords) == 0:
            return ""

        return " [" \
            + ", " \
                .join(list_texts_keywords) \
            + "]"

    def get_text_html_attack(
        dict_attack:typing.Dict):

        return "<div class=\"model_property\">" \
            + dict_attack \
                ["hits"] \
                .__str__() \
            + "x 💥" \
            + dict_attack \
                ["strength"] \
                .__str__() \
            + get_text_keywords(
                dict_attack \
                    ["keywords"]) \
            + "</div>"

    path_image_unit = "/" \
        .join(
            [
                md_shared.get_text_path_images_faction(name_faction),
                "units",
                dict_unit \
                    ["name"] \
                    + ".png"])

    text_html_rows_attacks = "" \
        .join(
            map(
                get_text_html_attack,
                dict_unit
                    ["attacks"]))

    return "<div class=\"model\" title=\"" \
        + str(
            dict_unit \
                ["points_per_model"]) \
        + " points per model.\"><div class=\"image_unit\" style=\"background-image: url('" \
        + path_image_unit \
        + "')\"><div class=\"header_unit\"><div class=\"model_properties\"><div class=\"model_property\"><span>⛊</span>" \
        + str(
            dict_unit \
                ["armor"]) \
        + "<span>🡆</span>" \
        + str(
            dict_unit \
                ["move"]) \
        + "</div><span class=\"name_unit\">" \
        + dict_unit \
            ["name"] \
        + "</span></div><div class=\"model_keywords\">" \
        + get_text_keywords( \
            dict_unit \
                ["keywords"]) \
        + "</div></div><div class=\"model_attacks\">" \
        + text_html_rows_attacks \
        + "</div></div></div>"

