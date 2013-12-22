from Cocoa import NSWindowController, NSLog, objc, NSApplication, NSApp
from Foundation import NSObject
from PyObjCTools import AppHelper
import sqlite3


class Media(NSWindowController):
    tableView = objc.IBOutlet()
    conn = None

    def awakeFromNib(self):
        NSLog('awakeFromNib')

    def windowDidLoad(self):
        NSWindowController.windowDidLoad(self)
        NSLog('windowDidLoad')

    def windowShouldClose_(self, sender):
        NSLog('windowShouldClose')
        return True

    def windowWillClose_(self, notification):
        NSLog('windowWillClose')
        AppHelper.stopEventLoop()

    def applicationShouldTerminateAfterLastWindowClosed_(self, sender):
        NSLog('applicationShouldTerminateAfterLastWindowClosed')
        return True


if __name__ == '__main__':
    app = NSApplication.sharedApplication()

    viewController = Media.alloc().initWithWindowNibName_('Media')
    viewController.showWindow_(viewController)

    NSApp.activateIgnoringOtherApps_(True)

    AppHelper.runEventLoop()
