import argparse
from examples.task_example import slow_sort_example, faster_sort_example,\
    to_json_example, from_json_example, fastest_sort_example, cached_example, singleton_example, nd_vector_example


execute = {1: slow_sort_example,
           2: faster_sort_example,
           3: fastest_sort_example,
           4: from_json_example,
           5: to_json_example,
           6: cached_example,
           7: singleton_example,
           8: nd_vector_example}


def create_parser():
    parser_ = argparse.ArgumentParser()
    parser_.add_argument('task_number', choices=[1, 2, 3, 4, 5, 6, 7, 8], type=int,
                         help='Number of task: 1 - slow sort 2 - faster sort 3 - the fastest sort 4 - from json '
                              '5 - to json 6 - cached 7 - singleton 8 - n vector')
    parser_.add_argument('-n', type=int, help='Number for sorting',
                         default=1000)
    parser_.add_argument('-js', type=str, help='Json-string to parse',
                         default='{"color": {"color": "ppp","doors": true,"tires": [0.78,"data deleted","o"]},'
                                 ' "doors": true,"tires": [0.78,"data deleted","o"]}')
    return parser_


def main():

    parser = create_parser()

    args = parser.parse_args()

    if args.task_number <= 3:
        execute[args.task_number](args.n)

    elif args.task_number == 4:
        execute[args.task_number](args.js)

    else:
        execute[args.task_number]()


if __name__ == '__main__':
    main()
