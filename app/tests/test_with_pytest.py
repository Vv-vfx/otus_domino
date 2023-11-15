import pytest


# ======================
# без фикстуры
# ======================
# from service.gamer import Gamer

# @pytest.mark.parametrize("name, role, number, mock_return_value, _cross_out_number_human_return", 
#                         [
#                             ('Ivan', 'human', 10, "continue play", "continue play" ),
#                             ('Ivan', 'human', 0, "not number in card", "lost"),
#                             ('Ivan', 'human', 90, "victory", "victory"),
#                         ]
#                         )
# def test_cross_out_number_human(mocker, name, role, number, mock_return_value, _cross_out_number_human_return):
 
#     gamer = Gamer(name, role)
#     mocker.patch.object(gamer.card, 'cross_out_number', return_value=mock_return_value)
 
#     assert gamer._cross_out_number_human(number) == _cross_out_number_human_return, 'error!'

# ======================
# c фикстурой
# ======================
@pytest.mark.parametrize("number, mock_return_value, _cross_out_number_human_return", 
                        [
                            (10, "continue play", "continue play" ),
                            (0, "not number in card", "lost"),
                            (90, "victory", "victory"),
                        ]
                        )
def test_cross_out_number_human(mocker, gamer, number, mock_return_value, _cross_out_number_human_return):
 
    mocker.patch.object(gamer.card, 'cross_out_number', return_value=mock_return_value)
 
    assert gamer._cross_out_number_human(number) == _cross_out_number_human_return, 'error!'
   

