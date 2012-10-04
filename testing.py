
import logging

def printing_callback(results):
    for mname, mresult in sorted(results.iteritems()):
        print mname
        for uri, state in sorted(mresult.iteritems()):
            print ' ', uri, logging.getLevelName(state.state)
            print '   ', state.note

def setUp(test):
    test.globs['printing_callback'] = printing_callback
