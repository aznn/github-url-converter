"""
This module is the CLI interface for the converter

Author: Ahmed Azaan Hassan (azaan@outlook.com) 2013
        https://github.com/aeonaxan/
"""

import sys
import helpers


def main():
    """Main method for this module"""

    if len(sys.argv) == 2:
        if sys.argv[1].lower() in ("help", "h"):
            printHelp()
            sys.exit(0)
        elif sys.argv[1] == "install":
            helpers.install_git_alias()
            sys.exit(0)

    if len(sys.argv) != 3:
        printHelp()
        sys.exit(1)

    if not helpers.is_repository():
        print "Must be a git repository"
        sys.exit(2)

    remote_name = sys.argv[1]
    protocol = sys.argv[2]

    remotes = helpers.get_remotes()
    remote = helpers.get_remote(sys.argv[1], remotes)

    if remote == None:
        print "Remote {0} does not exists. Valid remotes are:".format(remote_name)
        helpers.print_remotes(remotes)
        sys.exit(3)

    if protocol == "ssh":
        convertSSH(remote)
    elif protocol == "https":
        convertHTTPS(remote)
    else:
        print "Valid protocols are 'https' and 'ssh'"
        sys.exit(5)


def convertSSH(remote):
    """Converts the remote's url to a ssh url"""
    if not helpers.is_https_url(remote[1]):
        if helpers.is_ssh_url(remote[1]):
            print "Remote {0} is already a Github ssh URL".format(remote[0])
        else:
            print "Unrecognized URL for remote. Please see help"
            print "{0} - {1}".format(remote[0], remote[1])

        return

    url_fragments = remote[1].lower().strip('.git').split('/')
    assert len(url_fragments) == 5, "Invalid Github url " + remote[1]

    url = "git@github.com:" + url_fragments[3] + '/' + url_fragments[4] + '.git'

    if helpers.set_git_remote_url(remote[0], url):
        print "Successfully changed {0} URL to [{1}]".format(remote[0], url)
    else:
        print "Unexpected error! could not change the URL"


def convertHTTPS(remote):
    """Converts the remote's url to a ssh url"""
    if not helpers.is_ssh_url(remote[1]):
        if helpers.is_https_url(remote[1]):
            print "Remote {0} is already a Github ssh URL".format(remote[0])
        else:
            print "Unrecognized URL for remote. Please see help"
            print "{0} - {1}".format(remote[0], remote[1])

        return

    url_fragments = remote[1].lower().strip('.git').split(':')
    assert len(url_fragments) == 2, "Invalid github url " + remote[1]

    url = "https://github.com/" + url_fragments[1]

    if helpers.set_git_remote_url(remote[0], url):
        print "Successfully changed {0} URL to [{1}]".format(remote[0], url)
    else:
        print "Unexpected error! could not change the URL"


def printHelp():
    """Prints the usage/help message for the script"""
    print "Usage:"
    print "\tgithub-url-converter <remote_name> <https|ssh protocol to change into>"
    print "\n\tPlease note, this will only work with valid Github URLs"
    print "\tGithub SSH  : git@github.com:username/project.git"
    print "\tGithub HTTPS: https://github.com/username/project"
    print "\n\tTo install github-url-converter as an Alias execute this command"
    print "\tgithub-url-converter install"
    print "\tNow it is aliased globally to 'git convert'"


if __name__ == '__main__':
    main()
