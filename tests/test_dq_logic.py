# 这是一个基础的单元测试，用来验证我们的逻辑框架是否打通
import pytest

def test_infrastructure_ready():
    """验证测试框架是否能正常工作"""
    is_ready = True
    assert is_ready is True

def test_spark_session_exists():
    """验证在测试环境中是否能识别到代码逻辑（模拟）"""
    # 这里以后会放你对 _apply_rules 的测试
    assert 1 + 1 == 2