

import typing

from src import md_units
from src import md_shared




def get_text_html_army_lists(
    list_dicts_factions:typing.List[typing.Dict]):

    dict_army_lists = md_shared.get_dict_setting("army_lists.json")

    def get_html_army_list(
        text_side:str):

        dict_army_list = dict_army_lists \
            [text_side]

        name_faction = dict_army_list \
            ["faction"]

        dict_faction = next(
                filter(
                    lambda dict_faction: dict_faction["name"] == name_faction,
                    list_dicts_factions))

        dict_units = dict(
                map(
                    lambda dict_unit: (
                        dict_unit \
                            ["name"],
                        dict_unit),
                    dict_faction \
                        ["units"]))

        def get_text_html_unit(
            pair_dict_unit_army_list:typing.Tuple[int, typing.Dict]):

            int_index_unit, \
            dict_unit_army_list = pair_dict_unit_army_list

            dict_unit = dict_units \
                [
                    dict_unit_army_list \
                        ["name"]]

            text_parameters_functions = "'" \
                + text_side \
                + "', " \
                + str(int_index_unit)

            text_count_models = str(
                dict_unit_army_list \
                    ["count_models"])

            return "<div class=\"unit_army_list\" points_per_model=\"" \
                + str(dict_unit["points_per_model"]) \
                + "\"><div class=\"unit_state\"><div class=\"count_models\" onclick=\"decrease_count_models(" \
                + text_parameters_functions \
                + ")\">" \
                + text_count_models \
                + "x</div><div class=\"health_bar\">" \
                + ("<div class=\"token\" />" \
                    * 8) \
                + "</div></div><div onclick=\"set_inactive(" \
                + text_parameters_functions \
                + ")\">" \
                + md_units.get_text_html_data_unit(
                    dict_unit=dict_unit,
                    name_faction=name_faction) \
                + "</div></div>"

        return "<div id=\"" \
            + text_side \
            + "\"><div class=\"victory_state\"></div><div class=\"army_list\">" \
            + "" \
                .join(
                    map(
                        get_text_html_unit,
                        enumerate(
                            dict_army_list \
                                ["units"]))) \
            + "</div></div>"

    return get_html_army_list("left") \
        + get_html_army_list("right")

