# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Use a dictionary to store the phone numbers and names
    phone_book = {}
    for cq in queries:
        if cq.type == 'add':
            # if we already have contact with such number,
            # we should overwrite the contact's name
            phone_book[cq.number] = cq.name
        elif cq.type == 'del':
            # Check if the phone number is in the dictionary before deleting
            if cq.number in phone_book:
                del phone_book[cq.number]
        else:
            # Check if the phone number is in the dictionary before finding
            if cq.number in phone_book:
                result.append(phone_book[cq.number])
            else:
                result.append('not found')
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

