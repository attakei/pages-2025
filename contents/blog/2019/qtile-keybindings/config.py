from libqtile.command import lazy
from libqtile.config import Key

keys = [
    # 既存のものは省略
    # ミュートの切り替え
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle")),
    # ボリュームを上げ下げする
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%")),
    # 明るさを上げ下げする
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 5")),
]
