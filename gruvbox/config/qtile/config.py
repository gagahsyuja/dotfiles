# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from widgets.volume import Volume
from qtile_extras import widget

gruv_bg         = "#282828"
gruv_bg1        = "#3c3836"
gruv_bg2        = "#504945"
gruv_bg3        = "#665c54"
gruv_fg         = "#ebdbb2"
gruv_red        = "#cc241d"
gruv_green      = "#98971a"
gruv_yellow     = "#d79921"
gruv_blue       = "#458588"
gruv_purple     = "#b16286"
gruv_aqua       = "#689d6a"
gruv_gray       = "#a89984"

mod = "mod4"
terminal = "alacritty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("sh /home/ssa/.config/rofi/launchers/type-1/launcher.sh"), desc="Spawning Rofi"),
    Key([], "XF86MonBrightnessDown", lazy.spawn('light -U 5'), desc="Decreasing Brightness"),
    Key([], "XF86MonBrightnessUp", lazy.spawn('light -A 5'), desc="Increasing Brightness"),
    Key([], "XF86AudioLowerVolume", lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ -2%'), desc="Decreasing Audio Volume"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ +2%'), desc="Increasing Audio Volume"),
    Key([], "XF86AudioMute", lazy.spawn('pactl set-sink-mute @DEFAULT_SINK@ toggle'), desc="Muting Audio"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
   #Key([mod], "c", lazy.widget["visualiser"].toggle(), desc="cava toggle")
]

# groups = [Group(i) for i in "123456789"]
groups = [
    #Group("1", label="\uf120", spawn="alacritty"),
    Group("1", label="1", spawn="alacritty"),
    #Group("2", label="\uf268", spawn="google-chrome-stable", layout="max"),
    Group("2", label="2", spawn="google-chrome-stable", layout="max"),
    #Group("3", label="\uf1bc", spawn="spotify"),
    Group("3", label="3", spawn="spotify", layout="max"),
    Group("4"),
    Group("5"),
    Group("6")
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    #layout.Columns(
    #    border_focus = gruv_yellow,
    #    border_width=4, 
    #    margin=5),
    layout.MonadTall(
        border_focus = gruv_yellow,
        border_normal = gruv_bg2,
        border_width = 0, 
        margin = 11 
        ),
    layout.Max(
        margin = 11
        )
]

widget_defaults = dict(
    background = gruv_bg,
    foreground = gruv_fg,
    font = "JetBrainsMono Nerd Font",
    fontsize = 12,
    padding = 5
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Sep(
                    linewidth = 0,
                    padding = 10
                    ),
                widget.TextBox(
                    text = "\ue0b6",
                    fontsize = 27,
                    padding = 0,
                    foreground = gruv_yellow,
                    background = gruv_bg
                    ),
                widget.TextBox(
                    text = "\uf303",
                    fontsize = 28,
                    padding = 10,
                    foreground = gruv_bg,
                    background = gruv_yellow
                    ),
                widget.Sep(
                    linewidth = 0,
                    padding = 9,
                    background = gruv_yellow,
                    foreground = gruv_yellow
                    ),
                widget.TextBox(
                    text = "\ue0b4",
                    fontsize = 27,
                    padding = 0,
                    background = gruv_bg,
                    foreground = gruv_yellow
                    ),
                widget.Sep(
                    linewidth = 0,
                    padding = 10
                    ),
                widget.GroupBox(
                    background = gruv_bg,
                    disable_drag = True,
                    highlight_method = "line",
                    highlight_color = gruv_bg,
                    this_current_screen_border = gruv_yellow,
                    active = gruv_fg,
                    padding_x = 18,
                #   margin_x = -9,
                    margin_y = 2,
                    inactive = gruv_bg3,
                    fontsize = 21,
                    # rounded = True, 
                    ),
               #widget.Visualiser(
               #   framerate = 60,
               #   background = gruv_bg,
               #   bar_colour = gruv_yellow
               #   ),
                widget.Spacer(),
                widget.Clock(
                    format = "%I:%M %p",
                    foreground = gruv_yellow,
                    font = "JetBrainsMono Nerd Font Mono",
                    fontsize = 18
                    ),
                widget.Spacer(),
               #widget.HDDBusyGraph(
               #    graph_color = gruv_green,
               #    border_width = 0
               #    ),
               # widget.Visualiser(
               #     framerate = 60,
               #     background = gruv_yellow,
               #     bar_colour = gruv_bg
               #     ),
                widget.Sep(
                    linewidth = 0,
                    padding = 5
                    ),
                widget.Sep(
                    linewidth = 0,
                    padding = 5,
                    ),
                widget.TextBox(
                    text = "\ue0b6",
                    fontsize = 27,
                    padding = 0,
                    foreground = gruv_yellow,
                    background = gruv_bg
                    ),
                widget.TextBox(
                    text = "",
                    fontsize = 18,
                    padding = 5,
                    foreground = gruv_bg,
                    background = gruv_yellow
                    ),
                widget.DF(
                    format = "{uf}{m}",
                    padding = 5,
                    fontsize = 18,
                    visible_on_warn = False,
                    measure = "G",
                    foreground = gruv_bg,
                    background = gruv_yellow
                    ),
                widget.TextBox(
                    text = "",
                    fontsize = 18,
                    padding = 10,
                    background = gruv_yellow,
                    foreground = gruv_bg
                    ),
                widget.Memory(
                    format = "{MemUsed:.0f}{mm}",
                    fontsize = 18,
                    foreground = gruv_bg,
                    background = gruv_yellow,
                    padding = 10
                    ),
                widget.TextBox(
                    text = "\ue0b4",
                    fontsize = 27,
                    padding = 0,
                    background = gruv_bg,
                    foreground = gruv_yellow
                    ),
                widget.Sep(
                    linewidth = 0,
                    padding = 10
                    ),
                widget.TextBox(
                    text = "\ue0b6",
                    fontsize = 27,
                    padding = 0,
                    foreground = gruv_yellow,
                    background = gruv_bg
                    ),
                widget.TextBox(
                    text = "",
                    fontsize = 21,
                    padding = 10,
                    background = gruv_yellow,
                    foreground = gruv_bg
                    ),
                widget.CPU(
                    format = "{load_percent}%",
                    foreground = gruv_bg,
                    background = gruv_yellow,
                    fontsize = 18
                    ),
                widget.ThermalSensor(
                    fontsize = 18,
                    format = " {temp:.0f}{unit}",
                    foreground = gruv_bg,
                    background = gruv_yellow,
                    padding = 10
                    ),
                widget.TextBox(
                    text = "\ue0b4",
                    fontsize = 27,
                    padding = 0,
                    foreground = gruv_yellow,
                    background = gruv_bg
                    ),
                widget.Sep(
                    linewidth = 0,
                    padding = 10
                    ),
                widget.TextBox(
                    text = "\ue0b6",
                    fontsize = 27,
                    padding = 0,
                    background = gruv_bg,
                    foreground = gruv_yellow
                    ),
                widget.TextBox(
                    text = "",
                    fontsize = 18,
                    foreground = gruv_bg,
                    background = gruv_yellow,
                    padding = 10
                    ),
                Volume(
                    fontsize = 18,
                    fmt = "{}",
                    foreground = gruv_bg,
                    background = gruv_yellow,
                    get_volume_command = "pactl get-sink-volume @DEFAULT_SINK@",
                    check_mute_command = "pactl get-sink-mute @DEFAULT_SINK@",
                    check_mute_string = "yes",
                    volume_up_command = "pactl set-sink-volume @DEFAULT_SINK@ +2%",
                    volume_down_command = "pactl set-sink-volume @DEFAULT_SINK@ -2%",
                    mute_command = "pactl set-sink-mute @DEFAULT_SINK@ toggle"
                    ),
                widget.Battery(
                    format = "{char} {percent:2.0%}",
                    foreground = gruv_bg,
                    background = gruv_yellow,
                    charge_char = "",
                    discharge_char = "",
                    empty_char = "",
                    full_char = "",
                    padding = 10,
                    fontsize = 18,
                    update_interval = 1
                    ),
                widget.TextBox(
                    text = "\ue0b4",
                    fontsize = 27,
                    padding = 0,
                    foreground = gruv_yellow,
                    background = gruv_bg
                    ),
                widget.Sep(
                    linewidth = 0,
                    padding = 10
                    ),
                widget.TextBox(
                    text = "\ue0b6",
                    fontsize = 27,
                    padding = 0,
                    foreground = gruv_yellow,
                    background = gruv_bg
                    ),
               #widget.Sep(
               #    linewidth = 0,
               #    padding = 5
               #    ),
                widget.TextBox(
                    text = "\ufb77",
                    fontsize = 19,
                    padding = 10,
                    foreground = gruv_bg,
                    background = gruv_yellow
                    ),
                widget.Clock(
                    format = "%d-%m-%Y",
                    foreground = gruv_bg,
                    background = gruv_yellow,
                    font = "JetBrainsMono Nerd Font Mono",
                    padding = 10, 
                    fontsize = 18
                    ),
               #widget.Sep(
               #    padding = 13,
               #    linewidth = 0
               #    ),
                widget.TextBox(
                    text = "\ue0b4",
                    fontsize = 27,
                    padding = 0,
                    foreground = gruv_yellow,
                    background = gruv_bg
                    ),
                widget.Systray(
                    padding = 10
                    ),
                widget.Sep(
                   padding = 13,
                   linewidth = 0
                   ),
            ],
           35,
           margin=[3, 9, 11, 9],
           #margin = 8,
           #border_width=[0, 0, 0, 0],
           border_width = 6,
           #border_color=[gruv_yellow, gruv_yellow, gruv_yellow, gruv_yellow]
           border_color = gruv_bg
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button2", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button3", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
