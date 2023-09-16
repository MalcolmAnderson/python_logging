import logging
import sys
import getopt

def main(argv):
    print(f"args = {argv}")
    log_level = ''
    opts, args = getopt.getopt(argv, [logging])
    print(f"args = {argv}")
    print(f"opts = {opts}")
          
    
    logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)



    # assuming loglevel is bound to the string value obtained from the
    # command line argument. Convert to upper case to allow the user to
    # specify --log=DEBUG or --log=debug
    # numeric_level = getattr(logging, loglevel.upper(), None)
    # if not isinstance(numeric_level, int):
    #     raise ValueError('Invalid log level: %s' % loglevel)
    # logging.basicConfig(level=numeric_level, ...)

    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')
    logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
    logging.critical("this is a dire warning.")



if __name__ == '__main__':
    main(sys.argv[1:])
    
    
    