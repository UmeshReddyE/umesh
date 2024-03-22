class Operation:
    def _init_(self, action, preconditions, effects):
        self.action = action
        self.preconditions = preconditions
        self.effects = effects

def apply_operation(state, operation):
    # Check if preconditions are met
    if all(precond in state for precond in operation.preconditions):
        # Remove preconditions
        state.difference_update(operation.preconditions)
        # Add effects
        state.update(operation.effects)

def partial_order_planning(start_state, goal_state, operations):
    plan = []
    state = start_state.copy()

    while not all(goal in state for goal in goal_state):
        # applicable_operations = list(filter(lambda op: all(precond in state for precond in op.preconditions), operations))

        applicable_operations = [op for op in operations if all(precond in state for precond in op.preconditions)]
        chosen_operation = min(applicable_operations, key=lambda op: operations.index(op))

        apply_operation(state, chosen_operation)
        plan.append(chosen_operation.action)

    return plan

# Define the operations
o = Operation()
op1 = o._init_("Remove(Spare, Trunk)", {"At(Spare, Trunk)"}, {"At(Spare, Ground)", "-At(Spare, Trunk)"})
op2 = o._init_("Remove(Flat, Axle)", {"At(Flat, Axle)"}, {"At(Flat, Ground)", "-At(Flat, Axle)"})
op3 = o._init_("PutOn(Spare, Axle)", {"At(Spare, Ground)", "At(Flat, Axle)"}, {"At(Spare, Axle)", "-At(Spare, Ground)"})
op4 = o._init_("LeaveOvernight", set(), {"-At(Spare, Ground)", "-At(Spare, Axle)", "-At(Spare, Trunk)",
                                          "-At(Flat, Ground)", "-At(Flat, Axle)"})

# Define the initial and goal states
start_state = {"At(Flat, Axle)", "At(Spare, Trunk)"}
goal_state = {"At(Spare, Axle)"}

# Define the partial order plan
plan = partial_order_planning(start_state, goal_state, [op1, op2, op3, op4])

# Print the plan
print("Partial Order Plan:")
for action in plan:
    print(action)