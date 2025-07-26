

import itertools
import typing

from src import md_shared
from src import md_units




def get_text_html_army_lists(
    list_dicts_factions:typing.List[typing.Dict],
    dict_keywords:typing.Dict,
    dict_army_list_left:typing.Dict,
    dict_army_list_right:typing.Dict):

    def get_list_htmls_army_list(
        dict_army_list:typing.Dict,
        text_side:str):

        name_faction = dict_army_list \
            ["faction"]

        list_units_army_list = dict_army_list \
            ["units"]

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

        text_html_victory_state = "<div class=\"victory_state " \
            + text_side \
            + "\"><div class=\"victory_points\"><span onclick=\"increase_victory_points('" \
            + text_side \
            + "')\">0</span><span onclick=\"decrease_victory_points('" \
            + text_side \
            + "')\"> VP</span></div>,<span class=\"points_total\">? points remaining.</span></div>"

        name_faction = dict_faction \
            ["name"]

        name_directory_faction = md_shared.get_text_name_directory_faction(name_faction)

        def get_text_html_unit(
            pair_dict_unit_army_list:typing.Tuple[int, typing.Dict]):

            int_index_unit, \
            dict_unit_army_list = pair_dict_unit_army_list

            text_name_unit = dict_unit_army_list \
                ["name"]

            dict_unit = dict_units \
                [text_name_unit]

            text_parameters_functions = "'" \
                + text_side \
                + "', " \
                + str(int_index_unit)

            text_html_data_unit = md_units.get_text_html_data_unit(
                    dict_unit=dict_unit,
                    dict_keywords=dict_keywords,
                    name_directory_faction=name_directory_faction)

            return "<div class=\"unit_army_list\" points_per_model=\"" \
                + str(dict_unit["points_per_model"]) \
                + "\"><div class=\"unit_state\"><div class=\"health_bar\" onclick=\"reduce_health(" \
                + text_parameters_functions \
                + ")\"><div class=\"token next\" />" \
                + ("<div class=\"token\" />" \
                    * 7) \
                + "</div><div class=\"count_models\" initial=\"" \
                + str(
                    dict_unit_army_list \
                        ["count_models"]) \
                + "\" onclick=\"increase_number_models(" \
                + text_parameters_functions \
                + ")\">" \
                + str(
                    dict_unit_army_list \
                        ["count_models"]) \
                + "</div></div><div onclick=\"toggle_inactive(" \
                + text_parameters_functions \
                + ")\">" \
                + text_html_data_unit \
                + "</div></div>"

        text_html_units_individual = "" \
            .join(
                map(
                    get_text_html_unit,
                    enumerate(
                        list_units_army_list)))

        text_html_units = "<div class=\"army_list " \
            + text_side \
            + "\">" \
            + text_html_units_individual \
            + "</div>"

        return [
            text_html_victory_state,
            text_html_units]

    list_texts_html_army_list_left = get_list_htmls_army_list(
            dict_army_list=dict_army_list_left,
            text_side="left")

    list_texts_html_army_list_right = get_list_htmls_army_list(
            dict_army_list=dict_army_list_right,
            text_side="right")

    # TODO refactor
    return "" \
        .join(
            itertools.chain(
                *
                    zip(
                        list_texts_html_army_list_left,
                        list_texts_html_army_list_right)))

