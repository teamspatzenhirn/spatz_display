import libtmux

class tmux_server:
    def __init__(self):
        self.server = libtmux.Server(socket_path="tmp/tmux-spatz")
        self.session = self.server.new_session()
        self.session.rename_session("spatz")
        self.pane = self.session.active_window.active_pane #should only be 1

    def start_stack(self, launchfile: str):
        self.pane.send_keys("cd /home/corneliustiefenmoser/ade-home/2021/")
        self.pane.send_keys("ade stop")
        self.pane.send_keys("ade start")
        self.pane.send_keys("ade enter")
        self.pane.send_keys("cd 2021")
        self.pane.send_keys("source install/setup.zsh")
        self.pane.send_keys("ros2 launch teamspatzenhirn_launch " + launchfile)

    def get_text(self) -> list[str]:
        return self.pane.capture_pane()