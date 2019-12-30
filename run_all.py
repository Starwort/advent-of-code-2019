for i in range(25):
    print(f" --- Day {i+1} ---")
    # uncomment this if you want to see a prettier day 23
    # if i == 22:
    #     import day23vis
    #     continue
    __import__(f"day{i+1:0>2}")
