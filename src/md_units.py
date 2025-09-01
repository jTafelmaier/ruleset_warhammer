

import typing

from src import md_shared




def get_text_style_visible(
    bool_visible:bool):

    if bool_visible:
        return ""
    else:
        return " style=\"display: none;\""


def get_text_html_action(
    text_action:str,
    dict_actions:typing.Dict,
    bool_visible:bool = True):

    text_name_action, \
    _, \
    text_parameters = text_action \
        .partition(" ")

    return "<div class=\"unit_property " \
        + text_name_action \
        + "\" title=\"" \
        + dict_actions \
            [text_name_action] \
        + "\"" \
        + get_text_style_visible(bool_visible) \
        + "><span>" \
        + text_name_action \
        + "</span> " \
        + text_parameters \
        + "</div>"


def get_text_html_row_weapon(
    dict_weapon:typing.Dict,
    bool_visible:bool = True):

    list_texts_keywords = list(
        filter(
            lambda text: text is not None,
            [
                (dict_weapon["range"] if dict_weapon["range"] != "rn" else None),
                ("heavy" if dict_weapon["heavy"] else None),
                ("single" if dict_weapon["single"] else None)]))

    return "<div class=\"unit_property attack\"" \
        + get_text_style_visible(bool_visible) \
        + "><span>⚔</span>🗲" \
        + str(dict_weapon["ap"]) \
        + " 💥" \
        + str(dict_weapon["damage"]) \
        + " [" \
        + ", " \
            .join(list_texts_keywords) \
        + "]</div>"


def get_text_html_data_unit(
    dict_unit:typing.Dict,
    dict_actions:typing.Dict,
    name_faction:str,
    list_names_enhancements:typing.List[str] = []):

    list_dicts_enhancements = list(
        filter(
            lambda dict_enhancement: dict_enhancement["name"] in list_names_enhancements,
            dict_unit \
                ["enhancements"]))

    list_texts_rows_actions_enhancements = list(
        map(
            lambda dict_enhancement: get_text_html_action(
                text_action=dict_enhancement \
                    ["data"] \
                    ["name"],
                dict_actions=dict_actions,
                bool_visible=dict_enhancement \
                    ["visible"]),
            filter(
                lambda dict_enhancement: dict_enhancement["type"] == "action",
                list_dicts_enhancements)))

    list_texts_rows_weapons_enhancements = list(
        map(
            lambda dict_enhancement: get_text_html_row_weapon(
                dict_weapon=dict_enhancement \
                    ["data"],
                bool_visible=dict_enhancement \
                    ["visible"]),
            filter(
                lambda dict_enhancement: dict_enhancement["type"] == "weapon",
                list_dicts_enhancements)))

    path_image_unit = "/" \
        .join(
            [
                md_shared.get_text_path_images_faction(name_faction),
                "units",
                dict_unit \
                    ["name"] \
                    + ".png"])

    text_html_rows_actions = "<br/>" \
        .join(
            list(
                map(
                    lambda text_action: get_text_html_action(
                        text_action=text_action,
                        dict_actions=dict_actions),
                    dict_unit \
                        ["actions"])) \
            + list_texts_rows_actions_enhancements)

    text_html_rows_weapons = "<br/>" \
        .join(
            list(
                map(
                    get_text_html_row_weapon,
                    dict_unit
                        ["weapons"])) \
            + list_texts_rows_weapons_enhancements)

    def get_text_html_armor():

        list_dicts_enhancements_armor = list(
            filter(
                lambda dict_enhancement: dict_enhancement["type"] == "armor",
                list_dicts_enhancements))

        if len(list_dicts_enhancements_armor) > 0:
            return "<div class=\"unit_property replaceable_by_enhancement\"><span>⛊</span>" \
                + str(
                    dict_unit \
                        ["armor"]) \
                + "</div><div class=\"unit_property enhanced\"" \
                + get_text_style_visible(
                    list_dicts_enhancements_armor \
                        [0] \
                        ["visible"]) \
                + "><span>⛊</span>" \
                + str(
                    list_dicts_enhancements_armor \
                        [0] \
                        ["data"] \
                        ["value"]) \
                + "</div>"

        return "<div class=\"unit_property\"><span>⛊</span>" \
            + str(
                    dict_unit \
                        ["armor"]) \
            + "</div>"

    return "<div class=\"unit\" title=\"" \
        + str(
            dict_unit \
                ["points_per_model"]) \
        + " points per model.\"><div class=\"image_unit\" style=\"background-image: url('" \
        + path_image_unit \
        + "')\"><div class=\"header_unit\">" \
        + get_text_html_armor() \
        + "<h3 class=\"name_unit\">" \
        + dict_unit \
            ["name"] \
        + "</h3></div><div class=\"model_properties\"><br/>" \
        + text_html_rows_actions \
        + "<br/>" \
        + text_html_rows_weapons \
        + "</div></div></div>"

