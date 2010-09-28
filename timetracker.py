#!/usr/bin/env python

import datetime
import getopt
import json
import os
import os.path

DB = os.environ['HOME'] + "/.timetracker/db.json"
DATA = []
DATEINPUTFORMAT = "%Y-%m-%d %H:%M"
DATEISOFORMAT = "%Y-%m-%d %H:%M:%S"

def add(argv):
    global DATA
    
    shortoptions = 't:b:e:c:'
    longoptions = ["tag", "begin", "end", "comment"]
    
    try:
        opts, args = getopt.getopt(argv, shortoptions, longoptions)
    except getopt.GetoptError, err:
        print str(err)

    if "-b" in argv and "-e" in argv:

        tag = ""
        begin = datetime.datetime.today().isoformat(' ')
        end = datetime.datetime.today().isoformat(' ')
        comment = ""

        for o, a in opts:
            if o in ("-t", "--tag"):
                tag = a
            elif o in ("-b", "--begin"):
                begin = datetime.datetime.strptime(a, DATEINPUTFORMAT).isoformat(' ')
            elif o in ("-e", "--end"):
                end = datetime.datetime.strptime(a, DATEINPUTFORMAT).isoformat(' ')
            elif o in ("-c", "--comment"):
                comment = a
            else:
                print "unhandled option"

        entry = {'tag' : tag, 
                 'begin' : begin,
                 'end' : end, 
                 'comment' : comment }

        DATA.append(entry)
    else:
        print "specify -b and -e option for begin and end of entry"

def show(argv):
    for entry in DATA:
        print "%-10s %-26s %-26s %s" %(entry['tag'], entry['begin'], entry['end'], entry['comment'])

def delete(argv):
    print "delete entry"

def help(argv):
    print "timetracker - by core - 2010"
    print "timeformat " + DATEINPUTFORMAT 
    print "pre alpha - more coming soon"

def statistics(argv):
    for entry in DATA:
        time = datetime.datetime.strptime(entry['end'], DATEISOFORMAT) - datetime.datetime.strptime(entry['begin'], DATEISOFORMAT)
        print "total time: " + str(time)

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
        'statistics' : statistics,
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
