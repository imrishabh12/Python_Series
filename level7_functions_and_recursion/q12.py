# Q12. Create a function using **kwargs.

def student_info(**kwargs):

    for key, value in kwargs.items():
        print(key, ":", value)


student_info(
    name="Rishabh",
    age=21,
    course="B.Tech",
    marks=85
)