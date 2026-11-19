"""第 63 批：远处整座山突然消失，近处小石头却一直在画，转视角时三角形像纸片一..."""

def cone_radius(max_dist, center_dist):
    """包围锥半径。"""
    raise NotImplementedError("TODO: cone_radius")

def normal_cone(dot, threshold):
    """法线锥。"""
    raise NotImplementedError("TODO: normal_cone")

def index_bits(count):
    """索引位宽。"""
    raise NotImplementedError("TODO: index_bits")

def lod_seam(a, b):
    """LOD 接缝。"""
    raise NotImplementedError("TODO: lod_seam")

def pack_id(meshlet_id, instance_id):
    """ID 打包。"""
    raise NotImplementedError("TODO: pack_id")

def hzb_age(frame, result_frame, max_lag):
    """HZB 时效。"""
    raise NotImplementedError("TODO: hzb_age")

def instance_matrix(scale, offset):
    """实例数据。"""
    raise NotImplementedError("TODO: instance_matrix")

def buffer_capacity(count, limit):
    """缓冲上限。"""
    raise NotImplementedError("TODO: buffer_capacity")

def primitive_cull(area, epsilon):
    """图元裁剪。"""
    raise NotImplementedError("TODO: primitive_cull")

def local_index(index, base):
    """局部索引。"""
    raise NotImplementedError("TODO: local_index")

def skin_bounds(bind, current):
    """蒙皮包围盒。"""
    raise NotImplementedError("TODO: skin_bounds")

def debug_match(debug, release):
    """调试一致。"""
    raise NotImplementedError("TODO: debug_match")

def cluster_count(triangles, per_cluster):
    """簇数量。"""
    raise NotImplementedError("TODO: cluster_count")

def task_amplify(threads, per_thread):
    """任务放大。"""
    raise NotImplementedError("TODO: task_amplify")

def meshlet_valid(count, max_count):
    """簇上限。"""
    raise NotImplementedError("TODO: meshlet_valid")
