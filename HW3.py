# Sean Maroongroge
# HW2
# Implementing HUI3

# define constants
starting_constant = 1.371
alpha_constant = 0.371

#create the dictionary
hui3Dict = {'Vision':        [1, 0.98 ,0.89, 0.84, 0.75, 0.61],
            'Hearing':       [1, 0.95, 0.89, 0.8, 0.74, 0.61],
            'Speech':        [1, 0.94, 0.89, 0.81, 0.68],
            'Ambulation':    [1, 0.93, 0.86, 0.73, 0.65, 0.58],
            'Dexterity':     [1, 0.95, 0.88, 0.76, 0.65, 0.56],
            'Emotion':       [1, 0.95, 0.85, 0.64, 0.46],
            'Cognition':     [1, 0.92, 0.95, 0.83, 0.6, 0.42],
            'Pain':          [1, 0.96, 0.9, 0.77, 0.55]}

#create the function that returns a HUI3 score
def HUI3_calculator(vision, hearing, speech, ambulation, dexterity, emotion, cognition, pain):
    """
    :param vision: user provided score
    :param hearing: user provided score
    :param speech: user provided score
    :param ambulation: user provided score
    :param dexterity: user provided score
    :param emotion: user provided score
    :param cognition: user provided score
    :param pain: user provided score
    :return: the HUI3 score corresponding to above scores
    """

    #check values in range
    if not (vision in range (1,7)):
        raise ValueError('Vision score must be 1-6')
    if not (hearing in range (1,7)):
        raise ValueError('Hearing score must be 1-6')
    if not (speech in range (1,6)):
        raise ValueError('Speech score must be 1-5')
    if not (ambulation in range (1,7)):
        raise ValueError('Ambulation score must be 1-6')
    if not (dexterity in range (1,7)):
        raise ValueError('Dexterity score must be 1-6')
    if not (emotion in range (1,6)):
        raise ValueError('Emotion score must be 1-5')
    if not (cognition in range (1,7)):
        raise ValueError('Cognition score must be 1-6')
    if not (pain in range (1,6)):
        raise ValueError('Pain score must be 1-5')

    #calc score
    score = starting_constant
    score *= hui3Dict['Vision'][vision-1]
    score *= hui3Dict['Hearing'][hearing-1]
    score *= hui3Dict['Speech'][speech-1]
    score *= hui3Dict['Ambulation'][ambulation-1]
    score *= hui3Dict['Dexterity'][dexterity-1]
    score *= hui3Dict['Emotion'][emotion-1]
    score *= hui3Dict['Cognition'][cognition-1]
    score *= hui3Dict['Pain'][pain-1]
    score -= alpha_constant

    return score

# input values here to test/choose what score you're printing
print HUI3_calculator(1 , 1 , 1 , 1 , 3, 1 , 1 , 1)

