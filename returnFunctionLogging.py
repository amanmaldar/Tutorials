
# This functionality is mostly used in logging

def logger():       # logger function just returns the pointer to log_text function
    def log_text(msg):  # this is not executed by logger() function.
        print "Message is: " , msg

    return log_text # this is only line executed by logger() fucntion
    # return the pointer to function log_text. This will be used later just to call log_text fucntions without touching
    # logger() fucntion


data = logger();        # we receive the pointer to log_text fucntion.
data("testing internal function")   # use the pointer along with parameter to call the fucnction.
