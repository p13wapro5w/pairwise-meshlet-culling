import pytest
from render import meshlet_culling as mod

CASES = [
    ("cone", 'm.cone_radius(10, 4) == 6'),
    ("normal", 'm.normal_cone(0.8, 0.7) is True'),
    ("bits8", 'm.index_bits(200) == 8'),
    ("bits16", 'm.index_bits(300) == 16'),
    ("seam", 'm.lod_seam(3, 5) == 2'),
    ("pack", 'm.pack_id(2, 3) == 196610'),
    ("age", 'm.hzb_age(10, 9, 2) is True'),
    ("matrix", 'm.instance_matrix(2, (1, 2)) == (2, 4)'),
    ("capacity", 'm.buffer_capacity(10, 8) == 8'),
    ("primitive", 'm.primitive_cull(0.1, 0.01) is True'),
    ("local", 'm.local_index(2, 10) == 12'),
    ("skin", 'm.skin_bounds(1, 2) == 2'),
    ("debug", 'm.debug_match(1, 1) is True'),
    ("cluster", 'm.cluster_count(100, 32) == 4'),
    ("amplify", 'm.task_amplify(4, 2) == 8')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
