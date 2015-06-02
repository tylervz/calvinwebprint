import sys
import os
import time
import printstatus
import oauthcredentials
import cloudprint

username = os.getenv('UNIFLOW_USER')
password = os.getenv('UNIFLOW_PASSWORD')
email = '{}@students.calvin.edu'.format(username)
path = os.path.abspath(os.path.dirname(__file__))
token = oauthcredentials.get_token(self._email)

start = time.time()
result = cloudprint.has_uniflow_printer(token=self._token)
time_elapsed = time.time() - start
if (result != True):
    print "Error. Account does not have uniflow printer."
    sys.exit(0)
else:
    print "has_uniflow_printer() took " + time_elapsed + " seconds."

ticket = cloudprint._make_print_ticket()

#TODO: add more files of varying file sizes.
file_names = ['test.pdf', 'test.txt', 'test.doc', 'test.docx']
for name in file_names:
    path = os.path.join(path, 'docs', name)
    test_file = open(path, 'rb')
    start = time.time()
    cloudprint.submit_job(self._token, test_file,
                                   color=False, duplex=True,
                                   copies=1, collate=False)
    time_elapsed = time.time() - start
    print "Submitting " + name + " (" + os.fstat(test_file.fileno()).st_size + " Bytes) took " + time_elapsed + " seconds."
    test_file.close()


