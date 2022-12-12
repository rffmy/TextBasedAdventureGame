# definition of the class
class House:
    # Class has low (0.00%) cohesion. Cohesion measures the strength
    # of relationship between pieces of functionality within a given module.
    # When cohesion is high, the methods and variables of the class are
    # co-dependent and hang together as a logical whole.
    # However, if the task requires implementing classes without methods,
    # the cohesion always will be low since all variables will be in-dependent.
    # Please, ignore this issue if the task requires implement an empty class
    # (without any methods).
    construction = "building"
    elevator = True

    def get_attributes(self):
        return self.construction, self.elevator


# object of the class House
new_house = House()
