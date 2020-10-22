import argparse

from santa import Santa

SLED_MAX_CAPACITY = 12
DEFAULT_NUMBER_OF_PRESENTS = 20


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Call Santa to deliver presents.')
    parser.add_argument('--n-presents', metavar='N', type=int, help='Number of presents',
                        default=DEFAULT_NUMBER_OF_PRESENTS)

    args = parser.parse_args()

    n_presents = args.n_presents

    our_santa = Santa(n_presents)
    our_santa.distribute_presents()
