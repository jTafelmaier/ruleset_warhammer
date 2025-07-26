



function display_faction(text_id_faction) {

    let style_div_faction = document.getElementById(text_id_faction).style

    if (style_div_faction.display == "none") {

        Array.from(document
            .getElementsByClassName("container_faction_rules"))
            .forEach(element => element.classList.add("grayscale"))

        Array.from(document
            .getElementsByClassName("div_faction"))
            .forEach(element => element.style.display = "none")

        document.getElementsByClassName(text_id_faction)
            [0]
            .classList
            .remove("grayscale")

        style_div_faction.display =  "grid"}

    else {
        Array.from(document
            .getElementsByClassName("container_faction_rules"))
            .forEach(element => element.classList.remove("grayscale"))

        style_div_faction.display =  "none"}
}


function increase_victory_points(text_side) {

    let element_victory_points = document
        .getElementsByClassName("victory_state " + text_side)[0]
        .getElementsByTagName("span")[0]

    element_victory_points.textContent = (parseInt(element_victory_points.textContent) + 1).toString()
}


function decrease_victory_points(text_side) {

    let element_victory_points = document
        .getElementsByClassName("victory_state " + text_side)[0]
        .getElementsByTagName("span")[0]

    let int_victory_points_current = parseInt(element_victory_points.textContent)

    if (int_victory_points_current <= 0) {
        return
    }

    element_victory_points.textContent = (int_victory_points_current - 1).toString()
}


function update_count_models(
    element_unit,
    text_side,
    bool_increase) {

    let element_count_models = element_unit
        .getElementsByClassName("count_models")[0]

    var int_count_models_current = parseInt(element_count_models.textContent)
    let int_count_models_initial = parseInt(element_count_models.getAttribute("initial"))

    if (bool_increase) {
        if (int_count_models_current >= int_count_models_initial) {
            return
        }
        var int_count_models_new = int_count_models_current + 1

        element_unit
            .classList
            .remove("destroyed")
    } else {
        if (int_count_models_current <= 0) {
            return
        } else if (int_count_models_current == 1) {
            element_unit
                .classList
                .add("destroyed")
        }
        var int_count_models_new = int_count_models_current - 1
    }

    element_count_models.textContent = int_count_models_new
        .toString()

    let int_points_cost_total = Array.from(element_unit
        .parentElement
        .getElementsByClassName("unit_army_list"))
        .map(element => parseInt(element.getElementsByClassName("count_models")[0].textContent) * parseInt(element.getAttribute("points_per_model")))
        .reduce((a, b) => a + b)

    document
        .getElementsByClassName("victory_state " + text_side)[0]
        .getElementsByClassName("points_total")[0]
        .textContent = int_points_cost_total.toString() + " points remaining"
}


function increase_number_models(text_side, index_row) {

    let element_unit = document
        .getElementsByClassName("army_list " + text_side)[0]
        .getElementsByClassName("unit_army_list")[index_row]

    update_count_models(
        element_unit,
        text_side,
        true)
}


function reduce_health(text_side, index_row) {

    let element_unit = document
        .getElementsByClassName("army_list " + text_side)[0]
        .getElementsByClassName("unit_army_list")[index_row]

    let element_parent = element_unit
        .getElementsByClassName("health_bar")[0]

    let array_tokens = element_parent
        .getElementsByClassName("token")

    let int_count_tokens_used_new = element_parent
        .getElementsByClassName("used")
        .length + 1

    if (int_count_tokens_used_new == array_tokens.length) {
        int_count_tokens_used_new = 0

        update_count_models(
            element_unit,
            text_side,
            false)
    }

    if (int_count_tokens_used_new == array_tokens.length - 1) {
        element_parent.classList.add("red")
    } else {
        element_parent.classList.remove("red")
    }

    for (let i = 0; i < int_count_tokens_used_new; i++) {
        array_tokens[i].classList.add("used")
        array_tokens[i].classList.remove("next")
    }

    let list_classes = array_tokens[int_count_tokens_used_new]
        .classList

    list_classes.remove("used")
    list_classes.add("next")

    for (let i = int_count_tokens_used_new + 1; i < array_tokens.length; i++) {
        array_tokens[i].classList.remove("used")
        array_tokens[i].classList.remove("next")
    }
}


function toggle_inactive(text_side, index_row) {

    document
        .getElementsByClassName("army_list " + text_side)[0]
        .getElementsByClassName("unit_army_list")[index_row]
        .classList
        .toggle("inactive")

}

function next_turn() {

    Array.from(document
        .getElementsByClassName("unit_army_list"))
        .forEach(element => element.classList.remove("inactive"))

}

