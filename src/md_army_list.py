

import typing

from src import md_units
from src import md_shared




def get_text_html_army_lists(
    list_dicts_factions:typing.List[typing.Dict],
    dict_actions:typing.Dict):

    def get_html_army_list(
        text_side:str):

        dict_army_list = md_shared.get_dict_setting("army_list_" + text_side + ".json")

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
                + "\"><div class=\"unit_state\"><div class=\"health_bar\">" \
                + ("<div class=\"token\" />" \
                    * 8) \
                + "</div><div class=\"count_models\"><div class=\"increase\" onclick=\"update_count_models(" \
                + text_parameters_functions \
                + ", true)\">▲</div><div class=\"count_current\" initial=\"" \
                + text_count_models \
                + "\">" \
                + text_count_models \
                + "</div><div class=\"decrease\" onclick=\"update_count_models(" \
                + text_parameters_functions \
                + ", false)\">▼</div></div></div><div onclick=\"toggle_inactive(" \
                + text_parameters_functions \
                + ")\">" \
                + md_units.get_text_html_data_unit(
                    dict_unit=dict_unit,
                    dict_actions=dict_actions,
                    name_faction=name_faction) \
                + "</div></div>"

        return "<div class=\"" \
            + text_side \
            + "\"><div class=\"victory_state\"><div class=\"victory_points\"><span class=\"value\" onclick=\"update_victory_points('" \
            + text_side \
            + "', true)\">0</span><span onclick=\"update_victory_points('" \
            + text_side \
            + "', false)\"> VP,</span></div><div class=\"model_points\"><span class=\"value\">?</span>points remaining. -></div><span class=\"outcome\"></span></div><div class=\"army_list\">" \
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

