# DEPRECATED -- WILL BE REMOVED IN FUTURE VERSION

import os
import pprint
import subprocess
import traceback
import argparse

argparser = None

def run(args, javac_commands, jars):
    # print os.environ['CLASSPATH']
    processor_cp = os.environ['CLASSPATH']
    # checker-framework javac.
    javacheck = os.environ['JSR308']+"/checker-framework/checker/bin/javac"
    checker_command = [javacheck, "-processor", args.checker]

    for jc in javac_commands:
        pprint.pformat(jc)
        javac_switches = jc['javac_switches']
        cp = javac_switches['classpath']
        cmd = checker_command + ["-classpath", cp+":"+processor_cp]
        cmd.extend(jc['java_files'])
        print ("Running %s" % cmd)
        try:
            print (subprocess.check_output(cmd, stderr=subprocess.STDOUT))
        except subprocess.CalledProcessError as e:
            print e.output
