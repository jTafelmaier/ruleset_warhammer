

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

        # TODO catch error if not found
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

            dict_unit = dict_units \
                [dict_unit_army_list \
                    ["name"]]

            text_name_unit = dict_unit_army_list \
                ["name"]

            text_teleportation = "(t) " if "teleportation" in dict_unit["keywords"] else ""

            def get_text_html_action_tokens():

                def get_text_html_action_token(
                    key_index:str):

                    key_action_token = "action_token_" \
                        + text_side \
                        + "_" \
                        + str(int_index_unit) \
                        + "_" \
                        + key_index

                    return "<div id=\"" \
                        + key_action_token \
                        + "\" class=\"action_token toggleable\" onclick=\"toggle_token('" \
                        + key_action_token \
                        + "')\">AT</div>"

                if dict_unit_army_list["attached_to_index"] is not None:
                    return "attached"
                else:
                    return get_text_html_action_token("a") \
                        + get_text_html_action_token("b")

            def get_text_html_health_tokens():

                def get_text_health_token(
                    int_index_token:int):

                    # TODO re-implement as counter
                    # TODO make health bar size dynamic to cover area
                    key_health_token = "health_token_" \
                        + text_side \
                        + "_" \
                        + str(int_index_unit) \
                        + "_" \
                        + str(int_index_token)

                    return "<div id=\"" \
                        + key_health_token \
                        + "\" class=\"health_token toggleable\" onclick=\"toggle_token('" \
                        + key_health_token \
                        + "')\"></div>"

                return "" \
                    .join(
                        map(
                            get_text_health_token,
                            range(
                                dict_unit \
                                    ["health_points"])))

            text_id_row = "army_list_tr_" \
                + text_side \
                + "_" \
                + str(int_index_unit)

            return "<tr id=\"" \
                + text_id_row \
                + "\"><td>" \
                + get_text_html_action_tokens() \
                + "</td><td>" \
                + text_teleportation \
                + text_name_unit \
                + "</td><td>" \
                + str(
                        dict_unit_army_list \
                            ["count_models"]) \
                + "</td><td><div class=\"health_bar\">" \
                + get_text_html_health_tokens() \
                + "</div></td><td>" \
                + str(
                    get_points_cost_unit(dict_unit_army_list)) \
                + "</td><td><div class=\"button_destroy_unit\" onclick=\"destroy_unit('" \
                + text_id_row \
                + "')\">❌</div></td></tr>"

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

        text_html_army_list = "<div class=\"army_list\"><table class=\"table_default fullwidth\"><tbody><tr><th>Action tokens</th><th>Unit</th><th>#models</th><th>Health</th><th>Points (" \
            + str(int_total_points) \
            + " total)</th><th/></tr>" \
            + text_html_trs_units \
            + "</tbody></table></div>"

        name_faction = dict_faction \
            ["name"]

        name_directory_faction = md_shared.get_text_name_directory_faction(name_faction)

        set_names_units_in_army_list = set(
                map(
                    lambda dict_unit_army_list: dict_unit_army_list["name"],
                    list_units_army_list))

        def get_text_html_unit(
            dict_unit:typing.Dict):
            
            return md_units.get_text_html_unit(
                    dict_unit=dict_unit,
                    dict_keywords=dict_keywords,
                    text_side=text_side,
                    name_setting=name_setting,
                    name_directory_faction=name_directory_faction,
                    bool_show_inactive_information=False)

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

