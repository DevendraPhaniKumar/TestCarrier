import os
import sys
import unittest
from unittest import TestSuite
import HtmlTestRunner
import getopt
import time
from fnmatch import fnmatch
import glob, os,shutil


dirnameutils = os.path.dirname(os.path.abspath(__file__))


def usage():
        print ('Usage:\npython Test_Runner.py  <Path of Unit Test Scripts folder for TestSuit Execution>\n')
          
def run_test(path_to_test_module):
    
    abs_path_to_test_module = os.path.abspath(path_to_test_module[0])
    sys.path.insert(0, os.path.dirname(abs_path_to_test_module))
    testname = os.path.basename(abs_path_to_test_module)

    suite = TestSuite()    
    for all_test_suite in unittest.defaultTestLoader.discover(str(path_to_test_module[0]), pattern='*.py'):
        for test_suite in all_test_suite:
            suite.addTests(test_suite)
    
    HtmlTestRunner.HTMLTestRunner(combine_reports=True,output=dirnameutils + "\Results\\"+testname, report_name=testname, report_title="Automation Test Report",add_timestamp=True).run(suite)

def get_consolidate():
    
    time_format = "%Y-%m-%d"
    date = time.strftime(time_format)

    dir_name = dirnameutils + "\\Results\\"
    pattern = "*_"+date+".html"
    output_folder_name = dir_name+'CPENGINE_MB_RESULTS-'+date

    try:
        for txt_file in glob.iglob(dir_name+"\\*.zip"):
            os.remove(txt_file)
    except:
        print ("Folder is Not exist")
                    
    try:
        os.makedirs(output_folder_name) ## it creates the destination folder
    except:
        print ("Folder already exist")
            
    for path, subdirs, files in os.walk(dir_name):
        for name in files:
            if fnmatch(name, pattern):
                print(os.path.join(path, name))
                op_file = os.path.join(path, name)
                #os.remove(op_file)
                filename = os.path.basename(op_file)
                dest = os.path.join(output_folder_name,filename)
                #shutil.move(op_file, dest)
                shutil.copy2(op_file, dest)

    # Create 'path\to\zip_file.zip'
    shutil.make_archive(output_folder_name, 'zip', output_folder_name)     
    
if __name__ == "__main__":
            
    try:
        if sys.argv[1:] == []:
            usage()
            print ('\nTest Terminated.\n')
            sys.exit(2)
    except getopt.GetoptError as err:
        print ('\n Test Terminated.\n')
        sys.exit(2)
    except KeyboardInterrupt:
        print ("\nExecution stop requested...exiting.....")
        sys.exit(0)    
        
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h', ['help'])      
    except getopt.GetoptError:
        usage()
        sys.exit(2)  
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit(2)
           
print ('\nWelcome to Automation Script Execution\n')
print ('Test executing..\n')


#To Run the Test Suit

run_test(sys.argv[1:])


#To Get the Consolidated Results
get_consolidate()

