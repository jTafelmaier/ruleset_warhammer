

import typing

from src import md_shared




def get_text_html_data_unit(
    dict_unit:typing.Dict,
    name_faction:str,
    list_indices_enhancements:typing.List[int] = [],
    bool_show_invisible_enhancements = False):

    DICT_DESCRIPTIONS_ACTIONS = {
        "teleportation": "This model's unit can perform the &quot;Setup teleportation&quot; and &quot;Recall&quot; actions.",
        "move": "This model can perform the &quot;Move&quot; action.",
        "scan": "This model can perform the &quot;Scan&quot; action.",
        "score": "This model's unit can perform the &quot;Score objective&quot; action.\nFurthermore, this unit can be attached to another friendly unit at deployment, if that unit does not have a higher armor characteristic than this unit. While this unit is attached to another unit, it cannot be selected as a target unit.",
        "weapon": "This model can perform the &quot;Attack&quot; action."}

    def get_text_html_action(
        pair_action:typing.Tuple[int, typing.Dict]):

        dict_action = pair_action \
            [-1]

        text_type_action = dict_action \
            ["type"]

        def get_text_content():

            if text_type_action != "weapon":
                return "<span>" \
                    + dict_action \
                        ["type"] \
                    + "</span> " \
                    + dict_action \
                        ["data"] \
                        ["parameters"]

            dict_weapon = dict_action \
                ["data"]

            list_texts_keywords = list(
                filter(
                    lambda text: text is not None,
                    [
                        (dict_weapon["range"] if dict_weapon["range"] != "rn" else None),
                        ("heavy" if dict_weapon["heavy"] else None)]))

            return "<span>⚔</span>" \
                + dict_weapon \
                    ["hits"] \
                    .__str__() \
                + "x💥" \
                + dict_weapon \
                    ["strength"] \
                    .__str__() \
                + " [" \
                + ", " \
                    .join(list_texts_keywords) \
                + "]"

        return "<div class=\"unit_property" \
            + (" enhancement" if dict_action["is_enhancement"] else "") \
            + (" revealable invisible" if dict_action["is_enhancement"] and not dict_action["is_visible"] and not bool_show_invisible_enhancements else "") \
            + "\" title=\"" \
            + DICT_DESCRIPTIONS_ACTIONS \
                [text_type_action] \
            + "\">" \
            + get_text_content() \
            + "</div>"

    path_image_unit = "/" \
        .join(
            [
                md_shared.get_text_path_images_faction(name_faction),
                "units",
                dict_unit \
                    ["name"] \
                    + ".png"])

    text_html_rows_actions = "" \
        .join(
            map(
                get_text_html_action,
                filter(
                    lambda pair_action: not pair_action[-1]["is_enhancement"] or pair_action[0] in list_indices_enhancements,
                    enumerate(
                        dict_unit
                            ["actions"]))))

    def get_text_html_armor():

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
        + "</h3></div><div class=\"model_properties\">" \
        + text_html_rows_actions \
        + "</div></div></div>"

