

import itertools
import typing

from lib.unary import _dicts
from lib.unary import _iters

from src import md_shared
from src import md_units




def get_text_html_army_lists(
    dict_factions:typing.Dict,
    dict_keywords:typing.Dict,
    name_setting:str,
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
                    dict_factions \
                        >> _dicts.to_iterable_values() \
                        >> _iters.to_iterable_chained()))

        dict_units = dict(
                map(
                    lambda dict_unit: (
                        dict_unit \
                            ["name"],
                        dict_unit),
                    dict_faction \
                        ["units"]))

        def get_points_cost_unit(
            dict_unit_army_list:typing.Dict):

            return dict_unit_army_list \
                ["count_models"] \
                * dict_units \
                    [
                        dict_unit_army_list \
                            ["name"]] \
                    ["points_per_model"]

        def get_text_html_tr_unit(
            pair_dict_unit_army_list:typing.Tuple[int, typing.Dict]):

            int_index_unit, \
            dict_unit_army_list = pair_dict_unit_army_list

            text_name_unit = dict_unit_army_list \
                ["name"]

            dict_unit = dict_units \
                [text_name_unit]

            text_teleportation = "(t) " if "teleportation" in dict_unit["keywords"] else ""

            text_id_row = "army_list_tr_" \
                + text_side \
                + "_" \
                + str(int_index_unit)

            def get_text_html_health_bar():

                return "<div class=\"health_bar\" onclick=\"reduce_health('" \
                    + text_id_row \
                    + "')\">" \
                    + ("<div class=\"token\" />" \
                        * dict_unit \
                            ["health_points"]) \
                    + "</div>"

            def get_text_html_action_tokens():

                if dict_unit_army_list["attached_to_index"] is not None:
                    return "attached"

                return "<div class=\"action_tokens\" onclick=\"reduce_action_tokens('" \
                    + text_id_row \
                    + "')\">" \
                    + ("<div class=\"action_token token\">AT</div>" \
                        * 2) \
                    + "</div>"

            return "<tr id=\"" \
                + text_id_row \
                + "\" points_per_model=\"" \
                + str(
                    dict_unit \
                        ["points_per_model"]) \
                + "\"><td>" \
                + get_text_html_health_bar() \
                + "</td><td>" \
                + get_text_html_action_tokens() \
                + "</td><td>" \
                + text_teleportation \
                + text_name_unit \
                + "</td><td class=\"count_models\" initial=\"" \
                + str(
                    dict_unit_army_list \
                        ["count_models"]) \
                + "\" onclick=\"increase_number_models('" \
                + text_id_row \
                + "')\">" \
                + str(
                    dict_unit_army_list \
                        ["count_models"]) \
                + "</td><td class=\"points_cost\">" \
                + str(
                    get_points_cost_unit(dict_unit_army_list)) \
                + "</td><td/></tr>"

        text_html_trs_units = "" \
            .join(
                map(
                    get_text_html_tr_unit,
                    enumerate(
                        list_units_army_list)))

        int_total_points = sum(
                map(
                    get_points_cost_unit,
                    list_units_army_list))

        text_html_army_list = "<div class=\"army_list " \
            + text_side \
            + "\"><table class=\"table_default fullwidth\"><tbody><tr><th>Health</th><th>Action tokens</th><th>Unit</th><th>#models</th><th class=\"points_total\">Points (" \
            + str(int_total_points) \
            + " total)</th><th><span class=\"victory_points\" onclick=\"increase_victory_points('" \
            + text_side \
            + "')\">0</span><span onclick=\"decrease_victory_points('" \
            + text_side \
            + "')\">VP</span></th></tr>" \
            + text_html_trs_units \
            + "</tbody></table></div>"

        name_faction = dict_faction \
            ["name"]

        name_directory_faction = md_shared.get_text_name_directory_faction(name_faction)

        def get_text_html_unit(
            dict_unit:typing.Dict):

            return md_units.get_text_html_unit(
                    dict_unit=dict_unit,
                    dict_keywords=dict_keywords,
                    name_setting=name_setting,
                    name_directory_faction=name_directory_faction,
                    bool_show_inactive_information=False)

        set_names_units_in_army_list = set(
                map(
                    lambda dict_unit_army_list: dict_unit_army_list["name"],
                    list_units_army_list))

        text_html_units_individual = "" \
            .join(
                map(
                    get_text_html_unit,
                    filter(
                        lambda dict_unit: dict_unit["name"] in set_names_units_in_army_list,
                        dict_faction \
                            ["units"])))

        text_html_units = "<div>" \
            + text_html_units_individual \
            + "</div>"

        return [
            text_html_army_list,
            text_html_units]

    list_texts_html_army_list_left = get_list_htmls_army_list(
            dict_army_list=dict_army_list_left,
            text_side="left")

    list_texts_html_army_list_right = get_list_htmls_army_list(
            dict_army_list=dict_army_list_right,
            text_side="right")

    return "" \
        .join(
            itertools.chain(
                *
                    zip(
                        list_texts_html_army_list_left,
                        list_texts_html_army_list_right)))

