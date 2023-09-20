def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    # batch_list = list()
    # for name in names:
    #     batch_list.append(badge_maker(name))
    batch_list = [badge_maker(name) for name in names]
    return batch_list

def assign_rooms(names):
    assign_list = list()
    # for index in range(len(names)):
    #     message = f'Hello, {names[index]}! You\'ll be assigned to room {index + 1}!'
    #     assign_list.append(message)
    assign_list = [f'Hello, {names[index]}! You\'ll be assigned to room {index + 1}!' for index in range(len(names))]
    return assign_list

def printer(names):
    for batch in batch_badge_creator(names):
        print(batch)
    for assign in assign_rooms(names):
        print(assign)
