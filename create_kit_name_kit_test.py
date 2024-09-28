import sender_stand_request
import data

def positive_assert(name):
    kit_body = name
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name ["name"]


def negative_assert_symbol(name):
        kit_body = name
        kit_response = sender_stand_request.post_new_client_kit(kit_body)
        assert kit_response.status_code == 400
        assert kit_response.json()["name"] == 400


def test_create_kit_body_1_letter_in_first_name_get_success_response():
    positive_assert(data.kit_body_1)

def test_create_kit_body_511_letter_in_name_get_success_response():
    positive_assert(data.kit_body_2)

def test_create_kit_body_0_letter_in_name_get_error_response():
    negative_assert_symbol(data.kit_body_3)

def test_create_kit_body_512_letter_in_name_get_error_response():
    negative_assert_symbol(data.kit_body_4)

def test_create_kit_body_has_special_symbol_in_name_get_success_response():
    positive_assert(data.kit_body_5)

def test_create_kit_body_has_space_in_name_get_successful_response():
    positive_assert(data.kit_body_6)

def test_create_kit_body_has_number_in_name_get_success_response():
    positive_assert(data.kit_body_7)

def test_create_kit_body_no_name_get_error_response():
    negative_assert_symbol(data.Kit_body_8)

def test_create_kit_body_number_type_name_get_error_response():
    negative_assert_symbol(data.Kit_body_9)