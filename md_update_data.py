

import json
import os
import typing

from lib.unary import _dicts
from lib.unary import _iters
from lib.unary.main import unary




def main():

    def modify_data(
        dict_factions:typing.Dict):

        @unary()
        def modify_faction(
            dict_faction:typing.Dict):

            def modify_unit(
                dict_unit:typing.Dict):

                def re_add_property(
                    name_property:str):

                    t = dict_unit[name_property]

                    del dict_unit[name_property]

                    dict_unit[name_property] = t

                def modify_action(
                    dict_action:typing.Dict):

                    # placeholder

                    return None

                # placeholder

                list(
                        map(
                            modify_action,
                            dict_unit \
                                ["actions"]))

                return None

            # placeholder

            list(
                    map(
                        modify_unit,
                        dict_faction \
                            ["units"]))

            return None

        dict_factions \
            >> _dicts.to_iterable_values() \
            >> _iters.to_iterable_chained() \
            >> _iters.to_iterable_for_each_eager(modify_faction)

        return None

    path_data = os.path.join(
            "src",
            "data",
            "data_factions.json")

    with open(path_data, mode="r", encoding="utf-8") as file:
        dict_factions = json.load(file)

    modify_data(dict_factions)

    text_json = json.dumps(
            obj=dict_factions,
            indent=4,
            ensure_ascii=False)

    with open(path_data, mode="w", encoding="utf-8") as file:
        file \
            .write(text_json)

    return None


if __name__ ==  "__main__":
    main()

