# Class use can_speak animal project ....??



def can_speak(animal):
    if isinstance(animal, Person):
        return True
    elif isinstance(animal, Dog):
        return False
    else:
        raise RuntimeError('Unknown animal!')





def can_speak(animal):
    return animal.can_speak()