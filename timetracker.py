#!/usr/bin/env python

DB = ~/.timetracker/db.json

def main(argv):
    actions = {
        'add' : add,
        'show' : show,
        'delete' : delete,
        'help' : help,
        }

    if len(argv):
        action_id = argv[0]
        if action_id in actions:
            actions[action_id](argv[1:])
        else:
            print "Unknown command, use one of those:"

            for action in actions:
                print "-", action
    else:
        print "Please select a command."
        print

        print "Available:"
        for action in actions:
            print "-", action

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
