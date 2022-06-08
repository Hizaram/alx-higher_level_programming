#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is not None:
        score = -99999
        stud = None
        for k in a_dictionary.keys():
            if a_dictionary[k] == "" or a_dictionary[k] is None:
                return None
            if a_dictionary[k] > score:
                score = a_dictionary[k]
                stud = k
            return stud


if __name__ == '__main__':
    best_score = __import__('10-best_score').best_score

    a_dictionary = {'John': "", 'Bob': "", 'Mike': "", 'Molly': "", 'Adam': ""}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))
