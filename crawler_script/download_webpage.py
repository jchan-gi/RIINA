from __future__ import print_function

try:
    from pywinauto import application
except ImportError:
    import os.path
    pywinauto_path = os.path.abspath(__file__)
    pywinauto_path = os.path.split(os.path.split(pywinauto_path)[0])[0]
    import sys
    sys.path.append(pywinauto_path)
    from pywinauto import application

from pywinauto.controls.hwndwrapper import HwndWrapper

import sys
import time
import os.path

from pywinauto import WindowAmbiguousError

if len(sys.argv) < 2:
    print("please specify a web address to download")
    sys.exit()

web_address = sys.argv[1]

if len(sys.argv) > 2:
    outputfilename = sys.argv[2]
else:
    outputfilename = web_address
    outputfilename = outputfilename.replace('/', '')
    outputfilename = outputfilename.replace('\\', '')
    outputfilename = outputfilename.replace(':', '')
    if not (outputfilename.lower().endswith("htm") or
        outputfilename.lower().endswith("html")):
        outputfilename += ".html"

# make sure that we have an absolute path - otherwise it is
# hard to know where firefox might save the file!
outputfilename = os.path.abspath(outputfilename)

# start IE with a start URL of what was passed in
app = application.Application().start(
    r"C:\Program Files\Mozilla Firefox\firefox.exe {}".format(web_address))

# some pages are slow to open - so wait some seconds
time.sleep(5)

# mozilla is one of thos applications that use existing windows
# if they exist (at least on my machine!)
# so if we cannot find any window for that process
#  - find the actual process
#  - connect to it
#print(sys.argv[3])
if app.windows():
    mozilla = app.window(title_re=sys.argv[3])

else:
    app = application.Application().connect(title_re=sys.argv[3], visible_only=True)
    mozilla = app.window(title_re=sys.argv[3])

# ie doesn't define it's menus as Menu's but actually as a toolbar!
# print("No Menu's in FireFox:", mozilla.menu_items())

time.sleep(2)

try:
    # File -> Save As
    mozilla.type_keys("^S")
    time.sleep(3)
    #ie.Toolbar3.press_button("File")
    app.SaveAs.Edit.set_edit_text(outputfilename)
    time.sleep(1)
    app.SaveAs.Save.close_click()

    time.sleep(3)

    # if asked to overwrite say yes
    if app.SavePageAs.Yes.exists():
        app.SavePageAs.Yes.close_click()
except WindowAmbiguousError as e:
    for w in e.windows:
        w = HwndWrapper(w)
        print(w.window_text(), w.class_name())

#print("saved:", outputfilename)

# File close tab or close
#(Firefox makes it easy for us having the same shortcut for both!
#mozilla.type_keys("%F")
#mozilla.type_keys("C")
finally:
    mozilla.type_keys("%{F4}")
