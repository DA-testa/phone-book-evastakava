# python3

class Query:
    def _init_(self, query):
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
    # Use a dictionary to store contacts with numbers as keys
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            # Add contact to dictionary or update name if number already exists
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            # Remove contact from dictionary if it exists
            if cur_query.number in contacts:
                del contacts[cur_query.number]
        else:
            # Look up contact by number in dictionary
            response = contacts.get(cur_query.number, 'not found')
            result.append(response)
    return result

if _name_ == '_main_':
    write_responses(process_queries(read_queries()))

