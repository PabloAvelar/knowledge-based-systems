from time import sleep


class InferenceEngine:
    def __init__(self, rules, facts, ui_objects, user_dialog):
        self.rules = rules
        self.facts = facts
        self.prev_goals = []
        self.marked_objects = [fact for fact in facts.keys()]
        self.active_rules = set(range(len(rules)))

        self.user_dialog = user_dialog
        self.ui_objects = ui_objects

    def backward_chaining(self, goal):

        print("-" * 30)
        print(f"Goal: {goal}")
        print(f"prev_goals: {self.prev_goals}")
        print(f"marked_objects: {self.marked_objects}")
        print(f"active_rules: {self.active_rules}")
        print("-" * 30)
        initial_goal = goal

        # Stage 1
        if goal in self.facts:
            return self.facts[goal]

        self.marked_objects.append(goal)

        # Stage 2
        while True:
            rule_found = None
            for i in self.active_rules:
                rule = self.rules[i]
                if rule["conclusion"] == goal and not all(obj in self.prev_goals for obj in rule["premise"]):
                    rule_found = i
                    print(f"Rule index: {rule_found}")
                    break

            print("*" * 30)
            print(f"Rule found: {rule_found}")
            print(f"Goal: {goal}")
            print(f"Rule conclusion: {rule['conclusion']}")
            print(f"prev_goals: {self.prev_goals}")
            print(f"marked_objects: {self.marked_objects}")
            print(f"active_rules: {self.active_rules}")
            print(f"Facts known: {self.facts}")
            print("-" * 30)

            if rule_found is not None:
                # Stage 3
                rule = self.rules[rule_found]
                premise = rule["premise"]

                print(f"rule: {rule}")
                print("Evaluando premisas...")
                if all(obj in self.facts for obj in premise) or (
                        rule["operator"] == "or" and any(self.facts.get(obj, False) for obj in premise)):
                    print("Premisas conocidas")

                    # Evaluating AND
                    if rule['operator'] == 'and' and all(self.facts[obj] for obj in premise):
                        self.facts[goal] = True
                        self.ui_objects[goal].configure(fg_color='green')
                    # Evaluating OR
                    elif rule['operator'] == 'or' and any(self.facts[obj] for obj in premise):
                        self.facts[goal] = True
                        self.ui_objects[goal].configure(fg_color='green')
                    else:
                        self.facts[goal] = False
                        self.ui_objects[goal].configure(fg_color='red')

                        # If the conclusion is false, at least one premise is false
                        for obj in premise:
                            if obj not in self.facts:
                                self.facts[obj] = False
                                self.ui_objects[goal].configure(fg_color='red')

                    self.active_rules.remove(rule_found)


                else:
                    # Stage 4
                    print("Premisas desconocidas")
                    if all(obj in self.marked_objects for obj in premise):
                        print("Premisas marcadas")
                        print(f"Rule: {rule}")
                        print(f"Rule index: {rule_found}")

                        self.active_rules.remove(rule_found)
                    else:
                        for obj in premise:
                            if obj not in self.facts and obj not in self.marked_objects:
                                print(f"Premisa no cumplida: {obj}")

                                # New goal and adding previous goal
                                self.prev_goals.append(goal)
                                if goal not in self.facts:
                                    self.ui_objects[goal].configure(fg_color='white')
                                goal = obj
                                self.ui_objects[goal].configure(fg_color='blue')
                                sleep(2)
                                print(f"Marking new goal: {goal}")
                                self.marked_objects.append(goal)
                                break
                    continue  # Go to stage 2

            else:
                # Stage 5
                if initial_goal != goal:
                    text_dialog = f"¿Cuál es el valor (True/False) de '{goal}'?"
                    dialog = self.user_dialog(text=text_dialog)
                    user_input = dialog.get_input()

                    # user_input = input(f"¿Cuál es el valor (True/False) de '{goal}'? (déjalo vacío si no se sabe): ")
                    if user_input.lower() == 'true':
                        self.facts[goal] = True
                        self.ui_objects[goal].configure(fg_color='green')
                    else:
                        self.facts[goal] = False
                        self.ui_objects[goal].configure(fg_color='red')

            # Stage 6
            if initial_goal != goal:
                if goal not in self.facts:
                    self.ui_objects[goal].configure(fg_color='white')
                goal = self.prev_goals.pop()  # Regresamos al objetivo anterior
                self.ui_objects[goal].configure(fg_color='blue')
                sleep(2)
                print("New goal from stack: ", goal)
            if goal in self.facts:
                # Stage 7
                return self.facts.get(goal, "No se pudo determinar el valor.")

        return self.facts[initial_goal]

# facts = {
#     "D": True,
#     "F": True,
#     "E": True,
#     "L": True,
# }

# facts = {
#     "D": True,
#     "F": True,
#     "E": True,
#     "L": True,
# }
#
#
# rules = [
#     {"premise": ["A", "B"], "conclusion": "C"},  # Regla 1
#     {"premise": ["D", "E", "F"], "conclusion": "G"},  # Regla 2
#     {"premise": ["H", "I"], "conclusion": "J"},  # Regla 3
#     {"premise": ["C", "G"], "conclusion": "K"},  # Regla 4
#     {"premise": ["G", "J"], "conclusion": "L"},  # Regla 5
#     {"premise": ["K", "L"], "conclusion": "M"},  # Regla 6
# ]
#
#
# engine = InferenceEngine(rules, facts)
#
# goal = "M"
# result = engine.backward_chaining(goal)
#
# print(f"The value of {goal} is {result}")
