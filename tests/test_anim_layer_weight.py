import pytest
import gameplay.anim_layer_weight as mod

CASES = [
    ("normalize_weights", (1)),
    ("sample_interp", (1)),
    ("slice_gate", (1)),
    ("bone_version", (1)),
    ("time_step", (1)),
    ("weapon_switch", (1)),
    ("weight_snapshot", (1)),
    ("layer_blend", (1)),
    ("validation", (1)),
    ("audit", (1)),
    ("fallback", (1)),
    ("clamp", (1)),
    ("metrics", (1)),
    ("cross_frame", (1)),
    ("determinism", (1)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
