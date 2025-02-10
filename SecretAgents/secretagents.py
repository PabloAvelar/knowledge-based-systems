class SecretAgents:
    def __init__(self, rules, canvas, CTkButton, CTkTopLevel):
        self.rules = rules
        self.canvas = canvas
        self.CTkButton = CTkButton
        self.CTkTopLevel = CTkTopLevel

        self.hash_agents = {
            'ES': None,
            'F': None,
            'EG': None,
            'J': None
        }

        self.colors = ["#ffc9c9", "#feec98", "#b2f3bb"]

        self.agents_marked = []

    @staticmethod
    def is_negation_rule(rule) -> bool:
        key = list(rule.keys())[0]
        return '-' in key

    @staticmethod
    def make_negation(rule) -> str:
        """
        For a given rule, create a negation rule
        :param rule:
        :return:
        """
        rule = list(rule.values())[0]
        rule = rule.replace('/', '/-')
        return rule

    @staticmethod
    def is_neg_of_current_rule(current_rule, neg_rule) -> bool:
        current_rule_str = list(current_rule.keys())[0]
        current_rule_str = current_rule_str.replace('/-', '/')

        neg_rule_str = list(neg_rule.keys())[0]
        neg_rule_str = neg_rule_str.replace('/-', '/')

        return neg_rule_str == current_rule_str

    @staticmethod
    def get_country(rule, type='key') -> str:
        if type == 'value':
            return list(rule.values())[0].split('/')[1]

        return list(rule.keys())[0].split('/')[1]

    @staticmethod
    def get_agent(rule, type='key') -> str:
        if type == 'value':
            return list(rule.values())[0].split('/')[0]

        return list(rule.keys())[0].split('/')[0]

    def get_neg_rules(self, current_rule):
        """
        For a given rule, create a list of negation rules to apply
        The exception rule is the negation of the current rule

        :param current_rule: dict
        :return: list
        """

        neg_rules = []
        for rule in self.rules:
            if SecretAgents.is_negation_rule(rule) and not SecretAgents.is_neg_of_current_rule(current_rule, rule):
                neg_rules.append(rule)
        return neg_rules

    def draw_rule_nodes(self, text, x, y, i, color=None):
        if color is None:
            color = self.colors[i]
            print("Color: ", color)
            print("i: ", i)

        self.CTkButton(self.canvas, text=f"{text}", width=50, height=50, corner_radius=100,
                       bg_color='transparent', text_color="#000", border_width=2, fg_color=color).place(x=x,
                                                                                                        y=y)

    def get_rule_number(self, consequent):
        """
        Get the index of a rule given the rule consequent.
        :param consequent:
        :return:
        """
        for rule in self.rules:
            if list(rule.values())[0] == consequent:
                return self.rules.index(rule)

    def chaining_rules(self, main_rule) -> bool:
        """
        For a given rule, apply the corresponding rule to the hash_agents dictionary
        :param main_rule: dict
        :return: bool
        """

        print("Main rule", main_rule)
        neg_rules = self.get_neg_rules(main_rule)

        # Adding Tomas to the hash_agents dictionary
        secret_agent_country = SecretAgents.get_country(main_rule)
        print(secret_agent_country)
        self.hash_agents[secret_agent_country] = 'Tomas'

        # For nodes aesthetics and form
        y_button = 200
        i = 0

        # Display the rule number
        rule_number = self.get_rule_number(list(main_rule.values())[0])
        self.canvas.create_text(150, 90, text=f"Regla {rule_number + 1}", font=("Arial", 12))

        # Apply the rules
        for rule in neg_rules:
            x_button = 300

            # Check if Tomas is in the rule
            agent_country = SecretAgents.get_country(rule, type='value')
            mapped_agent = self.hash_agents[agent_country]
            agent = SecretAgents.get_agent(rule, type='value')
            key = list(rule.keys())[0]

            # Draw a line to connect nodes
            self.canvas.create_line(100, 100, x_button + 20, y_button + 20, fill='black', width=2)
            if mapped_agent == 'Tomas':
                value = SecretAgents.make_negation(rule)
                # self.canvas.create_line(100, 100, x_button, y_button, fill='black', width=2)

                # Display the rule number
                rule_number = self.get_rule_number(value)
                self.canvas.create_text(x_button + 100, y_button - 10, text=f"Regla {rule_number + 1}",
                                        font=("Arial", 12))

                # Draw a line to connect nodes
                self.canvas.create_line(x_button, y_button + 25, x_button + 300, y_button + 25, fill='black', width=2)

                # Key node
                self.draw_rule_nodes(key, x_button, y_button, i)
                x_button += 300

                # Value node
                self.draw_rule_nodes(value, x_button, y_button, i)

                y_button += 100

                result = {key: value}
                print("|--:", result)
            # Check if the agent is not already in the hash_agents dictionary, then add the agent
            elif mapped_agent is None and agent not in self.agents_marked:
                value = list(rule.values())[0]
                self.hash_agents[agent_country] = agent
                # Marking the agent as already added
                self.agents_marked.append(agent)

                # Display the rule number
                rule_number = self.get_rule_number(value)
                self.canvas.create_text(x_button + 100, y_button - 10, text=f"Regla {rule_number + 1}",
                                        font=("Arial", 12))

                # Draw a line to connect nodes
                self.canvas.create_line(x_button, y_button + 25, x_button + 300, y_button + 25, fill='black', width=2)

                # Key node
                self.draw_rule_nodes(key, x_button, y_button, i)
                x_button += 300

                # Value node
                self.draw_rule_nodes(value, x_button, y_button, i)

                y_button += 100

                # Draw a line to connect nodes

                print("|-- : ", rule)
                # print("Tomas is in the rule")
                # continue
            else:
                print("FALSE RULE")

                value = list(rule.values())[0]
                self.hash_agents[agent_country] = agent
                # Marking the agent as already added
                self.agents_marked.append(agent)

                # Draw a line to connect nodes
                self.canvas.create_line(x_button, y_button + 25, x_button + 300, y_button + 25, fill='black', width=2)

                # Key node
                self.draw_rule_nodes(key, x_button, y_button, i, color="red")
                x_button += 300
                # Value node
                self.draw_rule_nodes(value, x_button, y_button, i, color="red")
                y_button += 100

                print("|-- : ", rule)
                return False

            i += 1

        return True

# Rules for Tomas position
# Save the current index position of Tomas in order to apply the correct neg rule
# Neg_rule for the current rule: current_index + 1

# To determine a negation rule, make a function to extract the hyphen within the key in the rules dictionary

# rules = [
#     {'T/F': 'L/-ES'},  # Rule 1
#     {'T/-F': 'L/ES'},  # Rule 2
#     {'T/ES': 'A/-F'},  # Rule 3
#     {'T/-ES': 'A/F'},  # Rule 4
#     {'T/EG': 'C/-EG'},  # Rule 5
#     {'T/-EG': 'C/EG'},  # Rule 6
#     {'T/J': 'C/-F'},  # Rule 7
#     {'T/-J': 'C/F'},  # Rule 8
# ]

# secret_agents = SecretAgents(rules)
# index = 4
# rule = rules[index]
# secret_agents.chaining_rules(rule)
# print("rule: ", rule)
# is_neg = secret_agents.is_negation_rule(rule)
# print("is_neg: ", is_neg)
# new_neg = secret_agents.make_negation(rule)
# print("new_neg", new_neg)
