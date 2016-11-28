import sys
from .tracker_utils import get_repo_info, in_ipynb


def _get_init_info():
    # this gets all the needed information at the beginning of the run
    info = {}

    # open config file, get git repos to be tracked, eventual files that need to be included in the dependencies
    # (e.g. lookup tables, etc.)
    # TODO
    #config file can be 1) in the current directory, named neuroseries.yml,
    # 2) in the 'project' directory (root of the containing git repo
    # 3) in the home directory as .neuroseries/config.yaml
    # 4) at the location pointed to by the variable NEUROSERIES_CONFIG

    # get name of the entry point and the arguments
    import sys
    import os.path
    info['entry_point'] = os.path.realpath(sys.argv[0])
    info['args'] = sys.argv[1:]

    # get git status, if it's a script, this should be completely committed,
    # if it's a notebook everything should be committed
    # except for the notebook itself (which may be committed at the save time) TODO
    repos = []

    script_repo_info, is_dirty, script_repo = get_repo_info(os.path.dirname(info['entry_point']))

    if is_dirty and not in_ipynb():
        raise RuntimeError("""Running from a dirty git repository (and not from a notebook).
        Please commit your changes before running""")

    repos.append(script_repo_info)

    info['repos'] = repos

    # get commit id(s) TODO

    # get venv status TODO

    # get os information TODO

    # get hardware information TODO

    return info

info = _get_init_info()