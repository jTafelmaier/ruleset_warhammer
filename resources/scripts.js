



function display_faction(text_id_faction) {

    let style_div_faction = document.getElementById(text_id_faction).style

    if (style_div_faction.display == "none") {

        Array.from(document
            .getElementsByClassName("div_container_faction_rules"))
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
            .getElementsByClassName("div_container_faction_rules"))
            .forEach(element => element.classList.remove("grayscale"))

        style_div_faction.display =  "none"}
}


function update_points_total(element_tr) {

    let element_table = element_tr
        .parentElement

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

    let element_count_models = element_tr
        .getElementsByClassName("count_models")[0]

    let element_points_cost = element_tr
        .getElementsByClassName("points_cost")[0]

    var int_count_models_current = parseInt(element_count_models.textContent)
    var int_count_models_initial = parseInt(element_count_models.getAttribute("initial"))

    if (int_count_models_current >= int_count_models_initial) {
        return
    }

    let int_count_models_new = int_count_models_current + 1

    element_count_models.textContent = int_count_models_new
        .toString()

    element_points_cost.textContent = (int_count_models_new * parseInt(element_tr.getAttribute("points_per_model")))
        .toString()

    update_points_total(element_tr)

    element_tr
        .classList
        .remove("destroyed")
}


function reduce_health(text_id_element) {

    let element_tr = document
        .getElementById(text_id_element)

    let element_count_models = element_tr
        .getElementsByClassName("count_models")[0]

    let element_points_cost = element_tr
        .getElementsByClassName("points_cost")[0]

    let element_parent = element_tr
        .getElementsByClassName("health_bar")[0]

    let array_tokens = element_parent
        .getElementsByClassName("token")

    let int_count_tokens_used_new = element_parent
        .getElementsByClassName("used")
        .length + 1

    if (int_count_tokens_used_new == array_tokens.length) {
        int_count_tokens_used_new = 0

        let int_count_models_new = parseInt(element_count_models.textContent) - 1
        element_count_models.textContent = int_count_models_new.toString()
        element_points_cost.textContent = (int_count_models_new * parseInt(element_tr.getAttribute("points_per_model"))).toString()

        update_points_total(element_tr)

        if (int_count_models_new == 0) {
            element_tr.classList.add("destroyed")
        }
    }

    if (int_count_tokens_used_new == array_tokens.length - 1) {
        element_parent.classList.add("red")
    } else {
        element_parent.classList.remove("red")
    }

    for (let i = 0; i < int_count_tokens_used_new; i++) {
        array_tokens[i].classList.add("used")
    }
    for (let i = int_count_tokens_used_new; i < array_tokens.length; i++) {
        array_tokens[i].classList.remove("used")
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
        .getElementById("div_army_lists")
        .getElementsByClassName("action_token token"))
        .forEach(element => element.classList.remove("used"))

}

