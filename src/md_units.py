

import copy
import itertools
import typing

from src import md_shared




DICT_DESCRIPTIONS_ACTIONS = {
    "scan": "This model can perform the &quot;Scan&quot; action.",
    "move": "This model can perform the &quot;Move&quot; action.",
    "attack": "This model can perform the &quot;Attack&quot; action."}


def get_text_html_action(
    dict_action:typing.Dict):

    text_type_action = dict_action \
        ["type"]

    def get_text_content():

        if text_type_action != "attack":
            return "<span>" \
                + text_type_action \
                + "</span> " \
                + dict_action \
                    ["parameters"]

        def get_text_keywords():

            if len(dict_action["keywords"]) == 0:
                return ""

            return " [" \
                + " " \
                    .join(
                        dict_action \
                            ["keywords"]) \
                + "]"

        return "<span>⚔</span>" \
            + dict_action \
                ["hits"] \
                .__str__() \
            + "x 💥" \
            + dict_action \
                ["strength"] \
                .__str__() \
            + get_text_keywords()

    return "<div class=\"unit_property" \
        + (" revealable variation invisible" if dict_action["is_variation"] else "") \
        + (" revealable" if dict_action["to_replace"] else "") \
        + "\" title=\"" \
        + DICT_DESCRIPTIONS_ACTIONS \
            [text_type_action] \
        + "\">" \
        + get_text_content() \
        + "</div>"


def get_text_html_data_unit(
    dict_unit:typing.Dict,
    name_faction:str,
    index_chosen_variation:typing.Optional[int] = None):

    path_image_unit = "/" \
        .join(
            [
                md_shared.get_text_path_images_faction(name_faction),
                "units",
                dict_unit \
                    ["name"] \
                    + ".png"])

    def get_dict_chosen_variation():

        if index_chosen_variation is None:
            return {
                "replace_ids": [],
                "actions_gained": []}
        else:
            return dict_unit \
                ["variations"] \
                [index_chosen_variation]

    dict_chosen_variation = get_dict_chosen_variation()

    def get_tuple_sorting(
        dict_action:typing.Dict):

        int_key_1 = list(
                DICT_DESCRIPTIONS_ACTIONS \
                    .keys()) \
            .index(dict_action["type"])

        if dict_action["type"] != "attack":
            return (
                int_key_1,
                0,
                0)

        return (
            int_key_1,
            dict_action \
                ["type"],
            len(
                dict_action \
                    ["keywords"]))

    def get_dict_action(
        pair_action:typing.Tuple[int, typing.Dict]):

        index_action, \
        dict_action = pair_action

        dict_action_copy = copy.copy(dict_action)

        dict_action_copy["is_variation"] = False
        dict_action_copy["to_replace"] = index_action in dict_chosen_variation["replace_ids"]

        return dict_action_copy

    list_dicts_actions = list(
        map(
            get_dict_action,
            enumerate(
                dict_unit
                    ["actions"])))

    def get_dict_action_copy(
        dict_action:typing.Dict):

        dict_action_copy = copy.copy(dict_action)

        dict_action_copy["is_variation"] = True
        dict_action_copy["to_replace"] = False

        return dict_action_copy

    text_html_rows_actions = "" \
        .join(
            map(
                get_text_html_action,
                sorted(
                    list(
                        map(
                            get_dict_action_copy,
                            dict_chosen_variation \
                                ["actions_gained"])) \
                        + list_dicts_actions,
                    key=get_tuple_sorting)))

    def get_text_html_armor():

        def get_text_keywords():

            if len(dict_unit["keywords"]) == 0:
                return ""

            return " [" \
                + ", " \
                    .join(
                        dict_unit \
                            ["keywords"]) \
                + "]"

        return "<div class=\"unit_property\"><span>⛊</span>" \
            + str(
                    dict_unit \
                        ["armor"]) \
            + get_text_keywords() \
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

