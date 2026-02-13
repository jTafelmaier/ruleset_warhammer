

import typing

from src import md_shared




def generate_htmls():

    list_dicts_factions = md_shared.get_dict_setting("data_factions.json") \
        ["data"]

    def get_text_html_data_unit(
        dict_unit:typing.Dict,
        name_faction:str):

        def get_text_html_attack(
            dict_attack:typing.Dict):

            return "<div class=\"model_property\"><span class=\"icon attack\">" \
                + dict_attack \
                    ["range"] \
                + "</span>" \
                + dict_attack \
                    ["hits"] \
                    .__str__() \
                + "x " \
                + dict_attack \
                    ["strength"] \
                    .__str__() \
                + " " \
                + " " \
                    .join(
                        dict_attack \
                            ["keywords"]) \
                + "</div>"

        def get_text_html_keywords():

            if len(dict_unit["keywords"]) == 0:
                return ""

            return "<div class=\"model_property\">" \
                + "<br/>" \
                    .join(
                        dict_unit \
                            ["keywords"]) \
                + "</div>"

        path_image_unit = "/" \
            .join(
                [
                    md_shared.get_text_path_images_faction(name_faction),
                    "units",
                    dict_unit \
                        ["name"] \
                        + ".png"])

        text_html_rows_attacks = "" \
            .join(
                map(
                    get_text_html_attack,
                    dict_unit
                        ["attacks"]))

        return "<div class=\"model\" title=\"" \
            + str(
                dict_unit \
                    ["points_per_model"]) \
            + " points per model.\"><div class=\"image_unit\" style=\"background-image: url('" \
            + path_image_unit \
            + "')\"><div class=\"data_unit\"><div class=\"name_unit\">" \
            + dict_unit \
                ["name"] \
            + "</div><div class=\"model_property\"><span class=\"icon\">⛊</span>" \
            + str(
                dict_unit \
                    ["armor"]) \
            + "</div>" \
            + "<div class=\"model_property\"><span class=\"icon\">🡆</span>" \
            + str(
                dict_unit \
                    ["move"]) \
            + " " \
            + dict_unit \
                ["type_movement"] \
            + "</div>" \
            + text_html_rows_attacks \
            + get_text_html_keywords() \
            + "</div></div></div>"

    def get_text_html_faction_rules():

        def get_text_html_button_show_faction(
            dict_faction:typing.Dict):

            name_faction = dict_faction \
                ["name"]

            path_image_faction = "/" \
                .join(
                    [
                        md_shared.get_text_path_images_faction(name_faction),
                        "faction.png"])

            return "<div class=\"container_faction_button " \
                + name_faction \
                + "\"><a class=\"preview_faction_button\" href=\"index_" \
                + name_faction \
                + ".html\" style=\"background-image: url('" \
                + path_image_faction \
                + "')\">" \
                + name_faction \
                + "</a></div>"

        def create_html_faction(
            dict_faction:typing.Dict):

            name_faction = dict_faction \
                ["name"]

            def get_text_html_unit(
                dict_unit:typing.Dict):

                return get_text_html_data_unit(
                        dict_unit=dict_unit,
                        name_faction=name_faction)

            text_html_faction = "" \
                .join(
                    map(
                        get_text_html_unit,
                        dict_faction \
                            ["units"]))

            text_html = "<div class=\"faction_rules " \
                + name_faction \
                + "\">" \
                + text_html_faction \
                + "</div>"

            soup_faction = md_shared.get_soup(text_html)

            text_html_template = md_shared.get_text_file(
                [
                    "src",
                    "data",
                    "template_faction.html"])

            soup_full = md_shared.get_soup(text_html_template)

            soup_full \
                .find(
                    name="placeholder",
                    id="id_faction") \
                .replace_with(soup_faction)

            with open("index_" + name_faction + ".html", mode="w", encoding="utf-8") as file_html:
                file_html \
                    .write(
                        soup_full \
                            .prettify())

            return

        # TODO refactor
        list(
            map(
                create_html_faction,
                list_dicts_factions))

        return "<div class=\"selection_factions\">" \
            + "" \
                .join(
                    map(
                        get_text_html_button_show_faction,
                        list_dicts_factions)) \
            + "</div>"

    def get_text_html_army_lists():

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
                    + "\"><div class=\"unit_state\"><div class=\"health_bar\">" \
                    + ("<div class=\"token\" />" \
                        * 8) \
                    + "</div><div class=\"count_models\" onclick=\"decrease_count_models(" \
                    + text_parameters_functions \
                    + ")\" onmouseover=\"highlight_destroy(" \
                    + text_parameters_functions \
                    + ")\" onmouseout=\"undo_highlight_destroy(" \
                    + text_parameters_functions \
                    + ")\">" \
                    + text_count_models \
                    + "</div></div><div onclick=\"toggle_inactive(" \
                    + text_parameters_functions \
                    + ")\">" \
                    + get_text_html_data_unit(
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

    text_html_template = md_shared.get_text_file(
        [
            "src",
            "data",
            "template_index.html"])

    soup_full = md_shared.get_soup(text_html_template)

    dict_replacements = {
        "id_factions": md_shared.get_soup(get_text_html_faction_rules()),
        "id_army_lists": md_shared.get_soup(get_text_html_army_lists())}

    for id_placeholder, soup_replacement in dict_replacements.items():
        soup_full \
            .find(
                name="placeholder",
                id=id_placeholder) \
            .replace_with(soup_replacement)

    with open("index.html", mode="w", encoding="utf-8") as file_html:
        file_html \
            .write(
                soup_full \
                    .prettify())

    return None

