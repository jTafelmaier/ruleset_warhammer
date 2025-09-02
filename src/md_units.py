

import typing

from src import md_shared




def get_text_html_data_unit(
    dict_unit:typing.Dict,
    name_faction:str,
    list_indices_enhancements:typing.List[int] = [],
    bool_show_invisible_enhancements = False):

    DICT_DESCRIPTIONS_ACTIONS = {
        "scan": "This model can perform the &quot;Scan&quot; action.",
        "score": "This model's unit can perform the &quot;Score objective&quot; action.\nFurthermore, this unit can be attached to another friendly unit at deployment, if that unit does not have a higher armor characteristic than this unit. While this unit is attached to another unit, it cannot be selected as a target unit.",
        "move": "This model can perform the &quot;Move&quot; action.",
        "teleportation": "This model's unit can perform the &quot;Setup teleportation&quot; and &quot;Recall&quot; actions.",
        "weapon": "This model can perform the &quot;Attack&quot; action."}

    def get_text_html_action(
        dict_action:typing.Dict):

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
                        ("[20 cm]" if dict_weapon["range"] == 20 else None),
                        ("[heavy]" if dict_weapon["heavy"] else None)]))

            return "<span>" \
                + ("⚔" if dict_weapon["range"] == 5 else "𖦏") \
                + "</span>" \
                + dict_weapon \
                    ["hits"] \
                    .__str__() \
                + "x💥" \
                + dict_weapon \
                    ["strength"] \
                    .__str__() \
                + " " \
                + " " \
                    .join(list_texts_keywords)

        return "<div class=\"unit_property" \
            + (" enhancement" if dict_action.get("is_enhancement", False) else "") \
            + (" revealable invisible" if not dict_action.get("is_visible", True) and not bool_show_invisible_enhancements else "") \
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

    def get_dict_enhancement(
        index:int):

        dict_enhancement = dict_unit \
            ["enhancements"] \
            [index]

        dict_enhancement["is_enhancement"] = True

        return dict_enhancement

    list_dicts_enhancements = list(
        map(
            get_dict_enhancement,
            list_indices_enhancements))

    def get_tuple_sorting(
        dict_action:typing.Dict):

        int_key_1 = list(
                DICT_DESCRIPTIONS_ACTIONS \
                    .keys()) \
            .index(dict_action["type"])

        if dict_action["type"] != "weapon":
            return (
                int_key_1,
                0,
                0)

        dict_data = dict_action \
            ["data"]

        return (
            int_key_1,
            dict_data \
                ["range"],
            dict_data \
                ["heavy"])

    text_html_rows_actions = "" \
        .join(
            map(
                get_text_html_action,
                sorted(
                    list_dicts_enhancements \
                        + dict_unit
                            ["actions"],
                    key=get_tuple_sorting)))

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

