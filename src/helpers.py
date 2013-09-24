import subprocess

def install_git_alias():
    """Installs the github-url-converter as an git alias for convert"""
    cmd = "git config --global --replace-all alias.convert !github-url-converter"
    with open('/dev/null', 'w') as f:
        subprocess.call(cmd.split(), stdout=f, stderr=f)

    print "github-url-converter aliased to git convert"

def is_repository():
    with open('/dev/null', 'w') as f:
        res = subprocess.call(["git", "rev-parse"], stdout=f, stderr=f)
        return res == 0


def set_git_remote_url(remote, url):
    """Sets the git remote url for the given remote
    returns whether the operation succeded"""

    with open('/dev/null', 'w') as f:
        res = subprocess.call(["git", "remote", "set-url", remote, url], stdout=f, stderr=f)
        return res == 0

def get_remotes():
    """Returns a list of remotes and their url's. If there are two urls
    for push and fetch, only one of it will be returned, we assume they
    are the same"""

    p = subprocess.Popen(["git", "remote", "-v"], stdout=subprocess.PIPE)
    out, err = p.communicate()

    if err is not None:
        print "Unexpected error in getting Git remotes (git remove -v)"
        raise err

    remotes = []
    remote_names = []
    for remote in out.split("\n"):
        if len(remote) == 0:
            continue

        remote = tuple(remote.split()[:2])

        if remote[0] in remote_names:
            continue

        remotes.append(remote)
        remote_names.append(remote[0])

    return remotes


def get_remote(remote, remotes):
    """Returns the remote if it exists, else None"""
    for r in remotes:
        if r[0] == remote:
            return r
    return None


def print_remotes(remotes):
    """Prints a list of the given remotes and url"""
    for remote in remotes:
        print "{0} - {1}".format(remote[0], remote[1])


def is_ssh_url(url):
    """Checks whether the github url is a ssh url"""
    # make strict assumptions about the url, better to fail rather break a remote
    return url.find("git@github.com:") == 0

def is_https_url(url):
    """Checks whether the github url is a https url"""
    # make strict assumptions about the url, better to fail rather break a remote
    return url.find("https://github.com/") == 0
