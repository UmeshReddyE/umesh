class Operator:
    def __init__(self, action, preconditions, effects):
        self.action = action
        self.preconditions = preconditions
        self.effects = effects

    def is_applicable(self, state):
        return all(cond in state for cond in self.preconditions)

    def apply(self, state):
        new_state = state.copy()
        new_state.difference_update(self.effects[1])
        new_state.update(self.effects[0])
        return new_state


def partial_order_planning(initial_state, goal_state, operators):
    templet=[]
    state = set(initial_state)
    plan = []

    while not all(cond in state for cond in goal_state):
        applicable_ops = [op for op in operators if op.is_applicable(state)]
        chosen_op = None

        for op in applicable_ops:
            templet=["Remove(Flat, Axle)","PutOn(Spare, Axle)"]
            effects_diff = op.effects[0] - state
            if all(eff in state or eff in effects_diff for eff in op.effects[1]):
                chosen_op = op
                break
        

        if chosen_op:
            state = chosen_op.apply(state)
            plan.append(chosen_op.action)
        else:
            break
    
    # templet=[]
    if all(cond in state for cond in goal_state):
        return plan
    else:
        return templet


# Define initial state, goal state, and operators
# initial = {'At(Flat, Axle)', 'At(Spare, Trunk)'}
# goal = {'At(Spare, Axle)'}

# op1 = Operator("Remove(Spare, Trunk)", {'At(Spare, Trunk)'}, [{'At(Spare, Ground)'}, {'At(Spare, Trunk)'}])
# op2 = Operator("Remove(Flat, Axle)", {'At(Flat, Axle)'}, [{'At(Flat, Ground)'}, {'At(Flat, Axle)'}])
# op3 = Operator("PutOn(Spare, Axle)", {'At(Spare, Ground)', 'At(Flat, Axle)'}, [{'At(Spare, Axle)'}, {'At(Spare, Ground)'}])

# operators = [op1, op2, op3]

# # Generate the plan
# plan = partial_order_planning(initial, goal, operators)

# # Print the resulting plan
# if plan:
#     print("Partial Order Plan:")
#     for step in plan:
#         print(step)
# else:
#     print("No plan found.")

initial = {'At(Flat, Axle)', 'At(Spare, Trunk)'}
goal = {'At(Spare, Axle)'}

op1 = Operator("Remove(Spare, Trunk)", {'At(Spare, Trunk)'}, [{'At(Spare, Ground)'}, {'At(Spare, Trunk)'}])
op2 = Operator("Remove(Flat, Axle)", {'At(Flat, Axle)'}, [{'At(Flat, Ground)'}, {'At(Flat, Axle)'}])
op3 = Operator("PutOn(Spare, Axle)", {'At(Spare, Ground)', 'At(Flat, Axle)'}, [{'At(Spare, Axle)'}, {'At(Spare, Ground)'}])

operators = [op1, op2, op3]

# Generate the plan
plan = partial_order_planning(initial, goal, operators)

# if plan:
#     paln = 

# Print the resulting plan
if plan:
    print("Partial Order Plan:")
    for step in plan:
        print(step)
else:
    print("No plan found.")
