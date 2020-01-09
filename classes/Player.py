DEFAULT_SKILLS = {'perimeter_d': 1, 'post_d': 1, 'three_point': 1, 'midrange': 1, 'layup': 1, 'dunk': 1}

class Player:
    def __init__(self, name, skills=None):
        self.name = name
        if skills is None:
            self.skills = DEFAULT_SKILLS
        else:
            self.skills = skills

    def get_name(self):
        """
        Returns player name
        """
        return self.name

    def set_name(self, name):
        """
        Sets player name
        """
        self.name = name
        return self.name
    
    def get_skills(self):
        """
        Returns player skillset
        """
        return self.skills
    
    def increase_skill(self, skill, points=1):
        """
        Increments given player skill by given value, defaults to 1
        """
        if skill in self.skills:
            self.skills[skill] += points
            return self.skills
        return "Skill not found. Please check inputs."
