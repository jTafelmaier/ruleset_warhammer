



function calculate_winning_state() {

    function set_texts(function_get_text) {
    
        function set_text(
            text_side,
            index) {

            element = document
                .getElementsByClassName(text_side)[0]
                .getElementsByClassName("outcome")[0]

            text = function_get_text(index)

            element.textContent = text
            element.classList = "outcome " + text
        }

        [
            "left",
            "right"]
            .forEach(set_text)
        }

    function determine_winning(property) {

        function get_int_value(text_side) {

            return parseInt(document
                .getElementsByClassName(text_side)[0]
                .getElementsByClassName(property)[0]
                .getElementsByClassName("value")[0]
                .textContent)
        }

        let int_difference = get_int_value("left") - get_int_value("right")

        if (int_difference == 0) {
            return false
        }

        let array_winning = [
            "winning",
            "losing"]

        if (int_difference < 0) {
            array_winning.reverse()
        }

        set_texts(index => array_winning[index])

        return true
    }

    if (determine_winning("victory_points")) {
        return
    }
    if (determine_winning("model_points")) {
        return
    }

    set_texts(index => "draw")
}


function update_victory_points(
    text_side,
    bool_increase) {

    let element_victory_points = document
        .getElementsByClassName(text_side)[0]
        .getElementsByClassName("victory_state")[0]
        .getElementsByClassName("value")[0]

    let int_victory_points_current = parseInt(element_victory_points.textContent)

    let int_change = bool_increase ? 1 : -1

    if (int_victory_points_current <= 0 && int_change == -1) {
        return
    }

    element_victory_points.textContent = (int_victory_points_current + int_change).toString()

    calculate_winning_state()
}


function calculate_points_total(
    text_side) {

    let int_points_cost_total = Array.from(document
        .getElementsByClassName(text_side)[0]
        .getElementsByClassName("unit_army_list"))
        .map(element => parseInt(element.getElementsByClassName("count_current")[0].textContent) * parseInt(element.getAttribute("points_per_model")))
        .reduce((a, b) => a + b)

    document
        .getElementsByClassName(text_side)[0]
        .getElementsByClassName("model_points")[0]
        .getElementsByClassName("value")[0]
        .textContent = int_points_cost_total.toString()

    calculate_winning_state()
}


function setup_health_bars() {

    function setup_health_bars_side(
        text_side) {

        let array_units = document
            .getElementsByClassName(text_side)[0]
            .getElementsByClassName("unit_army_list")

        function setup_health_bar(
            index) {

            let element_health_bar = array_units[index]
                .getElementsByClassName("health_bar")[0]

            let array_tokens = element_health_bar
                .getElementsByClassName("token")

            function set_class_health_tokens(
                index_token,
                text_class) {

                Array.from(array_tokens)
                    .slice(0, index_token)
                    .forEach(element => element.classList.add(text_class))

                Array.from(array_tokens)
                    .slice(index_token, array_tokens.length)
                    .forEach(element => element.classList.remove(text_class))
            }

            function save_health_bar(
                index_token) {

                set_class_health_tokens(index_token, "used")

                if (index_token == array_tokens.length - 1) {
                    element_health_bar.classList.add("red")
                } else {
                    element_health_bar.classList.remove("red")
                }
            }

            for (let index_token = 0; index_token < array_tokens.length; index_token++) {
                array_tokens[index_token].addEventListener("mouseenter", () => set_class_health_tokens(index_token, "preview_used"))
                array_tokens[index_token].addEventListener("click", () => save_health_bar(index_token))
            }

            element_health_bar
                .addEventListener("mouseleave", () => set_class_health_tokens(0, "preview_used"))
        }

        for (let index_unit = 0; index_unit < array_units.length; index_unit++) {
            setup_health_bar(index_unit)
        }

    }

    setup_health_bars_side("left")
    setup_health_bars_side("right")

}


function initialise() {

    setup_health_bars()
    calculate_points_total("left")
    calculate_points_total("right")

}


function update_count_models(
    text_side,
    index_row,
    bool_increase) {

    let element_unit = document
        .getElementsByClassName(text_side)[0]
        .getElementsByClassName("unit_army_list")[index_row]

    let element_count_models = element_unit
        .getElementsByClassName("count_current")[0]

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

    calculate_points_total(text_side)
}


function toggle_inactive(
    text_side,
    index_row) {

    document
        .getElementsByClassName(text_side)[0]
        .getElementsByClassName("unit_army_list")[index_row]
        .classList
        .toggle("inactive")

}

function next_turn() {

    Array.from(document
        .getElementsByClassName("unit_army_list"))
        .forEach(element => element.classList.remove("inactive"))

}

