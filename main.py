from updater4pyi import upd_source, upd_core
from updater4pyi.upd_iface_pyqt4 import UpdatePyQt4Interface



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    swu_source = upd_source.UpdateGithubReleasesSource('githubusername/githubproject')
    swu_updater = upd_core.Updater(current_version=...,
                                   update_source=swu_source)
    swu_interface = UpdatePyQt4Interface(swu_updater,
                                         progname='Your Project Name',
                                         ask_before_checking=True,
                                         parent=QApplication.instance())