
#   ___ _____ ___ _     _____    ____             __ _
#  / _ \_   _|_ _| |   | ____|  / ___|___  _ __  / _(_) __ _
# | | | || |  | || |   |  _|   | |   / _ \| '_ \| |_| |/ _` |
# | |_| || |  | || |___| |___  | |__| (_) | | | |  _| | (_| |
#  \__\_\|_| |___|_____|_____|  \____\___/|_| |_|_| |_|\__, |
#                                                      |___/


# --------------------------------------------------------
                    #### CLASSES ####
# --------------------------------------------------------

import os
import re
import socket
import subprocess
from typing import List  # noqa: F401
from libqtile import bar, layout, widget, qtile, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.widget import Spacer
from libqtile.lazy import lazy
import colors

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget.decorations import PowerLineDecoration


# --------------------------------------------------------
                #### FUNCTIONS ####
# --------------------------------------------------------

# A function for hide/show all the windows in a group
@lazy.function
def minimize_all(qtile):
    for win in qtile.current_group.windows:
       if hasattr(win, "toggle_minimize"):
           win.toggle_minimize()



# --------------------------------------------------------
                #### DEFAULTS APPS ####
# --------------------------------------------------------

terminal = "alacritty"
home = os.path.expanduser('~')


# --------------------------------------------------------
                 #### KEYBINDINGS ####
# --------------------------------------------------------

mod = "mod1" #ALT KEY

keys = [


    # --------------------------------------------------------
                    #### WINDOW FOCUS ####
    # --------------------------------------------------------  
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(), desc="Move window focus to other window"),




    # --------------------------------------------------------
                    #### WINDOW MOVEMENT ####
    # --------------------------------------------------------
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    #Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),



    
    # --------------------------------------------------------
                    #### WM MANAGEMENT ####
    # --------------------------------------------------------
    Key([mod], "w", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "d", minimize_all(), desc="Toggle hide/show all windows on current group"),
    #Key([mod, "control"], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    #Key([mod], "p", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    #Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
		]



# --------------------------------------------------------
                    #### GROUPS ####
# --------------------------------------------------------

groups = []
group_names = ["1", "2", "3", "4", "5", "z" ]
group_labels = ["  ", "  ", "  ", " 󰮯 ", "  ", " 󰊠 "]
group_layouts = ["columns", "columns", "columns", "floating", "columns", "columns"]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))
 
for i in groups:
    keys.extend(
        [
        Key([mod],i.name,lazy.group[i.name].toscreen(),desc="Switch to group {}".format(i.name),),
        Key([mod, "shift"],i.name,lazy.window.togroup(i.name, switch_group=False),desc="Move focused window to group {}".format(i.name),),
        Key(["mod1"],"space", lazy.screen.next_group(), desc="Move to next group."),
        #Key(["mod1", "shift"], "Tab", lazy.screen.prev_group(), desc="Move to previous group."),
        ]
        )



# --------------------------------------------------------
                #### SCRATCHPADS ####
# --------------------------------------------------------

groups.append(ScratchPad("scratchpad", [
        DropDown("term", "alacritty --class=scratch", width=0.4, height=0.6, x=0.3, y=0.2, opacity=1),
        DropDown("btop", "alacritty --class=btop -e btop", width=0.4, height=0.6, x=0.3, y=0.2, opacity=1),
        DropDown("galculator", "galculator", width=0.4, height=0.6, x=0.3, y=0.2, opacity=1),
        #DropDown("ranger", "alacritty --class=ranger -e ranger", width=0.4, height=0.6, x=0.3, y=0.2, opacity=1),
        ]))




# --------------------------------------------------------
            #### SCRATCHPAD KEYBINDINGS ####
# --------------------------------------------------------

keys.extend([
    Key([mod, "shift"], "q", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod, "shift"], "w", lazy.group['scratchpad'].dropdown_toggle('btop')),
    Key([mod, "shift"], "e", lazy.group['scratchpad'].dropdown_toggle('galculator')),
    #Key([mod, "shift"], "r", lazy.group['scratchpad'].dropdown_toggle('galculator')),
        ])


# --------------------------------------------------------
                #### PYWAL COLORS ####
# --------------------------------------------------------

colors = []
cache='/home/vonraj/.cache/wal/colors'
def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(8):
            colors.append(file.readline().strip())
    colors.append('#ffffff')
    lazy.reload()
load_colors(cache)



#colors = colors.MonokaiPro

# --------------------------------------------------------
                ##### LAYOUT THEME #####
# --------------------------------------------------------


layout_theme = {
    "border_width": 3,
    "margin": 15,
    "border_focus": colors[3],
    "border_normal": "#32344a",
    "num_columns": 4,
    "insert_position": 1,
    }



# --------------------------------------------------------
                    #### LAYOUTS ####
# --------------------------------------------------------

layouts = [
      layout.Columns(**layout_theme),
      layout.Max(**layout_theme),
      layout.Floating(**layout_theme),
      #layout.Zoomy(**layout_theme),
      #layout.VerticalTile(**layout_theme),
      #layout.RatioTile(**layout_theme),
      #layout.MonadWide(**layout_theme),
      #layout.Matrix(**layout_theme),
      #layout.MonadTall(**layout_theme),
      #layout.Tile(**layout_theme),
      #layout.Bsp(**layout_theme),
]


# --------------------------------------------------------
                #### WIDGET DEFAULTS ####
# --------------------------------------------------------

widget_defaults = dict(
    font="FiraCode Nerd Font Bold Italic",
    fontsize=19,
    padding=2,
)


extension_defaults = widget_defaults.copy()



# --------------------------------------------------------
                #### DECORATIONS ####
# --------------------------------------------------------

#decor_left = {
    #"decorations": [
    #    PowerLineDecoration(
            #path="arrow_left"
   #          path="rounded_left"
            # path="forward_slash"
            # path="back_slash"
  #      )
 #   ],
#}

#decor_right = {
   # "decorations": [
 #       PowerLineDecoration(
            #path="arrow_right"
  #           path="rounded_right"
            # path="forward_slash"
            # path="back_slash"
    #    )
    #],
#}



# --------------------------------------------------------
                    #### WIDGETS ####
# --------------------------------------------------------

widget_list = [

            #widget.Prompt(),



            #widget.Image(
             #   filename = "~/.config/qtile/hacker_hat.png",
             #   mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('nitrogen')}, 
                #background=colors[1], 
             #   background=("#000000.0"),
                #foreground=colors[3],
             #   ),
              



            widget.GroupBox(
                fontsize = 20, 
                background=("#000000.0"),
                #background=colors[3],
                active=colors[3],
                inactive=colors[7],
                highlight_color = colors[2],
                this_current_screen_border = colors[3],
                highlight_method = 'black',
                rounded = True,
                borderwidth = 3,
                center_aligned = True,
                hide_unused = False,
                disable_drag = True,
                ),





            widget.Spacer(
                #background=colors[1],
                background=("#000000.0"),
                length=2,
                ),



            widget.CurrentLayoutIcon(

                use_mask= True,
                font="Font Awesome 6 Brands Bold",
                background=("#000000.0"),
                #background=colors[1],
                foreground=colors[3],
                padding = 7,
                scale=0.8,
                ),
             


            widget.Spacer(
                background=("#000000.0"),
                ),


            widget.TextBox(
                text = '  󰸉 ',
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('nitrogen')}, 
                font = "FiraCode Nerd Font Bold",
                background=("#000000.0"),
                foreground = colors[3],
                #background = colors[0],
                padding = 3,
                fontsize = 20,
                ),
 
              
            

            widget.WindowName(
                foreground=colors[7],
                background=("#000000.0"),
                width=bar.CALCULATED,
                empty_group_string="Desktop",
                #background=colors[0],
                max_chars = 35,
                ), 
                    
             widget.Pomodoro(
                background=("#000000.0"),
                foreground = colors[7],
                color_inactive = colors[3],
                prefix_inactive = '  ',
                prefix_paused = '  ',
                prefix_active = ' 󰜎 ',
                prefix_break = ' 󱫞 ',
                prefix_long_break = ' 󰒲 ',
                #color_active =
                notification_on = True,
                fontsize=None,
                font = "FiraCode Nerd Font Bold",
                scroll_delay=0,
                #padding=0,
                length_pomodori=25, 
                ),      

            widget.Spacer(
                #background=colors[0],
                background=("#000000.0"),
                ),



            widget.Systray(
                background=("#000000.0"),
                #background=colors[0],
                icon_size=22,
                padding=5,
                ),



            widget.TextBox(
                text = '  ',
                font = "FiraCode Nerd Font Bold",
                foreground = colors[3],
                background=("#000000.0"),
                #background = colors[0],
                padding = 5,
                fontsize = 20,
                ),
            
            
            
                         
            widget.CheckUpdates(
				distro='Arch',
                background=("#000000.0"),
                #background=colors[0],
				colour_have_updates=colors[7],
				colour_no_updates=colors[7],
				display_format='{updates} ',
                no_update_string= ' 0 ',
                ),


            widget.TextBox(
                text = '  ',
                font = "FiraCode Nerd Font Bold",
                foreground = colors[3],
                background=("#000000.0"),
                #background = colors[0],
                #padding = 1,
                fontsize = 20,
                ),



            widget.CPU(
                format = '{load_percent}%',
                foreground = colors[7],
                background=("#000000.0"),
                #background = colors[0],
                ),



            widget.TextBox(
                text = '  󰋊',
                font = "FiraCode Nerd Font Bold",
                foreground = colors[3],
                background=("#000000.0"),
                #background = colors[0],
                padding = 5,
                fontsize = 20,
                ),



             widget.DF(
                update_interval = 60,
                foreground = colors[7],
                background=("#000000.0"),
                #background = colors[0],
                format = '{uf}{m}',
                fmt = '{} ',
                visible_on_warn = False,
                ),



            widget.TextBox(
                text = ' 󰧑 ',
                font = "FiraCode Nerd Font Bold",
                foreground = colors[3],
                background=("#000000.0"),
                #background = colors[0],
                #padding = 1,
                fontsize = 20,
                ),



		    widget.Memory(
                format='{MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}', 
				measure_mem='G',
                foreground=colors[7], 
                background=("#000000.0"),
				#background=colors[0],
                ),



                



            widget.TextBox(
                text = '  󰕾 ',
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("scripts/volume_slide.sh")},
                font = "FiraCode Nerd Font Bold",
                foreground = colors[3],
                background=("#000000.0"),
                #background = colors[0],
                #padding = 5,
                fontsize = 20,
                ),



            widget.Volume(
                foreground = colors[7],
                background=("#000000.0"),
                #background = colors[0],
                fmt = '{}',
                ),



            widget.TextBox(
                text = '   ',
                font = "FiraCode Nerd Font Bold",
                foreground = colors[3],
                background=("#000000.0"),
                #background = colors[0],
                #padding = 6,
                fontsize = 20,
                ),



            widget.Clock(
                format="%H:%M",
                foreground= colors[7],
                background=("#000000.0"),
                #background=colors[0],
                ),


            
            widget.Clock(
                format=" - %A -",
                foreground= colors[7],
                background=("#000000.0"),
                #background=colors[0],
                ),



            widget.TextBox(
                text = '  ',
                font = "FiraCode Nerd Font Bold",
                foreground = colors[3],
                background=("#000000.0"),
                #background = colors[0],
                #padding = 6,
                fontsize = 20,
                ),



            widget.Clock(
                format="%d/%m/%Y ",
                foreground= colors[7],
                background=("#000000.0"),
                #background=colors[0],
                ),



            widget.TextBox(
                text="", 
                fontsize = 30, 
                font = "FiraCode Nerd Font Mono", 
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("scripts/powermenu.sh")}, 
                foreground = colors[7],
                padding=10,
                background=("#000000.0"),
                #background=colors[3],
                ),
]


# --------------------------------------------------------
                    #### SCREENS ####
# --------------------------------------------------------
screens = [
    Screen(
        top=bar.Bar(
            widget_list,
            30,
            padding=20,
            opacity=0.7,
            border_width=[0, 0, 0, 0],
            margin=[10,40,10,40],
            background="#000000.3",
        ),
    ),
]



# --------------------------------------------------------
            #### DRAG FLOATING LAYOUTS ####
# --------------------------------------------------------
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]



# --------------------------------------------------------
            #### DEFINE FLOATING LAYOUTS ####
# --------------------------------------------------------
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False

floating_layout = layout.Floating(**layout_theme,

    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="download"),    
        Match(wm_class="notification"), 
        Match(wm_class="toolbar"),     
        Match(wm_class="error"),       
        Match(wm_class="confirmreset"), 
        Match(wm_class="makebranch"),   
        Match(wm_class="maketag"),      
        Match(wm_class="ssh-askpass"),  
        Match(wm_class="file_progress"),
        Match(wm_class="splash"),
        Match(wm_class="feh"),
        Match(wm_class="Galculator"),
        #Match(wm_class="openrgb"),
        Match(wm_class="ckb-next"),
        #Match(wm_class="xfce4-terminal"),
        Match(wm_class="nitrogen"),
        Match(wm_class="pinentry"),
        Match(wm_class="ark"),
        Match(wm_class="nemo-preview-start"),
        Match(wm_class="nwg-look"),
        Match(wm_class="steam"),




        


        ],
)



# --------------------------------------------------------
                #### GENERAL SETUP ####
# --------------------------------------------------------

auto_fullscreen = True
focus_on_window_activation = "focus"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None


# --------------------------------------------------------
            #### WINDOW MANAGER NAME ####
# --------------------------------------------------------

wmname = "Qtile"
