import pytest
from trace import calculate

def test_units_and_limit():
    result = calculate(100, 1)
    assert result['resistance_ohms'] == pytest.approx(0.048)
    assert result['voltage_drop_volts'] == pytest.approx(0.096)
    assert result['power_watts'] == pytest.approx(0.192)
    assert result['within_limit']
    assert not calculate(100, 0.1)['within_limit']

@pytest.mark.parametrize('length,width', [(-1,1),(1,0),(1,float('nan'))])
def test_invalid_dimensions(length,width):
    with pytest.raises(ValueError):
        calculate(length,width)
