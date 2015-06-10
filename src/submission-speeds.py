import sys
import os
import time
import printapp
from printapp import printstatus, oauthcredentials, cloudprint

with printapp.app.app_context():
    username = os.getenv('UNIFLOW_USER')
    password = os.getenv('UNIFLOW_PASSWORD')
    email = '{}@students.calvin.edu'.format(username)
    base_path = os.path.abspath(os.path.dirname(__file__))
    token = oauthcredentials.get_token(email)

    start = time.time()
    result = cloudprint.has_uniflow_printer(token=token)
    time_elapsed = time.time() - start
    if (result != True):
        print "Error. Account does not have uniflow printer."
        sys.exit(0)
    else:
        print "has_uniflow_printer() took " + str(time_elapsed) + " seconds."

    #TODO: add more files of varying file sizes.
    file_names = ['a.txt', 'test.txt', 'test.docx', 'test.doc', 'test.pdf']
    for name in file_names:
        path = os.path.join(base_path, 'printapp/test/docs', name)
        test_file = open(path, 'rb')
        start = time.time()
        cloudprint.submit_job(token, test_file,
                              color=False, duplex=True,
                              copies=1, collate=False)
        time_elapsed = time.time() - start
        file_size = os.fstat(test_file.fileno()).st_size
        print "Submitting " + name + " (" + str(file_size) + " Bytes) took " + str(time_elapsed) + " seconds."
        test_file.close()


