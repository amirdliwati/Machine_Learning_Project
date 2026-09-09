while True:
    try:
        n = input("enter int number")
        n = int(n)
        break
    except ValueError:
        print("bad")
    finally:
        print("good2")
    
