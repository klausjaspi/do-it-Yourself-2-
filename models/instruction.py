instruction_list = [{
    "id": "1",
    "name": "Paint a Car",
    "description": "Instructions how to paint a car!",
    "steps": ["Wash the car", "Dry the car", "Remove old paint", "Spray paint 2-3 layers of new paint in safe place"],
},
    {"id": "2",
     "name": "Paint a House",
     "description": "Instructions how to paint a house",
     "steps": ["Remove old paint", "Paint 2-3 layers of new paint"],
     }]


def get_last_id():
    if instruction_list:
        last_instruction = instruction_list [-1]

    else:
        return 1
    return last_instruction.id + 1


class Instruction:

    def __init__(self, name, description, steps, tools, cost, duration):

        self.id = get_last_id()
        self.name = name
        self.description = description
        self.steps = steps
        self.tools = tools
        self.cost = cost
        self.duration = duration
        self.is_publish = True

    @property
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'steps': self.steps
        }
