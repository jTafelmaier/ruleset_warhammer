

import itertools
import typing

from lib.unary import _dicts
from lib.unary import _iters

from src import md_shared
from src import md_units




def get_text_html_army_lists(
    dict_factions:typing.Dict,
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

            text_parameters_functions = "'" \
                + text_side \
                + "', " \
                + str(int_index_unit + 1)

            def get_text_html_action_tokens():

                if dict_unit_army_list["attached_to_index"] is not None:
                    return "attached"

                text_token_brace = "<div class=\"action_token brace token\">BT</div>" if "large" not in dict_unit["keywords_model"] else ""

                return "<div class=\"action_tokens\" onclick=\"reduce_action_tokens(" \
                    + text_parameters_functions \
                    + ")\"><div class=\"action_token token\">AT</div>" \
                    + text_token_brace \
                    + "</div>"

            return "<tr points_per_model=\"" \
                + str(
                    dict_unit \
                        ["points_per_model"]) \
                + "\"><td><div class=\"health_bar\" onclick=\"reduce_health(" \
                + text_parameters_functions \
                + ")\"><div class=\"token next\" />" \
                + ("<div class=\"token\" />" \
                    * 7) \
                + "</div></td><td>" \
                + get_text_html_action_tokens() \
                + "</td><td>" \
                + text_name_unit \
                + "</td><td class=\"count_models\" initial=\"" \
                + str(
                    dict_unit_army_list \
                        ["count_models"]) \
                + "\" onclick=\"increase_number_models(" \
                + text_parameters_functions \
                + ")\">" \
                + str(
                    dict_unit_army_list \
                        ["count_models"]) \
                + "</td><td class=\"points_cost\">" \
                + str(
                    get_points_cost_unit(dict_unit_army_list)) \
                + "</td></tr>"

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

        text_html_victory_state = "<div class=\"victory_state " \
            + text_side \
            + "\"><div class=\"victory_points\"><span onclick=\"increase_victory_points('" \
            + text_side \
            + "')\">0</span><span onclick=\"decrease_victory_points('" \
            + text_side \
            + "')\"> VP</span></div>,<span class=\"points_total\">" \
            + str(int_total_points) \
            + " points remaining.</span></div>"

        text_html_army_list = "<div class=\"army_list " \
            + text_side \
            + "\"><table class=\"table_default fullwidth\"><tbody><tr><th>Health</th><th>AT</th><th>Unit</th><th>#</th><th class=\"points\">Points</th></tr>" \
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
                    name_directory_faction=name_directory_faction)

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
            text_html_victory_state,
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

