import requests
import sys
# C-style parser for command line options
import getopt
import json

# Send Slack message using Slack API
def send_slack_message(message):
    # payload = json.dumps(message)
    payload = '{"text": "%s"}' % message
    response = requests.post(
        'https://hooks.slack.com/services/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', data=payload)
    print(response.text)


def main(argv):
    message = ''
    try:
        # short opts are column (:) seperated
        # Using them will require us to at least option from the one between the column (:)
        # = in long opts means you have to pass a value
        # - should be passed by the user for the short opts
        # -- should be passed by the user for the long opts
        opts, args = getopt.getopt(argv, "hm:", ["message=", "help"])
    except getopt.GetoptError:
        print("Options error")
        sys.exit(2)
    if len(opts) == 0:
        print("Missing option(s). Try with -h for usage info.")
        sys.exit()
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            # Usage helper
            print('Usage: driver.py -m "<message>"')
            sys.exit()
        elif opt in ("-m", "--message"):
            message = arg
    send_slack_message(message)

if __name__ == "__main__":
    # First argument is the file name, while the rest are the options with their values.
    main(sys.argv[1:])
