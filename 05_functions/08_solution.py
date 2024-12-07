def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


print_kwargs(Name="Rohit", Designation="IT Officer", Salary="100000")
