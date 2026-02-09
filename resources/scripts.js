



function set_class_victory_state() {

    function get_int_points_remaining(text_side) {

        return parseInt(
            document
                .getElementById(text_side)
                .getElementsByClassName("victory_state")[0]
                .textContent)
    }

    let int_points_difference = get_int_points_remaining("left")
        - get_int_points_remaining("right")

    function get_name_class() {
        if (int_points_difference > 0)
            return "left_winning"
        else if (int_points_difference < 0)
            return "right_winning"
        else
            return "draw"
    }

    document
        .getElementById("army_lists")
        .classList = [get_name_class()]
}


function update_points_total(
    text_side) {

    let element_side = document
        .getElementById(text_side)

    let int_points_total = Array.from(element_side
        .getElementsByClassName("unit_army_list"))
        .map(element => parseInt(element.getElementsByClassName("count_models")[0].textContent) * parseInt(element.getAttribute("points_per_model")))
        .reduce((a, b) => a + b)

    element_side
        .getElementsByClassName("victory_state")[0]
        .textContent = int_points_total.toString()

    set_class_victory_state()
}


function set_health_bar(
    element_health_bar,
    index_token,
    text_class) {

    let array_tokens = Array.from(element_health_bar
        .getElementsByClassName("token"))

    array_tokens
        .slice(0, index_token)
        .forEach(element => element.classList.add(text_class))

    array_tokens
        .slice(index_token, array_tokens.length)
        .forEach(element => element.classList.remove(text_class))

    if (text_class == "used") {
        if (index_token == array_tokens.length - 1) {
            element_health_bar.classList.add("red")
        } else {
            element_health_bar.classList.remove("red")
        }
    }
}


function setup_health_bars() {

    function setup_health_bar(
        element_unit) {

        let element_health_bar = element_unit
            .getElementsByClassName("health_bar")[0]

        let array_tokens = Array.from(element_health_bar
            .getElementsByClassName("token"))

        function set_triggers(
            element,
            index) {

            element.addEventListener("click", () => set_health_bar(element_health_bar, index, "used"))
            element.addEventListener("mouseenter", () => set_health_bar(element_health_bar, index, "preview_used"))
        }

        element_health_bar
            .addEventListener("mouseleave", () => set_health_bar(element_health_bar, 0, "preview_used"))

        array_tokens
            .forEach(set_triggers)
    }

    Array.from(document
        .getElementsByClassName("unit_army_list"))
        .forEach(setup_health_bar)
}


function decrease_count_models(
    text_side,
    index_row) {

    let element_unit = document
        .getElementById(text_side)
        .getElementsByClassName("unit_army_list")[index_row]

    let element_count_models = element_unit
        .getElementsByClassName("count_models")[0]

    var int_count_models_new = parseInt(element_count_models.textContent) - 1

    if (int_count_models_new <= 0) {
        element_unit
            .classList
            .add("destroyed")

        test_next_turn()
    }

    element_count_models.textContent = int_count_models_new
        .toString()

    set_health_bar(
        element_unit
            .getElementsByClassName("health_bar")[0],
        0,
        "used")

    update_points_total(text_side)
}


function set_inactive(
    text_side,
    index_row) {

    document
        .getElementById(text_side)
        .getElementsByClassName("unit_army_list")[index_row]
        .classList
        .add("inactive")

    test_next_turn()
}


function test_next_turn() {

    array_units = Array.from(document
        .getElementsByClassName("unit_army_list"))

    if (!array_units.every(element => element.classList.contains("inactive") || element.classList.contains("destroyed")))
        return;

    array_units
        .forEach(element => element.classList.remove("inactive"))

    element_turn_counter = document
        .getElementById("turn_counter")

    element_turn_counter
        .textContent = (parseInt(element_turn_counter
            .textContent)
            + 1)
            .toString()
}


function initialise() {

    setup_health_bars()
    update_points_total("left")
    update_points_total("right")
}

