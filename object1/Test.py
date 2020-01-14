from object1.Student import Student

def get_score(self):
    return {'chanidsoi':893298}



def monkeypatch4Student():
    Student.get_score = get_score


if __name__ == '__main__':
    tom = Student('tomc', english=80, chinese=20, shanshan=80)
    print(tom.get_score())
    monkeypatch4Student()
    print(tom.get_score())