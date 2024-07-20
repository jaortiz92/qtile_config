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

from typing import List  # noqa: F401

from libqtile import bar, layout, extension, hook, qtile #widget,
from libqtile import widget as widget_basic
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration
import colors
import re

mod = "mod4"
alt = "mod1"
terminal = "tilix"

FONT = "HackNerdFontMono-Regular"
FONT_BOLD = "HackNerdFontMono-Bold"
COLORS = colors.MonokaiPro


keys = [
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([alt], "Tab", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge oflLk screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([alt], "F4", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "g", lazy.window.toggle_floating(), desc="Toggle floating",),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.run_extension(extension.DmenuRun(
        background=COLORS[0][0],
        foreground=COLORS[1][0],
        selected_background=COLORS[0][1],
        selected_foreground=COLORS[1][1],
        dmenu_ignorecase=True
    )),
        desc="Spawn a command using a prompt widget"),
    Key([mod], "space", lazy.spawn("rofi -show drun"), desc="Menu Rofi"),
    Key([mod], "f", lazy.spawn("firefox"), desc="Menu Rofi"),
    Key([mod], "i", lazy.spawn("chromium"), desc="Menu Rofi"),
    Key([mod], "c", lazy.spawn("code"), desc="Menu Rofi"),
]

# groups = [Group(i) for i in "123456789"]
__groups = {
    1: Group("MAIN"),
    2: Group("WWW"),#, matches=[Match(wm_class=["firefox"])]),
    3: Group("DEV"),#, matches=[Match(wm_class=["code", "chromium"])]),
    4: Group("OTH"),
}

groups = [__groups[i] for i in __groups.keys()]


def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]


for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(get_group_key(i.name)), lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(get_group_key(i.name)), lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])


layout_theme = {"border_width": 2,
                "margin": 8,
                "align": 1,
                "border_focus": COLORS[8],
                "border_normal": COLORS[0]
                }

layouts = [
    layout.Columns(
        border_focus_stack=COLORS[0],
        border_width=2,
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
        **layout_theme
    ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    layout.Tile(
         shift_windows=True,
         border_width = 0,
         margin = 0,
         ratio = 0.335,
    ),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Max(
         border_width = 0,
         margin = 0,
    ),
]

widget_defaults = dict(
    font=FONT_BOLD, #font='sans',
    fontsize=16,
    padding=10,
    background=COLORS[0]
)
extension_defaults = widget_defaults.copy()

def widget_spacer():
    return widget.Spacer(length = 5)

def change_volume(delta):
    qtile.cmd_spawn("pactl set-sink-volume @DEFAULT_SINK@ {}%".format(delta))

def decoration_theme(color):
    return [
        BorderDecoration(
            colour = COLORS[color],
            border_width = [0, 0, 2, 0],
        )
    ]

def text_box():
    return widget.TextBox(
        text = '|',
        font = FONT,
        foreground = COLORS[1],
        padding = 5,
        fontsize = 14
    )

def init_widgets_list():
    widgets_list = [
        widget.Image(
                 filename = "~/.config/qtile/icons/logo.png",
                 scale = "False",
                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("rofi -show drun")},
                 ),
        widget.Prompt(
                 font = FONT,
                 fontsize=14,
                 foreground = COLORS[1]
        ),
        widget.GroupBox(
                 fontsize = 12,
                 margin_y = 5,
                 margin_x = 5,
                 padding_y = 0,
                 padding_x = 5,
                 borderwidth = 3,
                 active = COLORS[8],
                 inactive = COLORS[1],
                 rounded = False,
                 highlight_color = COLORS[2],
                 highlight_method = "line",
                 this_current_screen_border = COLORS[7],
                 this_screen_border = COLORS[4],
                 other_current_screen_border = COLORS[7],
                 other_screen_border = COLORS[4],
                 ),
        text_box(),
        widget.CurrentLayoutIcon(
                 # custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                 foreground = COLORS[1],
                 padding = 4,
                 scale = 0.6
                 ),
        widget.CurrentLayout(
                 foreground = COLORS[1],
                 padding = 5
                 ),
        text_box(),
        widget.WindowName(
                 foreground = COLORS[6],
                 max_chars = 40
                 ),
        #widget.GenPollText(
        #         update_interval = 300,
        #         func = lambda: subprocess.check_output("printf $(uname -r)", shell=True, text=True),
        #         foreground = COLORS[3],
        #         fmt = '{}',
        #         decorations=[
        #             BorderDecoration(
        #                 colour = COLORS[3],
        #                 border_width = [0, 0, 2, 0],
        #             )
        #         ],
        #         ),
        widget_spacer(),
        widget.CPU(
                 format = ' Cpu: {load_percent}%',
                 foreground = COLORS[4],
                 decorations=decoration_theme(4),
                 ),
        widget_spacer(),
        widget.Memory(
                 foreground = COLORS[8],
                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                 format = '{MemUsed: ,.0f}{mm}',
                 fmt = '  Mem: {} used',
                 decorations=decoration_theme(8),
                 ),
        widget_spacer(),
        widget.DF(
                 update_interval = 60,
                 foreground = COLORS[5],
                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e df')},
                 partition = '/',
                 #format = '[{p}] {uf}{m} ({r:.0f}%)',
                 format = '{uf}{m} free',
                 fmt = '  Disk: {}',
                 visible_on_warn = False,
                 decorations = decoration_theme(5),
                 ),
        widget_spacer(),
        widget.Battery(
            foreground = COLORS[6],
            fmt = '⚡ Btry: {}',
            #format='{char} {percent:2.0%} {hour:d}:{min:02d} {watt:.2f} W',
            format='{char}{percent:2.0%} {hour:d}:{min:02d}',
            low_percentage=0.2,
            decorations = decoration_theme(6),
        ),
        widget_spacer(),
        widget_basic.Systray(
            background = COLORS[7][1],
            padding = 3,
            icon_size = 20,
            #decorations = decoration_theme(5)
        ),
        #widget.Volume(
                #channel='IEC958',
                #foreground = COLORS[7],
                #emoji = True,
                #fmt = 'Vol: {}',
                #decorations=decoration_theme(7),
                #update_interval=1,
                #volume_app=change_volume
                #),
        widget_spacer(),
        widget.KeyboardLayout(
                 foreground = COLORS[3],
                 fmt = '⌨ {}',
                 configured_keyboards = ['latam'],
                 decorations=decoration_theme(3),
                 ),
        widget_spacer(),
        widget.Clock(
                 foreground = COLORS[4],
                 format = "%a, %b %d %Y - %H:%M",
                 decorations=decoration_theme(4),
                 ),
        #widget_spacer(),
        #widget_spacer(),
        ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1 

# All other monitors' bars will display everything but widgets 22 (systray) and 23 (spacer).
def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[22:24]
    return widgets_screen2

# For adding transparency to your bar, add (background="#00000000") to the "Screen" line(s)
# For ex: Screen(top=bar.Bar(widgets=init_widgets_screen2(), background="#00000000", size=24)),

def init_screens():
    return [
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=26)),
            #Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26)),
            #Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26))
        ]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    #widgets_screen2 = init_widgets_screen2()

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])
    # subprocess.run([home + '/.config/qtile/autostart_display.sh'])


@hook.subscribe.startup_complete
def reset():
    lazy.restart()


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
