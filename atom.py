while(1):
    import periodictable
    atomic_no=int(input("Enter the atomic no:"))
    element=periodictable.elements[atomic_no]
    print("Atomic number:",element.number)
    print("Symbol:",element.symbol)
    print("Name:",element.name)
    print("Atomic Mass:",element.mass)
    print("Density:",element.density)
    print("#################################")
