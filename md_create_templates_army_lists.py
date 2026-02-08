

import json
import os
import typing

from lib.unary import _dicts
from lib.unary import _iters
from lib.unary.main import unary

from src import md_shared




def main():

    @unary()
    def save_army_list_template(
        dict_faction:typing.Dict):

        def get_dict_unit(
            dict_unit:typing.Dict):

            name_unit = dict_unit \
                ["name"]

            return {
                "name": name_unit,
                "count_models": 1}

        list_dicts_units = list(
                map(
                    get_dict_unit,
                    dict_faction \
                        ["units"]))

        name_faction = dict_faction \
            ["name"]

        name_file_json = "army_list_" \
            + name_faction \
            + ".json"

        path_data = os.path.join(
                "src",
                "data",
                "army_list_templates",
                name_file_json)

        text_json = json.dumps(
                obj={
                    "faction": name_faction,
                    "units": list_dicts_units},
                indent=4,
                ensure_ascii=False)

        with open(path_data, mode="w", encoding="utf-8") as file:
            file \
                .write(text_json)

        return None

    md_shared.get_dict_setting("data_factions.json") \
        >> _dicts.to_iterable_values() \
        >> _iters.to_iterable_chained() \
        >> _iters.to_iterable_for_each_eager(save_army_list_template)

    return None


if __name__ ==  "__main__":
    main()

