

import json
import os
import typing

from lib.unary import _dicts
from lib.unary import _iters
from lib.unary.main import unary

from src import md_shared




def main():

    @unary()
    def update_setting(
        name_setting:str):

        @unary()
        def save_army_list_template(
            dict_faction:typing.Dict):

            def get_dict_unit(
                dict_unit:typing.Dict):

                name_unit = dict_unit \
                    ["name"]

                return {
                    "name": name_unit,
                    "count_models": 1,
                    "attached_to_index": None}

            list_dicts_units = list(
                    map(
                        get_dict_unit,
                        dict_faction \
                            ["units"]))

            name_faction = dict_faction \
                ["name"]

            dict_army_list = {
                "faction": name_faction,
                "units": list_dicts_units}

            name_directory_faction = md_shared.get_text_name_directory_faction(name_faction)

            name_file_json = "army_list_" \
                + name_directory_faction \
                + ".json"

            path_data = os.path.join(
                    "src",
                    "data",
                    name_setting,
                    "army_list_templates",
                    name_file_json)

            text_json = json.dumps(
                    obj=dict_army_list,
                    indent=4,
                    ensure_ascii=False)

            with open(path_data, mode="w", encoding="utf-8") as file:
                file \
                    .write(text_json)

            return None

        path_data = os.path.join(
                "src",
                "data",
                name_setting,
                "data_factions.json")

        with open(path_data, mode="r", encoding="utf-8") as file:
            dict_factions = json.load(file)

        dict_factions \
            >> _dicts.to_iterable_values() \
            >> _iters.to_iterable_chained() \
            >> _iters.to_iterable_for_each_eager(save_army_list_template)

    md_shared.LIST_NAMES_SETTINGS \
        >> _iters.to_iterable_for_each_eager(
            update_setting)

    return None


if __name__ ==  "__main__":
    main()

