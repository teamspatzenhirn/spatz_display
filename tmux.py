import libtmux
from libtmux.exc import BadSessionName, LibTmuxException


class tmux_server:
    def __init__(self):
        self.server = libtmux.Server(socket_path="tmp/tmux-spatz")
        self.session = self.server.new_session()
        try :
            self.session.rename_session("spatz")
        except LibTmuxException: # this should kill an old session so we don't start the stack in multiple sessions
            old_session = self.server.sessions.get(name="spatz")
            old_session.kill_session()
            self.session.rename_session("spatz")
        self.pane = self.session.active_window.active_pane #should only be 1
        self.previous_pane_len = 0


    def start_stack(self, launchfile: str):
        self.pane.send_keys("cd $HOME/ade-home/2021/")
        self.pane.send_keys("ade stop")
        self.pane.send_keys("ade start")
        self.pane.send_keys("ade enter")
        self.pane.send_keys("cd 2021")
        self.pane.send_keys("source install/setup.zsh")
        self.pane.send_keys("ros2 launch teamspatzenhirn_launch " + launchfile)

    def get_new_content(self) -> list[str]:
        entire_pane = self.pane.capture_pane(start="-")
        diff : list[str] = []
        #this looks dumb but this is honestly faster and more consistent than any other way to check for changes
        if entire_pane.__len__() != self.previous_pane_len:
            diff = (entire_pane[self.previous_pane_len-entire_pane.__len__():])
        self.previous_pane_len = entire_pane.__len__()
        return diff
