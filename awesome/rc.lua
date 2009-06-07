-- Standard awesome library
require("awful")
-- Theme handling library
require("beautiful")
-- Notification library
require("naughty")
require("wicked")
-- shifty - dynamic tagging library
require("shifty")
-- useful for debugging, marks the beginning of rc.lua exec
print("Entered rc.lua: " .. os.time())

-- Execute command and return its output. You probably won't only execute commands with one
-- line of output
function execute_command(command)
   local fh = io.popen(command)
   local str = ""
   for i in fh:lines() do
      str = str .. i
   end
   io.close(fh)
   return str
end
-- {{{ Variable definitions
-- Themes define colours, icons, and wallpapers
-- The default is a dark theme
theme_path = "/home/xzap/.config/awesome/themes/default/theme"
-- Uncommment this for a lighter theme
-- theme_path = "/usr/share/awesome/themes/sky/theme"

-- Actually load theme
beautiful.init(theme_path)

-- This is used later as the default terminal and editor to run.
browser = "firefox"
mail = "thunderbird"
terminal = "urxvt"
editor = os.getenv("EDITOR") or "nano"
editor_cmd = terminal .. " -e " .. editor

-- Default modkey.
-- Usually, Mod4 is the key with a logo between Control and Alt.
-- If you do not like this or do not have such a key,
-- I suggest you to remap Mod4 to another key using xmodmap or other tools.
-- However, you can use another modifier like Mod1, but it may interact with others.
modkey = "Mod4"

-- Table of layouts to cover with awful.layout.inc, order matters.
layouts =
{
    awful.layout.suit.tile,
    awful.layout.suit.tile.left,
    awful.layout.suit.tile.bottom,
    awful.layout.suit.tile.top,
    awful.layout.suit.fair,
    awful.layout.suit.fair.horizontal,
    awful.layout.suit.max,
    awful.layout.suit.max.fullscreen,
    awful.layout.suit.magnifier,
    awful.layout.suit.floating
}




-- Table of clients that should be set floating. The index may be either
-- the application class or instance. The instance is useful when running
-- a console app in a terminal like (Music on Console)
--    xterm -name mocp -e mocp
floatapps =
{
    -- by class
    ["mirage"] = true,
    ["volwheel"] = true,
    ["urxvtcnotify"] = true,
    ["totem"] = true,
    ["audacious"] = true,
    ["wine"] = true,
    ["gmplayer"] = true,   
    ["pinentry"] = true,
    ["gimp"] = true,
    ["gmpc"] = true,
    ["MPlayer"] = true,
    ["Rox"] = true,
    ["tilda"] = true,
    ["qq"] = true,
    ["smplayer"] = true,
    ["pinentry"] = true,
    ["gimp"] = true,
    -- by instance
    ["mocp"] = true
}

-- Applications to be moved to a pre-defined tag by class or instance.



-- Define if we want to use titlebar on all applications.
use_titlebar = false
-- }}}
--{{{ SHIFTY: configured tags
shifty.config.tags = {
    ["1"] =     { layout = awful.layout.suit.max,          mwfact=0.60, exclusive = false, solitary = false, position = 1, init = true, screen = 1, slave = true } ,
    ["web"] =    { layout = awful.layout.suit.tile.bottom,  mwfact=0.65, exclusive = true , solitary = true , position = 4, spawn = "firefox"  } ,
    ["mail"] =   { layout = awful.layout.suit.tile,         mwfact=0.55, exclusive = false, solitary = false, position = 5, spawn = "thunderbird", slave = true     } ,
    ["media"] =  { layout = awful.layout.suit.float,                     exclusive = false, solitary = false, position = 8 } ,
    ["office"] = { layout = awful.layout.suit.tile, position = 9} ,
}
--}}}

--{{{ SHIFTY: application matching rules
-- order here matters, early rules will be applied first
shifty.config.apps = {
         { match = { "Navigator","Vimperator","Gran Paradiso"              } , tag = "web"    } ,
         { match = { "Shredder.*","Thunderbird","mutt"                     } , tag = "mail"   } ,
         { match = { "pcmanfm",                                            } , tag="pcmanfm",slave = true   } ,
         { match = { "OpenOffice.*", "Abiword", "Gnumeric"                 } , tag = "office" } ,
         { match = { "MPlayer.*","gtkpod","Ufraw","easytag"} , tag = "media", nopopup = true } ,
         { match = { "MPlayer", "Gnuplot", "galculator" ,"gimp","Mirage",                   } , float = true ,floatBars=false  } ,
    { match = {"Mirage"                         }, tag = { "graph", "Mirage" }           },
         { match = { terminal                                              } , tag="urxvt", honorsizehints = false, slave = true   } ,
  { match = { "htop", "Wicd", "jackctl"       }, tag = "sys",        screen = 1,     },

        { match = {"foobar2000.exe",                }, tag = "fb",           nopopup = true, },
        { match = {"Ardour.*", "Jamin",             }, tag = "ardour",                       },
        { match = {"Live.*",                        }, tag = "live",         nopopup = true, },
        { match = {"Deluge","nicotine","rtorrent"              }, tag = "p2p",                          },
        { match = {"Gimp","Ufraw"                   }, tag = { "graph", "gimp" }             },
        { match = {"gimp-image-window"              }, slave = true,                         },
        { match = {"gqview"                         }, tag = { "graph", "gqview" }           },
        { match = {"gedit"                         }, tag = { "gedit", }          },
    
        { match = {"gcolor2", "xmag"                }, intrusive = true,                     },
        { match = {"gcolor2"                        }, geometry = { 100,100,nil,nil },       },
        
        { match = { "" }, buttons = {
                             button({ }, 1, function (c) client.focus = c; c:raise() end),
                             button({ modkey }, 1, function (c) awful.mouse.client.move() end),
                             button({ modkey }, 3, awful.mouse.client.resize ), }, },

}
--}}}

--{{{ SHIFTY: default tag creation rules
-- parameter description
--  * floatBars : if floating clients should always have a titlebar
--  * guess_name : wether shifty should try and guess tag names when creating new (unconfigured) tags
--  * guess_position: as above, but for position parameter
--  * run : function to exec when shifty creates a new tag
--  * remember_index: ?
--  * all other parameters (e.g. layout, mwfact) follow awesome's tag API
shifty.config.defaults={  
  layout = awful.layout.suit.tile.bottom, 
  ncol = 1, 
  mwfact = 0.60,
 -- floatBars=true,
  guess_name=true,
  guess_position=true,
  run = function(tag) 
    local stitle = "Shifty Created: "
    stitle = stitle .. (awful.tag.getproperty(tag,"position") or shifty.tag2index(mouse.screen,tag))
    stitle = stitle .. " : "..tag.name
    naughty.notify({ text = stitle })
  end,
}
--}}}




--{{{xzaptext
xzaptextbox=widget({ type = "textbox", align = "right" })
xzaptextbox.text="| Firefox |"
xzaptextbox:buttons( awful.util.table.join(awful.button({ }, 1, function () awful.util.spawn("firefox") end)))
xzaptextbox2=widget({ type = "textbox", align = "right" })
xzaptextbox2.text="| Pcmanfm |"
xzaptextbox2:buttons( awful.util.table.join(awful.button({ }, 1, function () awful.util.spawn("pcmanfm") end)))
xzaptextbox3=widget({ type = "textbox", align = "left" })
xzaptextbox3.text=" " .. execute_command("mpc | grep volume| cut -f 2 -d : | cut -d% -f1") .. "%"
xzaptextbox3:buttons( awful.util.table.join(
               awful.button({ }, 1, function () awful.util.spawn("mpc toggle") end),
                awful.button({ }, 3, function () awful.util.spawn("lrcdis -m notify") end),
               awful.button({ }, 2, function () awful.util.spawn("killall lrcdis") end),
              awful.button({ }, 4, function () awful.util.spawn("mpc volume +3") 
xzaptextbox3.text=" " .. execute_command("mpc | grep volume| cut -f 2 -d : | cut -c1-4") .. "" end),

              awful.button({ }, 5, function () awful.util.spawn("mpc volume -3") 
xzaptextbox3.text=" " .. execute_command("mpc | grep volume| cut -f 2 -d : | cut -c1-4") .. "" end)
))

--wicked


--mpd
mpdwidget = widget({
    type = 'textbox',
    name = 'mpdwidget'
})
mpdwidget:buttons( awful.util.table.join(
               awful.button({ }, 1, function () awful.util.spawn("mpc next") 
xzaptextbox3.text=" " .. execute_command("mpc | grep volume| cut -f 2 -d : | cut -c1-4") .. ""
end),
                 awful.button({ }, 3, function () awful.util.spawn("mpc prev") end),
               awful.button({ }, 2, function () awful.util.spawn("mpc random") end),
              awful.button({ }, 4, function () awful.util.spawn("mpc seek +3") end),

              awful.button({ }, 5, function () awful.util.spawn("mpc seek -3") end)



))
wicked.register(mpdwidget, wicked.widgets.mpd, 
	function (widget, args)
		   if args[1]:find("volume:") == nil then
		      return ' <span color="white"> '..args[1].."</span>"
		   else
                      return ''
                   end
		end)
--Memory 
memwidget = widget({
    type = 'textbox',
    name = 'memwidget',align="right"
})

wicked.register(memwidget, wicked.widgets.mem,
    ' <span color="white">Memory:</span> $1 ($2Mb/$3Mb)')



--CPU Usage 
cpuwidget = widget({
    type = 'textbox',
    name = 'cpuwidget',align="right"
})

wicked.register(cpuwidget, wicked.widgets.cpu,
    ' <span color="white">CPU:</span> $1%')
--Filesystem
fswidget = widget({
    type = 'textbox',
    name = 'fswidget',align="right"
})

wicked.register(fswidget, wicked.widgets.fs,
    ' <span color="white">FS:</span> ${/ used}/${/ size} (${/ usep} used)', 120)
--[[vol
volumewidget2 = widget({
    type = 'textbox',
    name = 'volumewidget2'
})

function amixer_volume(format)
   local f = io.popen('amixer get PCM')
   local l = f:lines()
   local v = ''

   for line in l do
       if line:find('Front Left:') ~= nil then
            pend = line:find('%]', 0, true)
            pstart = line:find('[', 0, true)
            v = line:sub(pstart+1, pend)
       end
   end

   f:close()

   return {v}
end

wicked.register(volumewidget2, amixer_volume, "<span color='white'>Volume</span>: $1", 4)
--]]
--Network
netwidget = widget({
    type = 'textbox',
    name = 'netwidget',align="right"
})

wicked.register(netwidget, wicked.widgets.net, 
  --  ' <span color="white">NET</span>: ${eth0 down} / ${eth0 up} [ ${eth0 rx} //  ${eth0 tx} ]',nil, nil, 3)
 ' <span color="white">NET</span>: ${eth0 down} / ${eth0 up} ',nil, nil, 3)
-- ,height="16"




--xzapstop



-- {{{ Wibox
-- Create a textbox widget
mytextbox = widget({ type = "textbox", align = "right" })
-- Set the default text in textbox
mytextbox.text = "<b><small> " .. AWESOME_RELEASE .. " </small></b>"

-- Create a laucher widget and a main menu
myawesomemenu = {
   { "manual", terminal .. " -e man awesome" },
   { "edit config", editor_cmd .. " " .. awful.util.getdir("config") .. "/rc.lua" },
   { "restart", awesome.restart },
   { "quit", awesome.quit }
}
myluncher={
{"firefox","firefox"},
{"audacious","audacious"},
{"pcmanfm","pcmanfm"},
{"gmpc","gmpc"},
{"thunderbird","thunderbird"},
{"qq","qq"}
}

mymainmenu = awful.menu.new({ items = { { "awesome", myawesomemenu, beautiful.awesome_icon },
 { "my luncher", myluncher },                                       
{ "open terminal", terminal }
                                      }
                            })

mylauncher = awful.widget.launcher({ image = image(beautiful.awesome_icon),
                                     menu = mymainmenu })

-- Create a systray
mysystray = widget({ type = "systray", align = "right" })

-- Create a wibox for each screen and add it
mywibox = {}
mywibox2 = {}
mypromptbox = {}
mylayoutbox = {}
mytaglist = {}
mytaglist.buttons = awful.util.table.join(
                    awful.button({ }, 1, awful.tag.viewonly),
                    awful.button({ modkey }, 1, awful.client.movetotag),
                    awful.button({ }, 3, function (tag) tag.selected = not tag.selected end),
                    awful.button({ modkey }, 3, awful.client.toggletag),
                    awful.button({ }, 4, awful.tag.viewnext),
                    awful.button({ }, 5, awful.tag.viewprev)
                    )
mytasklist = {}
mytasklist.buttons = awful.util.table.join(
                     awful.button({ }, 1, function (c)
                                              if not c:isvisible() then
                                                  awful.tag.viewonly(c:tags()[1])
                                              end
                                              client.focus = c
                                              c:raise()
                                          end),
                     awful.button({ }, 2, function (c) c:kill()                         end),
                     awful.button({ }, 3, function ()
                                              if instance then
                                                  instance:hide()
                                                  instance = nil
                                              else
                                                  instance = awful.menu.clients({ width=250 })
                                              end
                   
                       end),

                     awful.button({ }, 4, function ()
                                              awful.client.focus.byidx(1)
                                              if client.focus then client.focus:raise() end
                                          end),
                     awful.button({ }, 5, function ()
                                              awful.client.focus.byidx(-1)
                                              if client.focus then client.focus:raise() end
                                          end))

for s = 1, screen.count() do
    -- Create a promptbox for each screen
    mypromptbox[s] = widget({ type = "textbox", align = "left" })
    -- Create an imagebox widget which will contains an icon indicating which layout we're using.
    -- We need one layoutbox per screen.
    mylayoutbox[s] = widget({ type = "imagebox", align = "right" })
    mylayoutbox[s]:buttons(awful.util.table.join(
                           awful.button({ }, 1, function () awful.layout.inc(layouts, 1) end),
                           awful.button({ }, 3, function () awful.layout.inc(layouts, -1) end),
                           awful.button({ }, 4, function () awful.layout.inc(layouts, 1) end),
                           awful.button({ }, 5, function () awful.layout.inc(layouts, -1) end)))
    -- Create a taglist widgetnetwidget,


    mytaglist[s] = awful.widget.taglist.new(s, awful.widget.taglist.label.all, mytaglist.buttons)

    -- Create a tasklist widget
    mytasklist[s] = awful.widget.tasklist.new(function(c)
                                                  return awful.widget.tasklist.label.currenttags(c, s)
                                              end, mytasklist.buttons)

    -- Create the wibox
    mywibox[s] = wibox({ position = "top", fg = beautiful.fg_normal, bg = beautiful.bg_normal })
    -- Add widgets to the wibox - order matters
    mywibox[s].widgets = { mylauncher,
                           mytaglist[s],
                           mytasklist[s],
                           mypromptbox[s],                           
                           s == 1 and mysystray or nil,
                           mytextbox,
                           mylayoutbox[s],
                                }
    mywibox[s].screen = s
--xzao wibox{{{
 -- Create the wibox
    mywibox2[s] = wibox({ position = "bottom", fg = beautiful.fg_normal, bg = beautiful.bg_normal,height=20 })
    -- Add widgets to the wibox - order matters
        mywibox2[s].widgets = {   
xzaptextbox3,      
        netwidget,
         mpdwidget,
         --volumewidget2,
        --volumewidget,
        cpuwidget,
        memwidget,
        xzaptextbox2,

xzaptextbox,
--fswidget

 }
    mywibox2[s].screen = s

--xzap-stop}}}
end
-- }}}
--{{{ SHIFTY: initialize shifty
-- the assignment of shifty.taglist must always be after its actually initialized 
-- with awful.widget.taglist.new()
shifty.taglist = mytaglist
shifty.init()
--}}}
-- {{{ Mouse bindings
root.buttons(awful.util.table.join(
    awful.button({ }, 2, function () mymainmenu:toggle() end),
    awful.button({ }, 3, function () awful.util.spawn(terminal) end),
    awful.button({ }, 4, awful.tag.viewnext),
    awful.button({ }, 5, awful.tag.viewprev)
))



-- }}}

-- {{{ Key bindings
globalkeys = awful.util.table.join(
    awful.key({ modkey,           }, "Left",   awful.tag.viewprev       ),
    awful.key({ modkey,           }, "Right",  awful.tag.viewnext       ),
    awful.key({ modkey,           }, "Escape", awful.tag.history.restore),
  -- SHIFTY: keybindings specific to shifty
  awful.key({ modkey, "Shift" }, "d", shifty.del),      -- delete a tag
  awful.key({ modkey, "Shift" }, "n", shifty.send_prev),-- move client to prev tag
  awful.key({ modkey          }, "n", shifty.send_next),-- move client to next tag
  awful.key({ modkey,"Control"}, "n", function() 
    shifty.tagtoscr(awful.util.cycle(screen.count(), mouse.screen +1))
  end),-- move client to next tag
  awful.key({ modkey          }, "a",     shifty.add),  -- creat a new tag
  awful.key({ modkey, "Shift" }, "r",  shifty.rename),  -- rename a tag
  awful.key({ modkey, "Shift" }, "a",                   -- nopopup new tag
    function() 
      shifty.add({ nopopup = true }) 
    end),
    awful.key({ modkey,           }, "j",
        function ()
            awful.client.focus.byidx( 1)
            if client.focus then client.focus:raise() end
        end),
    awful.key({ modkey,           }, "k",
        function ()
            awful.client.focus.byidx(-1)
            if client.focus then client.focus:raise() end
        end),
    awful.key({ modkey,           }, "w", function () mymainmenu:show(true)        end),

    -- Layout manipulation
    awful.key({ modkey, "Shift"   }, "j", function () awful.client.swap.byidx(  1) end),
    awful.key({ modkey, "Shift"   }, "k", function () awful.client.swap.byidx( -1) end),
    awful.key({ modkey, "Control" }, "j", function () awful.screen.focus( 1)       end),
    awful.key({ modkey, "Control" }, "k", function () awful.screen.focus(-1)       end),
    awful.key({ modkey,           }, "u", awful.client.urgent.jumpto),
    awful.key({ modkey,           }, "Tab",
        function ()
            awful.client.focus.history.previous()
            if client.focus then
                client.focus:raise()
            end
        end),

    -- Standard program
    awful.key({ modkey,           }, "Return", function () awful.util.spawn(terminal) end),
    awful.key({ modkey, "Control" }, "r", awesome.restart),
    awful.key({ modkey, "Shift"   }, "q", awesome.quit),

    awful.key({ modkey,           }, "l",     function () awful.tag.incmwfact( 0.05)    end),
    awful.key({ modkey,           }, "h",     function () awful.tag.incmwfact(-0.05)    end),
    awful.key({ modkey, "Shift"   }, "h",     function () awful.tag.incnmaster( 1)      end),
    awful.key({ modkey, "Shift"   }, "l",     function () awful.tag.incnmaster(-1)      end),
    awful.key({ modkey, "Control" }, "h",     function () awful.tag.incncol( 1)         end),
    awful.key({ modkey, "Control" }, "l",     function () awful.tag.incncol(-1)         end),
    awful.key({ modkey,           }, "space", function () awful.layout.inc(layouts,  1) end),
    awful.key({ modkey, "Shift"   }, "space", function () awful.layout.inc(layouts, -1) end),

    -- Prompt
    awful.key({ modkey }, "r",
              function ()
                  awful.prompt.run({ prompt = "Run: " },
                  mypromptbox[mouse.screen],
                  awful.util.spawn, awful.completion.shell,
                  awful.util.getdir("cache") .. "/history")
              end),

    awful.key({ modkey }, "x",
              function ()
                  awful.prompt.run({ prompt = "Run Lua code: " },
                  mypromptbox[mouse.screen],
                  awful.util.eval, nil,
                  awful.util.getdir("cache") .. "/history_eval")
              end),
--xzap-start
 awful.key({ modkey }, "b", 
       function () 
      if mywibox[mouse.screen].screen == nil then 
         mywibox[mouse.screen].screen = mouse.screen
     else
         mywibox[mouse.screen].screen = nil
     end
 end),
 awful.key({ modkey }, "v", 
       function () 
      if mywibox2[mouse.screen].screen == nil then 
         mywibox2[mouse.screen].screen = mouse.screen
     else
         mywibox2[mouse.screen].screen = nil
     end
 end),
awful.key({ modkey }, "F12", function () awful.util.spawn("xkill") end),
awful.key({ }, "XF86AudioRaiseVolume", function () awful.util.spawn("amixer set Master 2%+") end),
awful.key({ }, "XF86AudioLowerVolume", function () awful.util.spawn("amixer set Master 2%-") end),
awful.key({ }, "XF86AudioMute", function () awful.util.spawn("amixer set Master 0") end)

--xzap-end
)

-- Client awful tagging: this is useful to tag some clients and then do stuff like move to tag on them
clientkeys = awful.util.table.join(
    awful.key({ modkey,           }, "f",      function (c) c.fullscreen = not c.fullscreen  end),
    awful.key({ modkey, "Shift"   }, "c",      function (c) c:kill()                         end),
    awful.key({ modkey, "Control" }, "space",  awful.client.floating.toggle                     ),
    awful.key({ modkey, "Control" }, "Return", function (c) c:swap(awful.client.getmaster()) end),
    awful.key({ modkey,           }, "o",      awful.client.movetoscreen                        ),
    awful.key({ modkey, "Shift"   }, "r",      function (c) c:redraw()                       end),
    awful.key({ modkey }, "t", awful.client.togglemarked),
    awful.key({ modkey,}, "m",
        function (c)
            c.maximized_horizontal = not c.maximized_horizontal
            c.maximized_vertical   = not c.maximized_vertical
        end)
  
)
-- SHIFTY: assign client keys to shifty for use in
-- match() function (manage hook)
shifty.config.clientkeys = clientkeys
shifty.config.modkey = modkey
--}}}

-- Compute the maximum number of digit we need, limited to 9
for i=1, ( shifty.config.maxtags or 9 ) do
  table.insert(globalkeys, key({ modkey }, i, 
  function () 
    local t =  awful.tag.viewonly(shifty.getpos(i)) 
  end))
  table.insert(globalkeys, key({ modkey, "Control" }, i, 
  function () 
    local t = shifty.getpos(i)
    t.selected = not t.selected 
  end))
  table.insert(globalkeys, key({ modkey, "Control", "Shift" }, i, 
  function () 
    if client.focus then 
      awful.client.toggletag(shifty.getpos(i)) 
    end
  end))
  -- move clients to other tags
  table.insert(globalkeys, key({ modkey, "Shift" }, i,
    function () 
      if client.focus then 
        t = shifty.getpos(i)
        awful.client.movetotag(t)
        awful.tag.viewonly(t)
      end 
    end))
end




-- Set keys
root.keys(globalkeys)
-- }}}
-- Autostart
function autostart(dir)
    if not dir then
        do return nil end
    end
    local fd = io.popen("ls -1 -F " .. dir)
    if not fd then
        do return nil end
    end
    for file in fd:lines() do
        local c= string.sub(file,-1)   -- last char
        if c=='*' then  -- executables
            executable = string.sub( file, 1,-2 )
            print("Awesome Autostart: Executing: " .. executable)
            os.execute(dir .. "/" .. executable .. " &") -- launch in bg
        elseif c=='@' then  -- symbolic links
            print("Awesome Autostart: Not handling symbolic links: " .. file)
        else
            print ("Awesome Autostart: Skipping file " .. file .. " not executable.")
        end
    end
    io.close(fd)
end

autostart_dir = os.getenv("HOME") .. "/.config/awesome/autostart"
autostart(autostart_dir)
-- {{{ Hooks
-- Hook function to execute when focusing a client.
awful.hooks.focus.register(function (c)
    if not awful.client.ismarked(c) then
        c.border_color = beautiful.border_focus
    end
end)

-- Hook function to execute when unfocusing a client.
awful.hooks.unfocus.register(function (c)
    if not awful.client.ismarked(c) then
        c.border_color = beautiful.border_normal
    end
end)

-- Hook function to execute when marking a client
awful.hooks.marked.register(function (c)
    c.border_color = beautiful.border_marked
end)

-- Hook function to execute when unmarking a client.
awful.hooks.unmarked.register(function (c)
    c.border_color = beautiful.border_focus
end)

-- Hook function to execute when the mouse enters a client.
awful.hooks.mouse_enter.register(function (c)
    -- Sloppy focus, but disabled for magnifier layout
    if awful.layout.get(c.screen) ~= awful.layout.suit.magnifier
        and awful.client.focus.filter(c) then
        client.focus = c
    end
end)

-- Hook function to execute when a new client appears.
awful.hooks.manage.register(function (c, startup)
    -- If we are not managing this application at startup,
    -- move it to the screen where the mouse is.
    -- We only do it for filtered windows (i.e. no dock, etc).
    if not startup and awful.client.focus.filter(c) then
        c.screen = mouse.screen
    end

    if use_titlebar then
        -- Add a titlebar
        awful.titlebar.add(c, { modkey = modkey })
    end
    -- Add mouse bindings
    c:buttons(awful.util.table.join(
        awful.button({ }, 1, function (c) client.focus = c; c:raise() end),
        awful.button({ modkey }, 1, awful.mouse.client.move),
        awful.button({ modkey }, 3, awful.mouse.client.resize)
    ))
    -- New client may not receive focus
    -- if they're not focusable, so set border anyway.
    c.border_width = beautiful.border_width
    c.border_color = beautiful.border_normal

    -- Check if the application should be floating.
    local cls = c.class
    local inst = c.instance
    if floatapps[cls] then
        awful.client.floating.set(c, floatapps[cls])
    elseif floatapps[inst] then
        awful.client.floating.set(c, floatapps[inst])
    end

    -- Check application->screen/tag mappings.
    local target
    if apptags[cls] then
        target = apptags[cls]
    elseif apptags[inst] then
        target = apptags[inst]
    end
    if target then
        c.screen = target.screen
        awful.client.movetotag(tags[target.screen][target.tag], c)
    end

    -- Do this after tag mapping, so you don't see it on the wrong tag for a split second.
    client.focus = c

    -- Set key bindings
    c:keys(clientkeys)

    -- Set the windows at the slave,
    -- i.e. put it at the end of others instead of setting it master.
    -- awful.client.setslave(c)

    -- Honor size hints: if you want to drop the gaps between windows, set this to false.
    -- c.size_hints_honor = false
end)

-- Hook function to execute when arranging the screen.
-- (tag switch, new client, etc)
awful.hooks.arrange.register(function (screen)
    local layout = awful.layout.getname(awful.layout.get(screen))
    if layout and beautiful["layout_" ..layout] then
        mylayoutbox[screen].image = image(beautiful["layout_" .. layout])
    else
        mylayoutbox[screen].image = nil
    end

    -- Give focus to the latest client in history if no window has focus
    -- or if the current window is a desktop or a dock one.
    if not client.focus then
        local c = awful.client.focus.history.get(screen, 0)
        if c then client.focus = c end
    end
end)

-- Hook called every minute
awful.hooks.timer.register(60, function ()

    mytextbox.text = os.date(" %a %b %d, %H:%M ")
end)
-- }}}
