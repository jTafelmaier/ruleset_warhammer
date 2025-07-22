



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

        style_div_faction.display =  "block"}

    else {
        Array.from(document
            .getElementsByClassName("container_faction_rules"))
            .forEach(element => element.classList.remove("grayscale"))

        style_div_faction.display =  "none"}
}


function increase_victory_points(text_side) {

    let element_victory_points = document
        .getElementsByClassName("army_list " + text_side)[0]
        .getElementsByClassName("victory_points")[0]

    element_victory_points.textContent = (parseInt(element_victory_points.textContent) + 1).toString()
}


function decrease_victory_points(text_side) {

    let element_victory_points = document
        .getElementsByClassName("army_list " + text_side)[0]
        .getElementsByClassName("victory_points")[0]

    let int_victory_points_current = parseInt(element_victory_points.textContent)

    if (int_victory_points_current <= 0) {
        return
    }

    element_victory_points.textContent = (int_victory_points_current - 1).toString()
}


function update_count_models(element_tr, bool_increase) {

    let element_count_models = element_tr
        .getElementsByClassName("count_models")[0]

    var int_count_models_current = parseInt(element_count_models.textContent)
    let int_count_models_initial = parseInt(element_count_models.getAttribute("initial"))

    if (bool_increase) {
        if (int_count_models_current >= int_count_models_initial) {
            return
        }
        var int_count_models_new = int_count_models_current + 1

        element_tr
            .classList
            .remove("destroyed")
    } else {
        if (int_count_models_current <= 0) {
            return
        } else if (int_count_models_current == 1) {
            element_tr
                .classList
                .add("destroyed")
        }
        var int_count_models_new = int_count_models_current - 1
    }

    let element_table = element_tr
        .parentElement

    element_count_models.textContent = int_count_models_new
        .toString()

    element_tr
        .getElementsByClassName("points_cost")[0]
        .textContent = (int_count_models_new * parseInt(element_tr.getAttribute("points_per_model")))
            .toString()

    let int_points_cost_total = Array.from(element_table
        .getElementsByClassName("points_cost"))
        .map(element => parseInt(element.textContent))
        .reduce((a, b) => a + b)

    element_table
        .getElementsByClassName("points_total")[0]
        .textContent = "Points (" + int_points_cost_total.toString() + " total)"
}


function increase_number_models(text_id_element) {

    let element_tr = document
        .getElementById(text_id_element)

    update_count_models(
        element_tr,
        true)
}


function reduce_health(text_id_element) {

    let element_tr = document
        .getElementById(text_id_element)

    let element_parent = element_tr
        .getElementsByClassName("health_bar")[0]

    let array_tokens = element_parent
        .getElementsByClassName("token")

    let int_count_tokens_used_new = element_parent
        .getElementsByClassName("used")
        .length + 1

    if (int_count_tokens_used_new == array_tokens.length) {
        int_count_tokens_used_new = 0

        update_count_models(
            element_tr,
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


function reduce_action_tokens(text_id_element) {

    let element_parent = document
        .getElementById(text_id_element)
        .getElementsByClassName("action_tokens")[0]

    let array_tokens = element_parent
        .getElementsByClassName("token")

    let int_count_tokens_used_current = element_parent
        .getElementsByClassName("used")
        .length

    if (int_count_tokens_used_current < array_tokens.length) {
        var int_count_tokens_used_new = int_count_tokens_used_current + 1
    } else {
        var int_count_tokens_used_new = 0
    }

    for (let i = 0; i < int_count_tokens_used_new; i++) {
        array_tokens[i].classList.add("used")
    }
    for (let i = int_count_tokens_used_new; i < array_tokens.length; i++) {
        array_tokens[i].classList.remove("used")
    }
}


function restore_action_tokens() {

    Array.from(document
        .getElementById("army_lists")
        .getElementsByClassName("action_token token"))
        .forEach(element => element.classList.remove("used"))

}

