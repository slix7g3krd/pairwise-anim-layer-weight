# pairwise-anim-layer-weight

## 领域

游戏、图形与多媒体

## 主题

动画层权重归一

## 说明

层权重归一化、跨帧采样与切片就绪门控。

初始状态下 `gameplay/anim_layer_weight.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
