#!/usr/bin/env python

import datetime
import json
import os
import os.path

DB = os.environ['HOME'] + "/.timetracker/db.json"
DATA = []

def add(argv):
    global DATA
    print "adding entry"
    entry = {'tag' : "testing", 
             'begin' : datetime.datetime.today().isoformat(' '),
             'end' : "end", 
             'comment' : "comment" }

    DATA.append(entry)

def show(argv):
    print "show entrys"

def delete(argv):
    print "delete entry"

def help(argv):
    print "timetracer - by core - 2010"
    print
    print "pre alpha - more coming soon"

def load_json(io):
    global DATA 
    DATA = json.load(io)

def save_json(io):
    json.dump(DATA, io)

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
            if os.path.exists(DB):
                io = open(DB, 'r')
                load_json(io)
                io.close()

            actions[action_id](argv[1:])

            io = open(DB, 'w')
            save_json(io)
            io.close()
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
