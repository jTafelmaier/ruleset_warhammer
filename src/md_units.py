

import typing

from src import md_shared




def get_text_html_data_unit(
    dict_unit:typing.Dict,
    name_faction:str):

    def get_text_keywords(
        list_texts_keywords:typing.List[str]):

        if len(list_texts_keywords) == 0:
            return ""

        return "" \
            .join(
                map(
                    lambda text_keyword:  "<span class=\"keyword\">" + text_keyword + "</span>",
                    list_texts_keywords))

    def get_text_html_attack(
        dict_attack:typing.Dict):

        def get_text_icon_range():

            if dict_attack["range"] == 5:
                return "⚔"
            elif dict_attack["range"] == 20:
                return "⛶"
            else:
                return "⊹"

        return "<tr class=\"model_property\"><td class=\"attack\">" \
            + get_text_icon_range() \
            + "</td><td class=\"property\">" \
            + str(
                dict_attack \
                    ["hits"]) \
            + "x " \
            + dict_attack \
                ["strength"] \
                .__str__() \
            + "</td></tr>"

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
        + "')\"><div class=\"name_unit\">" \
        + dict_unit \
            ["name"] \
        + "</div><table class=\"data_unit\"><tbody><tr class=\"model_property\"><td class=\"icon\">⛊</td><td class=\"property\">" \
        + str(
            dict_unit \
                ["armor"]) \
        + " " \
        + get_text_keywords( \
            dict_unit \
                ["keywords_armor"]) \
        + "</td></tr><tr class=\"model_property\"><td class=\"icon\">🡆</td><td class=\"property\">" \
        + str(
            dict_unit \
                ["move"]) \
        + " " \
        + get_text_keywords( \
            dict_unit \
                ["keywords_movement"]) \
        + "</td></tr>" \
        + text_html_rows_attacks \
        + "</tbody></table></div></div>"

