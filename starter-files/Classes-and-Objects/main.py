def change_name(name):
    name = name
    return name


def change_age(age):
    age = age
    return int(age)


class Student:

    # [assignment] Skeleton class. Add your code here

    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def add_track(self, tracks):
        return self.tracks + [tracks]

    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)
if __name__ == '__main__':
    # Expected methods
    print(change_name("Peter"))
    print(change_age(34))
    print(Bob.add_track("UI/UX"))
    print(Bob.get_score())
